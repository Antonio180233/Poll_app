from.models import poll
from django import forms

class create_poll_form(forms.ModelForm):
    class Meta:
        model = poll
        fields = ['question', 'option_one', 'option_two', 'option_three']