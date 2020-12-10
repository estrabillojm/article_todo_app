from django import forms
from . import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body','thumbnail']

        widgets = {
            'title' : forms.TextInput(attrs={
                "placeholder":"Enter Title",
                "minlength":"4",
            }),
            'body' : forms.Textarea(attrs={
                "data-rule":"required",
                "minlength":"2",
                "data-msg":"Please write something for me",
                "placeholder": "Message"
            })
        }