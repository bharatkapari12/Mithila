from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'web/index.html')

def about(request):
    return render(request, 'web/about.html')

# def core(request):
#     return render(request, 'core_app/core.hmtl')
