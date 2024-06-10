from django.shortcuts import render, redirect
from .models import Batch
from .forms import BrewBatchForm


# Create your views here.
def index(request):
    num_batches = Batch.objects.all().count

    context = {
        'num_batches': num_batches,
    }
    return render(request, 'index.html', context)


def brew_batch(request):
    # form to create a new kombucha batch
    if request.method != 'POST':
        # no data submitted, creates blank form
        form = BrewBatchForm()
    else:
        # POST data submitted; process data
        form = BrewBatchForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('kombuchacalendar:index')
    context = {'form': form}
    return render(request, 'kombuchacalendar/brew_batch.html', context)
