from django.db import models


class Articles(models.Model):
    title = models.CharField('Název', max_length=50)
    anons = models.CharField('Upoutávka', max_length=250)
    full_text = models.TextField('Článek')
    date = models.DateTimeField('Datum publikace')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Všechny novinky'
        verbose_name_plural = 'Novinky'


class Premierleague(models.Model):
    title = models.CharField('Název', max_length=50)
    anons = models.CharField('Upoutávka', max_length=250)
    full_text = models.TextField('Článek')
    date = models.DateTimeField('Datum publikace')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Všechny novinky PL'
        verbose_name_plural = 'Premier League'


class Laliga(models.Model):
    title = models.CharField('Název', max_length=50)
    anons = models.CharField('Upoutávka', max_length=250)
    full_text = models.TextField('Článek')
    date = models.DateTimeField('Datum publikace')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Všechny novinky PL'
        verbose_name_plural = 'La Liga'


class Seriaa(models.Model):
    title = models.CharField('Název', max_length=50)
    anons = models.CharField('Upoutávka', max_length=250)
    full_text = models.TextField('Článek')
    date = models.DateTimeField('Datum publikace')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Všechny novinky SA'
        verbose_name_plural = 'Seria A'

class Ligamistru(models.Model):
    title = models.CharField('Název', max_length=50)
    anons = models.CharField('Upoutávka', max_length=250)
    full_text = models.TextField('Článek')
    date = models.DateTimeField('Datum publikace')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Všechny novinky LM'
        verbose_name_plural = 'Liga mistrů'



my_choices = (
    ('one', 'Nákup'),
    ('two', 'Nájem'),
    ('three', 'Volný agent'),
)

class Newtransfers(models.Model):
    first_name_transfer = models.CharField('Jmeno', max_length=100)
    last_name_transfer = models.CharField('Příjmení', max_length=100)
    last_club = models.CharField('Poslední tým', max_length=100)
    current_club = models.CharField('Současný tým', max_length=100)
    price_transfer = models.IntegerField('Cena v dolarech')
    contract_type = models.CharField('Smluvní typ', max_length=250, choices=my_choices)
    contract_time = models.IntegerField('Smluvní doba v letech')

    def __str__(self):
        return self.last_name_transfer

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Všechny transfers'
        verbose_name_plural = 'Transfers'