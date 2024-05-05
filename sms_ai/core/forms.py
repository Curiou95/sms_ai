from django import forms
from .models import Sitter

class SitterForm(forms.ModelForm):
    class Meta:
        model = Sitter
        fields = ['name', 'location', 'date_of_birth', 'gender', 'next_of_kin', 'NIN', 'recommender_name', 'religion', 'education_level', 'sitter_number', 'contacts', 'active']
