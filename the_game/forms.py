from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Textarea, CheckboxSelectMultiple, SelectMultiple
from django.utils import timezone

class AnswerForm(forms.Form):
    player_answer = forms.CharField(
        label='Player aswer',
        max_length=128,

        widget=forms.TextInput,
        required=True,
    )

