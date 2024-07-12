from django.shortcuts import render

# Create your views here.
def authpanel(request):
    return render(request, 'auth.html')