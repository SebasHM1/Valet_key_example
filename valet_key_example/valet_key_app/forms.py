from django import forms

class RequestValetKeyForm(forms.Form):
    file_name = forms.CharField(label="Nombre del archivo", max_length=255)
