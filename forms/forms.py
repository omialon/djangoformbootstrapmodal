from django import forms


class FormExemple(forms.Form):
    title = forms.CharField(label='Title', max_length=60, required=True)
