from django.contrib import admin
from .models import *


class OrdersAdmin(admin.ModelAdmin):
    list_display = ['user', 'created']


class OrdersConfigAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']


class SocialLinksAdmin(admin.ModelAdmin):
    list_display = ['tg_link', 'vk_link', 'inst_link', 'phone_number']


class OrderStatisticsAdmin(admin.ModelAdmin):
    list_display = ['sended', 'reviews', 'on_market']


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'starts', 'date']


admin.site.register(User)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(OrdersConfig, OrdersConfigAdmin)
admin.site.register(SocialLinks, SocialLinksAdmin)
admin.site.register(OrderStatistics, OrderStatisticsAdmin)
admin.site.register(Reviews, ReviewsAdmin)

