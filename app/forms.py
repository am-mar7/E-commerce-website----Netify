from django import forms
from .models import Contactor

class ContactForm (forms.ModelForm):
    class Meta:
        model = Contactor
        fields = [
            'name' ,
            'email' ,
            'message' ,
        ] 