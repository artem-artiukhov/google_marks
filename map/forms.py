from django import forms

class IPSendingForm(forms.Form):
    # ip = forms.GenericIPAddressField(required=False)
    file_field = forms.FileField(required=True)