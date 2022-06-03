from .models import Note
from django.forms import ModelForm, TextInput, Textarea


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ["title", "text"]
        widgets = {
            "title": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Title",
                }
            ),
            "text": Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Description",
                }
            ),
        }
