from.models import Givegift
from django.forms import ModelForm, TextInput, EmailInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Givegift
        fields = ['first_name_participant', 'last_name_participant', 'email_participant', 'messenger_participant']

        widgets = {
            "first_name_participant": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Vaše jméno'
            }),
            "last_name_participant": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Vaše příjmení'
            }),
            "email_participant": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Váš email'
            }),
            "messenger_participant": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Jakákoli sociální síť'
            })
        }
