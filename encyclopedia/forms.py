from typing import Text
from typing_extensions import Required
from django import forms


class CreatePageForm(forms.Form):
    title = forms.CharField(max_length=25, required=True, label='Your Title', widget=forms.TextInput(
        attrs={'placeholder': 'Title'}),
        error_messages={
        "required": "title should not be empty",
        "max_length": "less Than 25 pleaase"
    })

    contentMd = forms.CharField(label='Your Content', required=True, widget=forms.Textarea(
        attrs={'placeholder': 'Makdown Language'}))
