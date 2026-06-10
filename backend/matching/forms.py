from django import forms
from .models import OffreMentorat


class OffreMentoratForm(forms.ModelForm):
    class Meta:
        model = OffreMentorat
        fields = ['competence', 'type_offre', 'format']
        widgets = {
            'competence': forms.Select(attrs={'class': 'form-control-mentor'}),
            'type_offre': forms.Select(attrs={'class': 'form-control-mentor'}),
            'format': forms.Select(attrs={'class': 'form-control-mentor'}),
        }
