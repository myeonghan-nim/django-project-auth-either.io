from django import forms

from .models import Question, Choice


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'


class ChoiceForm(forms.ModelForm):
    choices = [(1, 'Left'), (2, 'Right'), ]
    pick = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)

    class Meta:
        model = Choice
        fields = ('pick', 'comment', )
