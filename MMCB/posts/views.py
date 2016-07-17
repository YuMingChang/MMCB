from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from posts.custom_function import req_field_getlist
from posts.forms import ProductForm, DetailForm, DetailFormSet
from products.models import Product, Detail

# Create your views here.
def post_list(request):
    queryset = Product.objects.all()
    context = {
        'title' : 'List',
        'object_list': queryset,
    }
    return render(request, 'posts/post_list.html', context)

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
        'title' : 'Create',
        'form': form,
    }
    return render(request, 'posts/post_create.html', context)

def post_update(request, id=None):
    instance = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=instance, submit_title='更新商品')
    detail_formset = DetailFormSet(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid() and detail_formset.is_valid():
        instance = form.save(commit=False)
        instance.save()
        detail_formset.save()
        messages.success(request, 'Item Saved')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'title' : 'Edit',
        'instance' : instance,
        'form' : form,
        'detail_formset': detail_formset
    }
    return render(request, 'posts/post_update.html', context)

def post_delete(request, id=None):
    instance = get_object_or_404(Product, id=id)
    instance.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect('posts:list')


# 商品內容新增
def post_add_detail(request):
    allProduct = Product.objects.all()
    nameList = []
    for objName in allProduct:  # get All of the Product Name
        nameList.append(objName)

    # 求Django常用语法，接受get和post参数的方法: http://zhidao.baidu.com/question/554222227.html
    if request.method == "POST":
        color_list = []
        size_list = []
        price_list = []

        section = request.POST.get('optradio')      # 從網頁回傳所選「新增商品內容格式」 (Radio Button)
        productName = request.POST.get('optName')   # 從網頁回傳所選「新增商品目標的名稱」(Select List)
        if section is not None and productName is not None: # Check section is a NoneType or not(RadioBox has been check or not.)
            colorField = section + 'color'               # color = S1color0~10   / S2color0~10   / S3color0~10
            sizeField = section + 'size'                 # size  = S1size0~10    / S2size0~10    / S3size0~10
            priceField = section + 'price'               # price = S1price0~10   / S2price0~10   / S3price0~10
            # print (color, size ,price)

            product = Product.objects.get(name=productName)
            # color_list = req_field_get(request, colorField)
            # size_list = req_field_get(request, sizeField)
            # price_list = req_field_get(request, priceField)
            color_list = req_field_getlist(request, colorField)
            size_list = req_field_getlist(request, sizeField)
            price_list = req_field_getlist(request, priceField)
            # print (color_list, size_list, price_list)

            if section == 'S1':     # Color - Size - Price
                for i in range(len(price_list)):
                    Detail.objects.create(product=product, color=color_list[i], size=size_list[i], price=price_list[i])
            elif section == 'S2':   # [Color - Pirce] * Size
                for i in range(len(size_list)):
                    for j in range(len(color_list)):
                        Detail.objects.create(product=product, color=color_list[j], size=size_list[i], price=price_list[j])
            elif section == 'S3':   # [Size - Price] * Color
                for i in range(len(color_list)):
                    for j in range(len(size_list)):
                        Detail.objects.create(product=product, color=color_list[i], size=size_list[j], price=price_list[j])

    context = {
        'title' : 'Add Detail',
        'productsName' : nameList,
    }
    return render(request, 'posts/post_add_detail.html', context)

# What the difference between using Django redirect and HttpResponseRedirect?:
# http://stackoverflow.com/questions/13304149/what-the-difference-between-using-django-redirect-and-httpresponseredirect
