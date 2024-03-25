from django.contrib import admin
from .models import Member, MemberProfile

# Register both your models here
admin.site.register(Member)
admin.site.register(MemberProfile)
