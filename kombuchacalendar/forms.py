import datetime
from django import forms
from django.utils import timezone
from .models import Batch


class BrewBatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ['starter_type', 'tea_flavor', 'sweetener', 'date_brewed', 'description', 'name',]


