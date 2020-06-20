from django.shortcuts import render

# Create your views here.
def logout_view(request):
    """
    url: logout/
    name: logout
    """

    logout(request)
    return redirect('main:home')

def home(request):
    return render(request, 'home.html')
