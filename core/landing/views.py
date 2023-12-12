from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

from .forms import *
from .models import *

def index(request):
    services = Service.objects.all()
    form = RequestCallForm()
    data = {"header": "Hello Django", "message": "Welcome to Python", 'services': services, 'form': form,
            'title': 'Организатор пространства - Vedana Kodu'}

    if request.method == 'POST':
        form = RequestCallForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Заявка отправлена!")
        print('kek')
    return render(request, "landing/index.html", context=data)
