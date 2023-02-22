from .models import Userdata
from django import forms
class Form(forms.ModelForm):
    
    class Meta:
        model = Userdata
        fields = ("__all__")
