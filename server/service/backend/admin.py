from django.contrib import admin

# Register your models here.
from .models.common import Feedback, Version, BankAccount


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    pass

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('platform', 'version', 'sha1sum', 'constraint', 'created',)
    list_filter = ('platform', 'version')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone', 'owner', 'created')
    list_filter = ('owner', 'created')
    list_select_related = True

#
# @admin.register(Country)
# class CountryAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Province)
# class ProvinceAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(City)
# class CityAdmin(admin.ModelAdmin):
#     """docstring for ProvinceAdmin"""
#     pass
