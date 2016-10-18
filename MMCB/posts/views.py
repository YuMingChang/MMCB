from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from posts.forms import ProductForm, DetailFormSet, ImageFormSet
from products.models import Product, Detail, Images
from members.models import PersonalInfo
from checkout.models import PurchaseOrder


@staff_member_required
def meta(request):
    values = request.META.items()
    sorted(values)
    html = []
    for k, v in values:
        html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(k, v))
    return HttpResponse('<table>{0}</table>'.format('\n'.join(html)))


@staff_member_required
def post_page(request):
    context = {
        'title': '管理頁面',
    }
    return render(request, 'posts/post_page.html', context)


@staff_member_required
def post_products_list(request):
    errors = []
    good_queryset = Product.objects.all()
    if request.method == 'GET' and 'search_name' in request.GET:
        try:
            good_queryset = Product.objects.filter(name__icontains=request.GET.get('search_name', None))
        except:
            errors.append('搜尋不到資料，請重新嘗試！')
    context = {
        'title': '商品管理列表',
        'errors': errors,
        'good_queryset': good_queryset,
    }
    return render(request, 'posts/post_products_list.html', context)


@staff_member_required
def post_product_add(request):
    product_form = ProductForm(request.POST or None, request.FILES or None, )
    image_formset = ImageFormSet(
        request.POST or None, request.FILES or None,
        queryset=Images.objects.none(),
    )
    if product_form.is_valid() and image_formset.is_valid():
        try:
            instance = product_form.save(commit=False)
            instance.save()
            for form in image_formset.cleaned_data:
                try:
                    image = form['image']
                    photo = Images(product=instance, image=image)
                    photo.save()
                except KeyError:
                    pass
            messages.success(request, 'Product Successfully Created')
            return redirect(reverse('posts:productlist'))
        except:
            messages.error(request, 'Product Not Successfully Created')
    context = {
        'title': '新增商品',
        'form': product_form,
        'formset': image_formset,
    }
    return render(request, 'posts/post_products_create.html', context)


@staff_member_required
def post_product_update(request, good_id=None):
    good = get_object_or_404(Product, id=good_id)
    product_form = ProductForm(
        request.POST or None, request.FILES or None,
        submit_title='確定修改商品', instance=good, )
    detail_formset = DetailFormSet(
        request.POST or None, request.FILES or None, instance=good, )
    image_formset = ImageFormSet(
        request.POST or None, request.FILES or None, instance=good, )
    if product_form.is_valid() and detail_formset.is_valid() and image_formset.is_valid():
        good = product_form.save(commit=False)
        detail_formset.save()
        image_formset.save()
        good.save()
        messages.success(request, 'Item Saved')
        return redirect(reverse('posts:productlist'))
    context = {
        'title': '商品編輯',
        'good': good,
        'form': product_form,
        'detail_formset': detail_formset,
        'image_formset': image_formset,
    }
    return render(request, 'posts/post_products_update.html', context)


@staff_member_required
def post_product_delete(request, good_id=None):
    good = get_object_or_404(Product, id=good_id)
    good.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect(reverse('posts:productlist'))


@staff_member_required
def post_detail_add(request, good_id=None):
    goods_id_name = Product.objects.all().values_list('id', 'name')
    errors = []
    context = {
        'title': '新增商品內容',
        'goods_id_name': goods_id_name,
        'selID': good_id,
        'errors': errors,
    }

    # [求Django常用语法，接受get和post参数的方法]
    # (http://zhidao.baidu.com/question/554222227.html)
    # [request.POST.get('sth') vs request.POST['sth'] - difference?]
    # (http://stackoverflow.com/questions/12518517/request-post-getsth-vs-request-poststh-difference)
    if request.POST:
        # 從網頁回傳所選「新增商品內容格式」 (Radio Button)
        section = request.POST.get('selRadio')
        # 從網頁回傳所選「新增商品內容格式」 (Radio Button)
        selObj = request.POST.get('selOption')
        # Check section is a NoneType or not(RadioBox has been check or not.)
        if section and selObj:
            # Initializing Multiple Lists/Line
            color_list, size_list, price_list = ([] for i in range(3))
            color_list = request.POST.getlist(section + 'color')
            size_list = request.POST.getlist(section + 'size')
            price_list = request.POST.getlist(section + 'price')
            lst = [color_list, size_list, price_list]
            for tmp in lst:
                while '' in tmp:
                    tmp.remove('')
            context['input_list'] = lst
            product = Product.objects.get(id=selObj)
            try:
                created_flag = False
                if any(len(x) == 0 for x in lst):
                    created_flag = False

                # Color - Size - Price
                elif (section == 'S1' and all(len(x) == len(lst[2]) for x in lst)):
                    for i in range(len(price_list)):
                        Detail.objects.create(
                            product=product,
                            color=color_list[i],
                            size=size_list[i],
                            price=price_list[i]
                        )
                    created_flag = True

                # [Color - Pirce] * Size
                elif section == 'S2' and len(lst[0]) == len(lst[2]):
                    for i in range(len(size_list)):
                        for j in range(len(color_list)):
                            Detail.objects.create(
                                product=product,
                                color=color_list[j],
                                size=size_list[i],
                                price=price_list[j]
                            )
                    created_flag = True

                # [Size - Price] * Color
                elif section == 'S3' and len(lst[1]) == len(lst[2]):
                    for i in range(len(color_list)):
                        for j in range(len(size_list)):
                            Detail.objects.create(
                                product=product,
                                color=color_list[i],
                                size=size_list[j],
                                price=price_list[j]
                            )
                    created_flag = True
                if created_flag:
                    color_list, size_list, price_list = ('', '', '')
                    return redirect(reverse('posts:update', kwargs={'good_id': selObj}))
                else:
                    errors.append("資料輸入有所缺少，請重新確認！")
            except ValueError:
                errors.append("資料輸入型態有誤，請重新確認！")
        else:
            errors.append("請記得選擇所新增商品，填寫內容後再次確認！")
    return render(request, 'posts/post_products_add_detail.html', context)

# What the difference between using Django redirect and HttpResponseRedirect?:
# http://stackoverflow.com/questions/13304149/what-the-difference-between-using-django-redirect-and-httpresponseredirect


@staff_member_required
def post_orders_list(request):
    errors = []
    order_queryset = PurchaseOrder.objects.all()
    get_list = ['search_name', 'selOrderStatus', 'search_year', 'search_month']
    str_search = '你所搜尋的'
    if request.method == 'GET' and any(sel in request.GET for sel in get_list):
        try:
            buyer, status, year, month = [request.GET.get(item, None) for item in get_list]
            print ('buyer= {}, status= {}, year= {}, month= {}'.format(buyer, status, year, month))
            if buyer is not None and buyer != '':
                personal = PersonalInfo.objects.filter(name__icontains=buyer)
                order_queryset = PurchaseOrder.objects.filter(shopper=personal)
                str_search += ' 買家：{} /'.format(buyer)
                if personal.exists() is False or order_queryset.exists() is None:
                    errors.append('搜尋不到資料，請重新嘗試！')
                    order_queryset = PurchaseOrder.objects.all()
            if year is not None and year != '':
                order_queryset = order_queryset.filter(order_date__year=year)
                str_search += ' 年份：{} /'.format(year)
            if month is not None and month != '':
                order_queryset = order_queryset.filter(order_date__month=month)
                str_search += ' 月份：{} /'.format(month)
            if status is not None:
                order_queryset = order_queryset.filter(status=status)
                str_search += ' 狀態：{} /'.format(dict(PurchaseOrder.ORDER_STATUS)[status])
        except ValueError:
            errors.append('輸入數值有誤，請重新輸入，謝謝！')
    context = {
        'title': '訂單管理列表',
        'order_queryset': order_queryset,
        'errors': errors,
    }
    if len(str_search) > 5:
        context['str_search'] = str_search
    return render(request, 'posts/post_orders_list.html', context)


@staff_member_required
def posts_order(request, number):
    order = get_object_or_404(PurchaseOrder, number=number)
    buyer = get_object_or_404(PersonalInfo, id=order.shopper.id)
    context = {
        'title': '訂單',
        'myorder': order,
        'buyer': buyer,
        'all_status': order.ORDER_STATUS,
    }
    return render(request, 'posts/post_order.html', context)


@staff_member_required
def posts_order_update(request, number, do):
    order = get_object_or_404(PurchaseOrder, number=number)
    if do is not None:
        if do in ['UP', 'PA', 'PC', 'WS', 'SN', 'AB', 'CA', 'AC', 'AD']:
            if do == 'AD':
                print ('{}'.format(order.sold_goods.all()))
            order.status = do
            order.save()
    return redirect(reverse('posts:order', kwargs={'number': number}))
