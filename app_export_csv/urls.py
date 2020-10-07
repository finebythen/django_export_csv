from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.Index, name="Index"),
    path('crispy_forms/', views.Crispy_Forms, name="Crispy_Forms"),
    path('forms_vanilla/', views.Vanilla_Forms, name="Vanilla_Forms"),
    path('forms_widget_tweaks/', views.Widget_Tweaks, name="Widget_Tweaks"),
    path('export_users_csv/', views.Export_Users_CSV, name="Export_Users_CSV"),
]
