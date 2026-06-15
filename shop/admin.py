from django.contrib import admin
from .models import *

@admin.register(TopHeader)
class TopHeaderAdmin(admin.ModelAdmin):
    list_display = ('shift', 'email', 'phone')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_filter = ('id',)
    search_fields = ('name',)

@admin.register(CarDetails)
class CarDetailsAdmin(admin.ModelAdmin):
    list_display = ('carId', 'name', 'price', 'title')
    list_filter = ('carId',)
    search_fields = ('name',)



admin.site.register(Menu) 
admin.site.register(SubMenu) 
admin.site.register(Sub2Menu)
admin.site.register(HomeBanner)
admin.site.register(Service)
admin.site.register(Feature)
admin.site.register(CarDetailImage)
admin.site.register(CarImage)
admin.site.register(ChooseUs)
admin.site.register(Blog)
admin.site.register(BlogDetails)
admin.site.register(BlogImage)
admin.site.register(FooterSection)
admin.site.register(AccessToken)

# admin.site.register(TitleBanner)
# admin.site.register(TitleBanner2)