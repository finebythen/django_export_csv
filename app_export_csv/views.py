from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv

from .models import Students
from .forms import Forms_Example_Form, Forms_Example_Form_Vanilla


# Create your views here.
def Index(request):
    context = {}

    return render(request, 'app_export_csv/index.html', context)


def Crispy_Forms(request):
    form = Forms_Example_Form()

    if request.method == 'POST':
        form = Forms_Example_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('Crispy_Forms')

    context = {'form': form}
    return render(request, 'app_export_csv/crispy_forms.html', context)


def Vanilla_Forms(request):
    form = Forms_Example_Form_Vanilla()

    if request.method == 'POST':
        form = Forms_Example_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('Vanilla_Forms')

    context = {'formset': form}
    return render(request, 'app_export_csv/forms_vanilla.html', context)


def Widget_Tweaks(request):
    form = Forms_Example_Form_Vanilla()

    if request.method == 'POST':
        form = Forms_Example_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('Vanilla_Forms')

    context = {'formset': form}
    return render(request, 'app_export_csv/forms_widget_tweaks.html', context)


def Export_Users_CSV(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachement; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['First name', 'Last name', 'E-Mail'])

    users = Students.objects.all().values_list('first_name', 'last_name', 'mail')
    for item in users:
        writer.writerow(item)

    return response
