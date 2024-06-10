from django.shortcuts import render, redirect
from .models import Batch


# Create your views here.
def index(request):
    num_batches = Batch.objects.all().count

    context = {
        'batches': num_batches,
    }
    return render(request, 'index.html', context)
