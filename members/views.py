from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
from .forms import MemberForm
from .forms import MemberProfileForm
from .models import MemberProfile
from .forms import WaterIntakeForm
from .forms import BodyFatForm
import requests
from django.conf import settings
from .forms import CalorieIntakeForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')  # Redirect to login URL after successful signup
    template_name = 'members/signup.html'

@login_required(login_url='login')
def member_list(request):
    # If you want to display MemberProfile instances
    member_profiles = MemberProfile.objects.all()
    return render(request, 'members/member_list.html', {'members': member_profiles})
@login_required(login_url='login')
def add_member_profile(request):
    if request.method == 'POST':
        form = MemberProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')  # Redirect to a URL where you list members or show success
    else:
        form = MemberProfileForm()
    
    return render(request, 'members/add_member_profile.html', {'form': form})
@login_required(login_url='login')
def water_intake_calculator(request):
    form = WaterIntakeForm(request.POST or None)
    recommended_water_intake = None
    
    if request.method == 'POST' and form.is_valid():
        weight = form.cleaned_data.get('weight')
        activity_level = form.cleaned_data.get('activity_level')
        climate = form.cleaned_data.get('climate')
        
        # API endpoint
        url = 'https://smvqlpky7g.execute-api.eu-west-1.amazonaws.com/test/helloworld?'
        
        # Query parameters
        params = {
            'weight': weight,
            'activity_level': activity_level,
            'climate': climate
        }
        
        # Make a request to the API
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            recommended_water_intake = data.get('recommended_water_intake_liters')
    
    return render(request, 'members/water_intake_calculator.html', {
        'form': form,
        'recommended_water_intake': recommended_water_intake
    })
@login_required(login_url='login')

def edit_member(request, pk):
    member = get_object_or_404(MemberProfile, pk=pk)
    if request.method == 'POST':
        form = MemberProfileForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberProfileForm(instance=member)
    return render(request, 'members/edit_member_profile.html', {'form': form})
@login_required(login_url='login')
def delete_member(request, pk):
    member = get_object_or_404(MemberProfile, pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('member_list')
    return render(request, 'members/confirm_delete.html', {'member': member})
@login_required(login_url='login')
   
def homepage(request):
    return render(request, 'members/homepage.html')
@login_required(login_url='login')
   
def calculate_body_fat(request):
    form = BodyFatForm(request.POST or None)
    context = {'form': form}
    
    if request.method == 'POST' and form.is_valid():
        # Extract data from form
        weight = form.cleaned_data['weight']
        height = form.cleaned_data['height']
        age = form.cleaned_data['age']
        gender = form.cleaned_data['gender']
        
        # Prepare API request
        api_url = 'https://fu8odvcjmd.execute-api.eu-west-1.amazonaws.com/getBodyFatCal'
        params = {'weight': weight, 'height': height, 'age': age, 'gender': gender}
        response = requests.get(api_url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            context['body_fat_percentage'] = data['BodyFatPercentage']
        else:
            context['error_message'] = 'There was an error processing your request.'
    
    return render(request, 'members/calculate_body_fat.html', context)
@login_required(login_url='login')

def get_fitness_news(request):
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': 'fitness',
        'apiKey': settings.NEWS_API_KEY,
    }
    response = requests.get(url, params=params)
    articles = response.json().get('articles', [])

    return render(request, 'members/fitness_news.html', {'articles': articles})    



@login_required(login_url='login')

def calorie_intake_view(request):
    form = CalorieIntakeForm(request.GET or None)
    context = {'form': form}
    
    if request.method == 'GET' and form.is_valid():
        # Extract data from form
        height = form.cleaned_data['height']
        weight = form.cleaned_data['weight']
        
        # Prepare API request
        api_url = 'http://calorieapi-env.eba-udbdxf3g.us-east-1.elasticbeanstalk.com/api/calorie_intake'
        params = {'height': height, 'weight': weight}
        response = requests.get(api_url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            context['calorie_intake'] = data.get('calorie_intake')
        else:
            context['error_message'] = 'There was an error processing your request.'
    
    return render(request, 'members/calorie_intake.html', context)
    
