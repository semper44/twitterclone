from pyexpat import model
from django.forms import ModelForm
from .models import Groupapp


class group_form(ModelForm):
    class Meta:
        model = Groupapp
        fields = ["name"]
