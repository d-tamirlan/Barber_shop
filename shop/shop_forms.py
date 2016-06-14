from django import forms
from phonenumber_field import modelfields


class OrderForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"required": ""}))
    address = forms.CharField(widget=forms.TextInput(attrs={"required": ""}))
    tel_number = forms.CharField(min_length=11, max_length=11, widget=forms.TextInput(attrs={"required": ""}))


class RecordForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "ИМЯ", "required": ""}))
    tel_number = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Номер телефона", "required": ""}))
    time = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "ВРЕМЯ", "required": ""}))
    date = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "ДАТА", "required": ""}))