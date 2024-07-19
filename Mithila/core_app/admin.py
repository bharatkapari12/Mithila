from django.contrib import admin
from .models import MithilaModel, MithilaFood, MithilaLanguage, MithilaCertificate

# Register your models here.
class MithilaInline(admin.TabularInline):
    model = MithilaFood
    extra = 2

class MithilaAdmin(admin.ModelAdmin):
    list_display = ('place_name', 'region', 'date_added')
    inlines = [MithilaInline]

class MithilaLanguageAdmin(admin.ModelAdmin):
    list_display = ('language_name', 'language_origin')
    filter_horizontal = ('mithila_place',)

class MithilaCertificateAdmin(admin.ModelAdmin):
    list_display = ('mithila_certificate', 'certificate_no')

admin.site.register(MithilaModel)
admin.site.register(MithilaLanguage, MithilaLanguageAdmin)
admin.site.register(MithilaCertificate, MithilaCertificateAdmin)