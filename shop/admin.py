from django.contrib import admin
from .models import catag, products


# Register your models here.
class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(catag, catadmin)


class prodAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','img','available']
    list_editable = ['price','stock','img','available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(products, prodAdmin)
