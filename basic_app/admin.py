from django.contrib import admin
from basic_app.models import Notice, ManageUser, Category
# Register your models here.
admin.site.register(ManageUser)
admin.site.register(Category)
admin.site.register(Notice)