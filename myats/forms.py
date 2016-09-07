from django import forms
from .models import Student

class SearchIdForm(forms.Form):
    person_id = forms.CharField()
    def clean(self):
        cleaned_data = super(SearchIdForm, self).clean()
        person_id = cleaned_data.get('person_id')
        if not Student.objects.filter(student_id=person_id).exists():
            raise forms.ValidationError('Invalid ID Number')
        return cleaned_data
