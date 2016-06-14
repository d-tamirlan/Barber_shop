from django.contrib import admin
from shop import models
from my_cms import cms_models


class News_image_admin(admin.TabularInline):
    model = models.NewsImages
    extra = 3


class News_admin(admin.ModelAdmin):
    inlines = [News_image_admin]


admin.site.register(models.News)
admin.site.register(models.NewsImages)
admin.site.register(models.Order)
admin.site.register(models.Record)
admin.site.register(models.Product)
admin.site.register(models.ProductImages)
admin.site.register(models.PhotoGallery)

admin.site.register(cms_models.Navigation)
admin.site.register(cms_models.ContactInfo)
admin.site.register(cms_models.Description)
admin.site.register(cms_models.PriceTable)
admin.site.register(cms_models.ManufacturerList)
admin.site.register(cms_models.ProductGroup)
admin.site.register(cms_models.AboutUs)
# Register your models here.
