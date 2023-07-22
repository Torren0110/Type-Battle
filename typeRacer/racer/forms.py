from django import forms
from .models import Passage
from .utils import checkEasy, checkMedium, checkHard

class AddPassageForm(forms.ModelForm):
    def clean(self):
        super().clean()

        difficulty = self.cleaned_data['difficulty']
        text = self.cleaned_data['text']

        if difficulty == 0 and not checkEasy(text):
            raise forms.ValidationError('Text is not easy(0) difficulty.')
        elif difficulty == 1 and not checkMedium(text):
            raise forms.ValidationError('Text is not medium(1) difficulty')
        elif difficulty == 2 and not checkHard(text):
            raise forms.ValidationError('Text is not hard(2) difficulty.')

    class Meta:
        model = Passage
        fields = ['title', 'text', 'difficulty']