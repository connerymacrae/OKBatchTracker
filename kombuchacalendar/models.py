from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Batch(models.Model):
    brewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(help_text="Tea Type, Sweetener Added, Batch Size, SCOBY Origin, etc. ")
    date_brewed = models.DateField(default=timezone.now)

    TYPE = (
        ("k", 'Kombucha'),
        ('j', 'Jun')
    )

    starter_type = models.CharField(max_length=1, default='k', choices=TYPE)

    class Meta:
        verbose_name_plural = 'batches'

    def __str__(self):
        return f'{self.name}({self.starter_type})-{self.date_brewed}'

    def get_absolute_url(self):
        #namespace
        return reverse('batch-detail', kwargs={'pk': self.pk})