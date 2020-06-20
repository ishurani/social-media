from django.shortcuts import render

# Create your views here.

def profile(request):
    current_user = User.objects.filter(user=request.user).last()
    return render(request,'profile.html', {'current_user': current_user})

def verification(request):
    return render(request,'home.html')
