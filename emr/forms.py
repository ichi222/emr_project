from django import forms
from .models import Treatment, MedicalImage

class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ['description']

class MedicalImageForm(forms.ModelForm):
    class Meta:
        model = MedicalImage
        fields = ['image', 'description']
