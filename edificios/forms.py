from django import forms
from .models import Edificios

class CustomeCreationEdificioForm(forms.ModelForm):
    class Meta:
        model = Edificios
        fields = ('nombre',
                  
                  )
