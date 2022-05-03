from tabnanny import check
from django import forms


class CreateNewList(forms.Form):
    name = forms.CharField(label='Name', max_length=225)
    check = forms.BooleanField(required=False)
