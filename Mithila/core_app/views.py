from django.shortcuts import render
from .models import MithilaModel

# Create your views here.
def core(request):
    mithila_items = MithilaModel.objects.all()
    return render(request, 'core_app/core.html', {'mithila_items': mithila_items})
