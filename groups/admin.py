from django.contrib import admin
from .models import Group,Groupmember
# Register your models here.

admin.site.register(Group)
admin.site.register(Groupmember)

class GroupmemberInline(admin.TabularInline):
    model = Groupmember
