from django import forms
from .models import *

class CustomeCreationEdificioForm(forms.ModelForm):
    class Meta:
        
        fields = ('nombre',
                  'salones',
                  'niveles',
                  'fecha_creacion',
                  'habilitado',
                  )
