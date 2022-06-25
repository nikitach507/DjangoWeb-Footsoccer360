from.models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Název článku'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Upoutávka'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Datum publikace'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text článku'
            })
        }