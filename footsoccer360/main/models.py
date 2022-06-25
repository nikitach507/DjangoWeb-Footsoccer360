from django.db import models


class Givegift(models.Model):
    first_name_participant = models.CharField('Vaše jméno', max_length=20)
    last_name_participant = models.CharField('Vaše příjmení', max_length=50)
    email_participant = models.EmailField('Váš email', max_length=50)
    messenger_participant = models.CharField('Jakákoli sociální síť', max_length=150)


    def __str__(self):
        return self.email_participant

    def get_absolute_url(self):
        return f'/main/{self.email_participant}'

    class Meta:
        verbose_name = 'Všechny formulaře'
        verbose_name_plural = 'Všechny e-mailové adresy pro dárek'

