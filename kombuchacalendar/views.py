from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import generic
from .models import Batch
from .forms import BrewBatchForm
from django.urls import reverse_lazy, reverse


# Create your views here.
def index(request):
    num_batches = Batch.objects.filter(archive=False).count

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
            return redirect('kombuchacalendar:batches')
    context = {'form': form}
    return render(request, 'kombuchacalendar/brew_batch.html', context)


class BatchListView(LoginRequiredMixin, generic.ListView):
    model = Batch
    template_name = 'kombuchacalendar/batch_list.html'

    def get_queryset(self):
        return Batch.objects.filter(brewer=self.request.user, archive=False)


class BatchDetailView(LoginRequiredMixin, generic.DetailView):
    model = Batch
    template_name = 'kombuchacalendar/batch_detail.html'


@login_required
def batch_update(request, batch_id):
    batch = Batch.objects.get(id=batch_id)

    if request.method != 'POST':
        # prefill form with current entry
        form = BrewBatchForm(instance=batch)
    else:
        # POST data submitted, process data
        form = BrewBatchForm(instance=batch, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('kombuchacalendar:batch_detail', pk=batch.id)

    context = {'form': form, 'batch': batch}
    return render(request, 'kombuchacalendar/batch_update.html', context)


@login_required
def batch_archive(request, batch_id):
    batch = Batch.objects.get(id=batch_id)

    if batch.archive is False:
        batch.archive = True
        batch.save()
        return redirect('kombuchacalendar:archive')


class ArchiveListView(LoginRequiredMixin, generic.ListView):
    model = Batch
    template_name = 'kombuchacalendar/archive_list.html'

    def get_queryset(self):
        return Batch.objects.filter(brewer=self.request.user, archive=True)


@login_required
def batch_unarchive(request, batch_id):
    batch = Batch.objects.get(id=batch_id)

    if batch.archive is True:
        batch.archive = False
        batch.save()
        return redirect('kombuchacalendar:batches')
