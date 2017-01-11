from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Textarea, CheckboxSelectMultiple, SelectMultiple
from django.utils import timezone
from the_game.models import Question


class AnswerForm(forms.Form):
    player_answer = forms.CharField(
        label='Player answer',
        max_length=128,

        widget=forms.TextInput,
        required=True,
    )

class StageOneForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
