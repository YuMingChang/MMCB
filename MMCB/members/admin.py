from django.contrib import admin
from members.models import PersonalInfo, Addresses, Accounts, FamilyNumber


@admin.register(Addresses)
class AddressesAdmin(admin.ModelAdmin):
    raw_id_fields = ['personalinfo']
    list_display = ['personalinfo', 'address', ]


class AddressesInline(admin.TabularInline):
    model = Addresses
    extra = 1


@admin.register(Accounts)
class AccountsAdmin(admin.ModelAdmin):
    raw_id_fields = ['personalinfo']
    list_display = ['personalinfo', 'account', ]


class AccountsInline(admin.TabularInline):
    model = Accounts
    extra = 1


@admin.register(FamilyNumber)
class FamilyNumberAdmin(admin.ModelAdmin):
    raw_id_fields = ['personalinfo']
    list_display = ['personalinfo', 'number', ]


class FamilyNumberInline(admin.TabularInline):
    model = FamilyNumber
    extra = 1


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    raw_id_fields = ['user']
    list_display = [
        'name',
        'gender',
        'birthday',
        'phone',
        'email',
        'money',
    ]
    ordering = ('-id', )
    inlines = [AddressesInline, AccountsInline, FamilyNumberInline]
