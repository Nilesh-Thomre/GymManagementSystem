from django.contrib import admin
from .models import Member, MemberProfile

# Register both your models here
admin.site.register(Member)
admin.site.register(MemberProfile)
from .models import CustomUser  

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff') 

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)