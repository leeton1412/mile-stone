from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemsAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemsAdminInline,)

    readonly_fields = ('order_number', 'date', 'delivery_cost',
                        'order_total', 'grand_total',)

    fields = ('order_number', 'date', 'full_name', 'email', 'phone_number',
            'country', 'postcode', 'town_or_city', 'street_address1',
            'street_address2', 'county', 'delivery_cost', 'order_total',
            'grand_total',)

    list_display = ('order_number', 'date', 'full_name',
                    'delivery_cost', 'order_total',
                    'grand_total',)

    odering = ('-date', )


admin.site.register(Order, OrderAdmin)

