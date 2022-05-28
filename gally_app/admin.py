from django.contrib import admin

# Register your models here.
from gally_app import models
class ImageAdmin(admin.ModelAdmin):
  list_display = ("id","img","categoryName","locationName","description")




admin.site.register(models.Location)
admin.site.register(models.Image,ImageAdmin)
admin.site.register(models.Category)
