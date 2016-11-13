from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
from members.models import PersonalInfo, Addresses, Accounts, FamilyNumber
from checkout.models import PurchaseOrder
from members.forms import PersonalInfoForm, AddressesFormSet, AccountsFormSet, FamilyNumberFormSet
from carton.cart import Cart
from datetime import datetime


@login_required
def member_page(request):
    errors = []
    cart = Cart(request.session)
    if not cart.is_empty:
        errors.append('您還有商品在購物車內尚未結帳')
    context = {
        'title': '個人資訊',
        'errors': errors,
    }
    return render(request, 'members/member-page.html', context)


@login_required
def member_info(request):
    errors = []
    first_flag = False
    info_form = PersonalInfoForm(request.POST or None)
    adr_formset = AddressesFormSet(None, queryset=Addresses.objects.none())
    act_formset = AccountsFormSet(None, queryset=Accounts.objects.none())
    num_formset = FamilyNumberFormSet(None, queryset=FamilyNumber.objects.none())
    try:
        # Load if PersonalInfo has been create.
        req_userinfo = request.user.personalinfo
        personalinfo = get_object_or_404(PersonalInfo, id=req_userinfo.id)
        info_form = PersonalInfoForm(request.POST or None, instance=personalinfo)
        print ('PersonalInfo LOADED')
        adr_formset = AddressesFormSet(request.POST or None, instance=personalinfo)
        act_formset = AccountsFormSet(request.POST or None, instance=personalinfo)
        num_formset = FamilyNumberFormSet(request.POST or None, instance=personalinfo)
    except ObjectDoesNotExist:
        # Create if PersonalInfo has not been create.
        info_form = PersonalInfoForm(request.POST or None, initial={'user': request.user.id, 'gender': 'F'})
        errors.append("您必須先填寫完整資料，才可以開始大買特買唷～")
        print ('PersonalInfo CREATED')
        first_flag = True
        adr_formset = None
        act_formset = None
        num_formset = None

    if request.method == "POST":
        if info_form.is_valid():
            instance = info_form.save(commit=False)
            if not first_flag:
                if adr_formset.is_valid() and act_formset.is_valid() and num_formset.is_valid():
                    try:
                        FORMSET = {
                            'address': adr_formset.cleaned_data,
                            'account': act_formset.cleaned_data,
                            'number': num_formset.cleaned_data,
                        }
                        # formset_list = [
                        #     [f[k] if k in f.keys() else None for f in v] for k, v in FORMSET.items()
                        # ]
                        # adr_list, act_list, num_list = formset_list
                        adr_list = [item['address'] if 'address' in item else None for item in FORMSET['address']]
                        act_list = [item['account'] if 'account' in item else None for item in FORMSET['account']]
                        num_list = [item['number'] if 'number' in item else None for item in FORMSET['number']]
                        formset_list = [adr_list, act_list, num_list]
                        info_adr = Addresses.objects.filter(personalinfo_id=request.user.personalinfo.id)
                        info_act = Accounts.objects.filter(personalinfo_id=request.user.personalinfo.id)
                        info_num = FamilyNumber.objects.filter(personalinfo_id=request.user.personalinfo.id)
                        formset_qs = [info_adr, info_act, info_num]
                        formsets = [adr_formset, act_formset, num_formset]

                        print (formset_list)
                        print (formset_qs)

                        for idx, qs in enumerate(formset_qs):
                            # If There is not any data in datebase.
                            if not qs.exists():
                                try:
                                    for item in formset_list[idx]:
                                        if item is not None:
                                            if idx == 0:
                                                adr = Addresses(personalinfo=instance, address=item)
                                                adr.save()
                                            elif idx == 1:
                                                act = Accounts(personalinfo=instance, account=item)
                                                act.save()
                                            elif idx == 2:
                                                num = FamilyNumber(personalinfo=instance, number=item)
                                                num.save()
                                            else:
                                                print ("Info Formset ERROR!!")
                                except:
                                    print ("Info Formset ADD ERRORR")
                            # If There is 1 or 2 queryset in database
                            else:
                                formsets[idx].save()
                            # elif qs.count() == 2:
                            #     formsets[idx].save()
                            # elif qs.count() == 1:
                            #     formsets[idx].save()
                            #     saved_qs = formset_qs[idx][0]
                            #     formset_list[idx].remove(str(saved_qs))
                            #     data = formset_list[idx][0]
                            #     if data is not None and data != str(saved_qs):
                            #         print ('----')
                            #         if idx == 0:
                            #             print (formset_list[idx][0])
                            #         elif idx == 1:
                            #             print (formset_list[idx][0])
                            #         elif idx == 2:
                            #             print (formset_list[idx][0])
                    except KeyError:
                        print ("formset_list KeyError!!")
            instance.save()
            return redirect(reverse('member:page'))
    context = {
        'title': '資料編輯',
        'form': info_form,
        'adr_formset': adr_formset,
        'act_formset': act_formset,
        'num_formset': num_formset,
        'errors': errors,
    }
    return render(request, 'members/member-info.html', context)


@login_required
def member_shoppinglist(request):
    errors = []
    order_list = None
    try:
        order_list = PurchaseOrder.objects.filter(buyer=request.user.personalinfo)
    except:
        pass
        # return redirect(reverse('member:info'))
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
def member_orderstatus(request, number=None, do=None, dt=None, account=None):
    errors = []
    try:
        order = get_object_or_404(PurchaseOrder, number=float(number))
        status = order.status
        if do is not None:
            try:
                print (do)
                if status == 'UPD' and do == 'PAD':
                    order.remittance_time = datetime.strptime(dt, "%Y-%m-%d %H:%M")
                    order.remittance_account = account
                    order.status = 'PAD'
                elif status == 'UPD' and do == 'ABN':
                    order.renounce_time = datetime.strptime(dt, "%Y-%m-%d %H:%M")
                    order.status = 'CFA'
                elif status == 'CFA' and do == 'CCA':
                    order.renounce_time = None
                    order.status = 'UPD'
                else:
                    errors.append('動作錯誤，請重新執行！')
            except:
                print ("EEERROR")
                pass
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
