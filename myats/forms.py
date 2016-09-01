from django import forms

class SearchIdForm(forms.Form):
    person_id = forms.IntegerField()
