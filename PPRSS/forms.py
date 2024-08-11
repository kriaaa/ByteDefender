# forms.py
from django import forms
from .models import FileUpload

class PEFileForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['file']
