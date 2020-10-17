from django import forms
from .models import FileUplad


def validate_file_extension(value):
    if not value.name.endswith('.csv'):
        raise forms.ValidationError("Only CSV file is accepted")


class FileUpladForm(forms.ModelForm):
    fiels_uploads = forms.FileField(label='Select a file',validators=[validate_file_extension])
    
    class Meta:
        model = FileUplad
        fields = ("fiels_uploads",)