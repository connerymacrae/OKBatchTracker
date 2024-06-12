import datetime
from django import forms
from django.utils import timezone
from .models import Batch


class BrewBatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ['date_brewed', 'name', 'description', 'starter_type']


