from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse


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


class Allnews(models.Model):
    title = models.CharField('Název', max_length=50, validators=[MinLengthValidator(35)])
    anons = models.CharField('Upoutávka', validators=[MinLengthValidator(35)], max_length=150)
    full_text = models.TextField('Článek')
    photo = models.ImageField('Fotografie', upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField('Datum vytvoření', auto_now_add=True)
    time_update = models. DateTimeField('Datum změny', auto_now=True)
    is_published = models.BooleanField('Vydání', default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Všechny novinky'
        verbose_name_plural = 'Novinky'
        ordering = ['-time_create', 'title']


class Category(models.Model):
    name = models.CharField('Kategorie', max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Všechny kategorie'
        verbose_name_plural = 'Kategorie'
        ordering = ['id']