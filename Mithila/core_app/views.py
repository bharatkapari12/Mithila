from django.shortcuts import render, get_object_or_404
from .models import MithilaModel

# Create your views here.
def core(request):
    mithila_items = MithilaModel.objects.all()
    return render(request, 'core_app/core.html', {'mithila_items': mithila_items})

def core_detail(request, core_id):
    mithila_detail = get_object_or_404(MithilaModel, id=core_id)
    return render(request, 'core_app/detail.html', {'mithila_detail': mithila_detail})