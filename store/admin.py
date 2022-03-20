from django.contrib import admin

from store.models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'price', 'stock', 'category',
                    'modified_date', 'is_available')


admin.site.register(Product, ProductAdmin)
