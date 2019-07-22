from django.contrib import admin
from .models import order,OrderItem

# Register your models here.
class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display  = ('id','first_name','last_name','email','address','city','region',)
    list_filter   = ('paid','created','updated')
    search_fields = ['first_name','last_name','email']
    inlines = [
    OrderItemAdmin
    ]

admin.site.register(order,OrderAdmin)        