from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
from members.models import PersonalInfo
from members.forms import PersonalInfoForm


@login_required
def member_page(request):
    context = {
        'title': '個人資訊',
    }
    return render(request, 'members/member-page.html', context)


@login_required
def member_info(request):
    req_qs_personal = request.user.personalinfo_set.all()
    errors = []

    form = PersonalInfoForm()
    # Create if PersonalInfo has not been create.
    if req_qs_personal.count() == 0:
        form = PersonalInfoForm(
                    request.POST or None, initial={'user': request.user.id})
    # Load if PersonalInfo has been create.
    elif req_qs_personal.count() == 1:
        instance = get_object_or_404(PersonalInfo, id=req_qs_personal[0].id)
        form = PersonalInfoForm(request.POST or None, instance=instance)
    else:
        errors.append('資料有誤，請聯繫工作人員！')
    if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('member:page')

    context = {
        'title': '資料編輯',
        'errors': errors,
        'form': form,
    }
    return render(request, 'members/member-info.html', context)


@login_required
def member_shoppinglist(request):
    context = {
        'title': '購物清單',
    }
    return render(request, 'members/member-shoppinglist.html', context)


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
