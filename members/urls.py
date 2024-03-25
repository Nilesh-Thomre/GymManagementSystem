from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('add/', views.add_member_profile, name='add_member_profile'),
    path('water-intake/', views.water_intake_calculator, name='water_intake'),
    path('member/edit/<int:pk>/', views.edit_member, name='edit_member'),
    path('member/delete/<int:pk>/', views.delete_member, name='delete_member'),
    
]
