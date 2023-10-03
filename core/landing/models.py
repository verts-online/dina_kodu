import datetime

from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=255)
    name_est = models.CharField(max_length=255, blank=True ,null=True)
    desc = RichTextField(blank=True, null=True)
    # desc = models.TextField()
    desc_est = models.TextField(blank=True ,null=True)
    price = models.IntegerField()

    class Meta:
        verbose_name = "Ус луга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name

class CallDayRequest(models.Model):
    day_rus = models.CharField(max_length=16)
    day_est = models.CharField(max_length=16, blank=True ,null=True)

    class Meta:
        verbose_name = "Удобрный день для звонка"
        verbose_name_plural = "Удобные дни для звонков"

    def __str__(self):
        return self.day_rus


class CallTimeRequest(models.Model):
    time_rus = models.CharField(max_length=16)
    time_est = models.CharField(max_length=16, blank=True ,null=True)

    class Meta:
        verbose_name = "Удобное время для звонка"
        verbose_name_plural = "Удобное время для звонка"

    def __str__(self):
        return self.time_rus

class CallWayRequest(models.Model):
    way_rus = models.CharField(max_length=16)
    way_est = models.CharField(max_length=16, blank=True ,null=True)

    class Meta:
        verbose_name = "Способ связи"
        verbose_name_plural = "Способы связи"

    def __str__(self):
        return self.way_rus


class CallRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидание'),
        ('in_process', 'В работе'),
        ('declined', 'Отклонено'),
        ('completed', 'Завершено'),
    ]
    services = models.ManyToManyField('Service', related_name='services')
    day = models.ForeignKey(CallDayRequest, on_delete=models.SET_NULL, null=True)
    time = models.ForeignKey(CallTimeRequest, on_delete=models.SET_NULL, null=True)
    way = models.ForeignKey(CallWayRequest, on_delete=models.SET_NULL, null=True)
    contact = models.CharField(max_length=255)

    request_created = models.DateTimeField(auto_now=True)
    status = models.CharField(default='pending', choices=STATUS_CHOICES, max_length=32)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f'Заявка от {self.request_created}'

