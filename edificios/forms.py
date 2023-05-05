from django import forms
from .models import *

class EdificioCreateForm(forms.ModelForm):
    class Meta:
        
        fields = ('nombre',
                  'salones',
                  'niveles',
                  'fecha_creacion',
                  'habilitado',
                  )
