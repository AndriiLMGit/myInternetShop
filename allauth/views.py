from django.shortcuts import render

# Create your views here.
def accounts_profile(request):
    return render(request, 'profile/profile.html')
