from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Batch(models.Model):
    brewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, help_text="Give your batch a name if you want...")
    description = models.TextField(help_text="Batch Size, SCOBY Origin, etc. ")
    date_brewed = models.DateField(default=timezone.now)

    STARTER_TYPE = (
        ('k', 'Kombucha'),
        ('j', 'Jun')
    )

    starter_type = models.CharField(max_length=1, default='k', choices=STARTER_TYPE)

    TEA_FLAVORS = (
        ('bl', "Black Tea"),
        ('pg', "Pear Ginger Black Tea"),
        ('bb', "Blueberry Black Tea"),
        ('jg', "Jasmine Green Tea"),
        ('sg', "Strawberry Green Tea"),
        ('cg', "Coconut Green Tea"),
    )

    tea_flavor = models.CharField(max_length=2, default='bl', choices=TEA_FLAVORS)

    SWEETENER_USED = (
        ('h', 'Honey'),
        ('s', 'Sugar'),
    )

    sweetener = models.CharField(max_length=1, default='s', choices=SWEETENER_USED)

    archive = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'batches'

    def starter_type_verbose(self):
        return dict(Batch.STARTER_TYPE)[self.starter_type]

    @property
    def date_brewed_display(self):
        return self.date_brewed.strftime(settings.UPDATED_DATE_FORMAT)

    def __str__(self):
        return f'{self.name}({self.get_starter_type_display()}):{self.date_brewed_display}'

    def get_absolute_url(self):
        return reverse('kombuchacalendar:batch_detail', kwargs={'pk': self.pk})
