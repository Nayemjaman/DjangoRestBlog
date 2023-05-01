from django.contrib import admin
from .models import User, Member, Creator, Staff
# Register your models here.
admin.site.register(Member)
admin.site.register(Creator)
admin.site.register(Staff)




@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username","is_member","is_craeator","is_staff")
