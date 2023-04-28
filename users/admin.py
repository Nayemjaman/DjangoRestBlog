from django.contrib import admin
from .models import User, Member, Creator, Staff
# Register your models here.
admin.site.register(User)
admin.site.register(Member)
admin.site.register(Creator)
admin.site.register(Staff)