from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView
from .views import SignUpView
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='members/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.member_list, name='member_list'),
    path('add/', views.add_member_profile, name='add_member_profile'),
    path('water-intake/', views.water_intake_calculator, name='water_intake'),
    path('member/edit/<int:pk>/', views.edit_member, name='edit_member'),
    path('member/delete/<int:pk>/', views.delete_member, name='delete_member'),
    path('homepage/', views.homepage, name='homepage'),
    path('calculate-body-fat/', views.calculate_body_fat, name='calculate_body_fat'),
    path('fitness-news/', views.get_fitness_news, name='fitness_news'),
    path('calorie_intake', views.calorie_intake_view, name='calorie_intake'),
]
