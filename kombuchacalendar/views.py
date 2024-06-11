from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Batch
from .forms import BrewBatchForm
from django.urls import reverse_lazy, reverse


# Create your views here.
def index(request):
    num_batches = Batch.objects.all().count

    context = {
        'num_batches': num_batches,
    }
    return render(request, 'index.html', context)


@login_required
def brew_batch(request):
    # form to create a new kombucha batch
    if request.method != 'POST':
        # no data submitted, creates blank form
        form = BrewBatchForm()
    else:
        # POST data submitted; process data
        form = BrewBatchForm(data=request.POST)
        if form.is_valid():
            brew = form.save(commit=False)
            brew.brewer = request.user
            brew.save()
            return redirect('kombuchacalendar:index')
    context = {'form': form}
    return render(request, 'kombuchacalendar/brew_batch.html', context)


class BatchListView(LoginRequiredMixin, generic.ListView):
    model = Batch


class BatchDetailView(LoginRequiredMixin, generic.DetailView):
    model = Batch