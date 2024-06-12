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
        ('k', 'Kombucha'),
        ('j', 'Jun')
    )

    starter_type = models.CharField(max_length=1, default='k', choices=TYPE)
    archive = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'batches'

    def starter_type_verbose(self):
        return dict(Batch.TYPE)[self.starter_type]

    @property
    def date_brewed_display(self):
        return self.date_brewed.strftime(settings.UPDATED_DATE_FORMAT)

    def __str__(self):
        return f'{self.name}({self.get_starter_type_display()}):{self.date_brewed_display}'

    def get_absolute_url(self):
        return reverse('kombuchacalendar:batch_detail', kwargs={'pk': self.pk})
