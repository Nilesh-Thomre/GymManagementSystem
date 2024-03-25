from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
from .forms import MemberForm
from .forms import MemberProfileForm
from .models import MemberProfile
from .forms import WaterIntakeForm
import requests
def member_list(request):
    # If you want to display MemberProfile instances
    member_profiles = MemberProfile.objects.all()
    return render(request, 'members/member_list.html', {'members': member_profiles})
def add_member_profile(request):
    if request.method == 'POST':
        form = MemberProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')  # Redirect to a URL where you list members or show success
    else:
        form = MemberProfileForm()
    
    return render(request, 'members/add_member_profile.html', {'form': form})
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

def delete_member(request, pk):
    member = get_object_or_404(MemberProfile, pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('member_list')
    return render(request, 'members/confirm_delete.html', {'member': member})