from django import forms
from .models import FileModel

class IPSendingForm(forms.ModelForm):
    # ip = forms.GenericIPAddressField(required=False)
    class Meta:
        model = FileModel
        fields = ['name','log_file']