# -*- coding: utf-8 -*-
from django.contrib import admin
from members.models import PersonalInfo
# Register your models here.

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    raw_id_fields = ['user']
    list_display = ['name', 'sexual', 'birthday', 'phone', 'email', 'accounts', 'money']
