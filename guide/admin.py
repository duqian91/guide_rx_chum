from django.contrib import admin
from guide.models import Guide, Category, Tag


# Register your models here.
admin.site.register(Guide)
admin.site.register(Category)
admin.site.register(Tag)

