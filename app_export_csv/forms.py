from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import ModelForm

from .models import Forms_Example


class Forms_Example_Form(ModelForm):

    class Meta:
        model = Forms_Example
        fields = '__all__'

        widgets = {
            'list_two': forms.CheckboxSelectMultiple(),
        }


class Forms_Example_Form_Vanilla(ModelForm):

    class Meta:
        model = Forms_Example
        exclude = [
            'list_one',
            'list_two',
        ]


class Forms_Example_Form_Widget_Tweaks(ModelForm):

    class Meta:
        model = Forms_Example
        exclude = [
            'list_one',
            'list_two',
        ]
