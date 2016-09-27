from django import forms


class RestSearchForm(forms.Form):
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Location'}))
    #location = forms.CharField(max_length=500)
