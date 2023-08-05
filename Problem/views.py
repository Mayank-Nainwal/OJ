from django.shortcuts import render , redirect
from django.contrib.auth import logout

# Create your views here.
def problem(request):
    return render(request , 'base2.html')

def logoutpage(request):
    logout(request)
    return redirect('login')
