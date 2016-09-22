from django import forms


class RestSearchForm(forms.Form):
    location = forms.CharField(max_length=1000)
