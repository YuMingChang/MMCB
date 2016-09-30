from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
from members.models import PersonalInfo
from members.forms import PersonalInfoForm
from checkout.models import PurchaseOrder


@login_required
def member_page(request):
    context = {
        'title': '個人資訊',
    }
    return render(request, 'members/member-page.html', context)


@login_required
def member_info(request):
    errors = []
    form = PersonalInfoForm()
    try:
        req_personalinfo = request.user.personalinfo
        # Load if PersonalInfo has been create.
        instance = get_object_or_404(PersonalInfo, id=req_personalinfo.id)
        form = PersonalInfoForm(request.POST or None, instance=instance)
    except:
        # Create if PersonalInfo has not been create.
        form = PersonalInfoForm(request.POST or None, initial={'user': request.user.id})
        errors.append("您必須先填寫完整資料，才可以開始大買特買唷～")
    finally:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect(reverse('member:page'))
    context = {
        'title': '資料編輯',
        'form': form,
        'errors': errors,
    }
    return render(request, 'members/member-info.html', context)


@login_required
def member_shoppinglist(request):
    errors = []
    order_list = None
    try:
        order_list = PurchaseOrder.objects.filter(shopper=request.user.personalinfo)
    except:
        errors.append("請先完整資料填寫後在開始大買特買唷～")
        return redirect(reverse('member:info'))
    context = {
        'title': '購物清單',
        'order_list': order_list,
        'errors': errors,
    }
    return render(request, 'members/member-shoppinglist.html', context)


@login_required
def member_order(request, number=None):
    errors = []
    myorder = None
    try:
        myorder = get_object_or_404(PurchaseOrder, number=float(number))
    except:
        errors.append('系統錯誤，拿不到訂單')
        return redirect(reverse('member:page'))
    context = {
        'title': '我的訂單',
        'myorder': myorder,
        'errors': errors,
    }
    return render(request, 'members/member_order.html', context)


@login_required
def member_orderstatus(request, number=None, do=None):
    errors = []
    try:
        order = get_object_or_404(PurchaseOrder, number=float(number))
        status = order.status
        if do is not None:
            if status == 'UP' and do == 'PA':
                order.status = 'PA'
            elif status == 'UP' and do == 'AB':
                order.status = 'AC'
            elif status == 'AC' and do == 'CA':
                order.status = 'UP'
            else:
                errors.append('動作錯誤，請重新執行！')
            order.save()
        return redirect(reverse('member:shoppinglist'))
    except:
        pass


@login_required
def member_others(request):
    qs_user = User.objects.all()
    qs_email = EmailAddress.objects.all()
    qs_facebook = SocialAccount.objects.all()
    qs_personal = PersonalInfo.objects.all()
    context = {
        'title': '會員資料',
        'qs_user': qs_user,
        'qs_email': qs_email,
        'qs_facebook': qs_facebook,
        'qs_personal': qs_personal,
    }
    return render(request, 'members/member-others.html', context)
