from django import forms
from .models import Edificio, Salon, Salon_clasificacion

class EdificioCreateForm(forms.ModelForm):
    class Meta:
        model = Edificio
        fields = ('nombre',
                  'salones',
                  'niveles',
                  )


class EdificioUpdateForm(forms.ModelForm):
    class Meta:
        model = Edificio
        fields = ('nombre',
                  'salones',
                  'niveles',
                  'habilitado',
                  )



class SalonCreateForm(forms.ModelForm):
    class Meta:
        model = Salon
        fields = ('nombre',
                  'capacidad',
                  'edificio',
                  'salon_clasificacion',
                  )


class SalonUpdateForm (forms.ModelForm):
    class Meta:
        model = Salon
        fields = ('nombre',
                  'capacidad',
                  'edificio',
                  'salon_clasificacion',
                  'habilitado',
                  )


class SalonClasiCreateForm(forms.ModelForm):
    class Meta:
        model = Salon_clasificacion
        fields = ('nombre',
                  )

class SalonClasiUpdateForm(forms.ModelForm):
    class Meta:
        model = Salon_clasificacion
        fields = ('nombre',
                  'habilitado',
                  )