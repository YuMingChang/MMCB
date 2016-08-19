from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.admin.views.decorators import staff_member_required

from posts.forms import ProductForm, DetailForm, DetailFormSet
from products.models import Product, Detail

def meta(request):
    values = request.META.items()
    sorted(values)
    html = []
    for k, v in values:
        html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(k, v))
    return HttpResponse('<table>{0}</table>'.format('\n'.join(html)))

@staff_member_required
def post_list(request):
    queryset = Product.objects.all()
    context = {
        'title' : '商品列表',
        'object_list': queryset,
    }
    return render(request, 'posts/post_list.html', context)

@staff_member_required
def post_create(request):
    form = ProductForm(request.POST or None, request.FILES or None, submit_title='新增商品')
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Successfully Created')
        return HttpResponseRedirect(instance.get_absolute_url())
    # else:
        # messages.error(request, 'Not Successfully Created')
    context = {
        'title' : '新增商品',
        'form': form,
    }
    return render(request, 'posts/post_create.html', context)

@staff_member_required
def post_update(request, id=None):
    instance = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=instance, submit_title='更新商品')
    detail_formset = DetailFormSet(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid() and detail_formset.is_valid():
        instance = form.save(commit=False)
        detail_formset.save()
        instance.save()
        messages.success(request, 'Item Saved')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'title' : '商品編輯',
        'instance' : instance,
        'form' : form,
        'detail_formset': detail_formset
    }
    return render(request, 'posts/post_update.html', context)

@staff_member_required
def post_delete(request, id=None):
    instance = get_object_or_404(Product, id=id)
    instance.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect(instance.get_absolute_url())


@staff_member_required
def post_add_detail(request):
    queryset = Product.objects.all()
    errors = []
    context = {
        'title' : '新增商品內容',
        'object_list' : queryset,
        'errors' : errors,
    }

    # 求Django常用语法，接受get和post参数的方法: http://zhidao.baidu.com/question/554222227.html
    # [request.POST.get('sth') vs request.POST['sth'] - difference?](http://stackoverflow.com/questions/12518517/request-post-getsth-vs-request-poststh-difference)
    if request.POST:
        section = request.POST.get('optradio')      # 從網頁回傳所選「新增商品內容格式」 (Radio Button)
        selObj  = request.POST.get('optName')       # 從網頁回傳所選「新增商品目標的名稱」(Select List)
        if section != None and selObj != None:      # Check section is a NoneType or not(RadioBox has been check or not.)
            color_list, size_list, price_list = ([] for i in range(3))      # Initializing Multiple Lists/Line
            color_list  = request.POST.getlist(section + 'color')
            size_list   = request.POST.getlist(section + 'size')
            price_list  = request.POST.getlist(section + 'price')
            lst = [color_list, size_list, price_list]
            for tmp in lst:
                while '' in tmp:
                    tmp.remove('')
            context['input_list'] = lst

            product = Product.objects.get(id=selObj)
            if section == 'S1' and all(len(x) == len(lst[2]) for x in lst):     # Color - Size - Price
                for i in range(len(price_list)):
                    Detail.objects.create(product=product, color=color_list[i], size=size_list[i], price=price_list[i])
                color_list, size_list, price_list = ('', '', '')
                return HttpResponseRedirect('/posts/{id}/edit'.format(id=selObj))
            elif section == 'S2' and len(lst[1])==len(lst[2]):                  # [Color - Pirce] * Size
                for i in range(len(size_list)):
                    for j in range(len(color_list)):
                        Detail.objects.create(product=product, color=color_list[j], size=size_list[i], price=price_list[j])
                color_list, size_list, price_list = ('', '', '')
                return HttpResponseRedirect('/posts/{id}/edit'.format(id=selObj))
            elif section == 'S3' and len(lst[0])==len(lst[2]):                  # [Size - Price] * Color
                for i in range(len(color_list)):
                    for j in range(len(size_list)):
                        Detail.objects.create(product=product, color=color_list[i], size=size_list[j], price=price_list[j])
                color_list, size_list, price_list = ('', '', '')
                return HttpResponseRedirect('/posts/{id}/edit'.format(id=selObj))
            else:
                errors.append("資料輸入有缺少，請重新確認！")
        else:
            errors.append("請記得選擇所新增商品，填寫內容後再次確認！")
    return render(request, 'posts/post_add_detail.html', context)

# What the difference between using Django redirect and HttpResponseRedirect?:
# http://stackoverflow.com/questions/13304149/what-the-difference-between-using-django-redirect-and-httpresponseredirect
