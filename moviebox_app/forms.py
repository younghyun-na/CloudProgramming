from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label='Search Movie', max_length=50)
