from django.db import models
from django import forms

PLAYER_CHOICES = (
    (0, 'Administrator'),
    (1, 'Browar'),
    (2, 'Dystrybutor'),
    (3, 'Hurtownik'),
    (4, 'Detalista'),
)

class Player(forms.Form):
    widget = forms.Select(choices=PLAYER_CHOICES)

class Game(models.Model):
    runda = models.FloatField() #runda
    mag_przed = models.FloatField() #magazyn_przed
    tow_odb = models.FloatField() #towar odebrany
    koszt_tow = models.FloatField() #koszt towaru
    tow_wys = models.FloatField() #towar wysłany
    dochod = models.FloatField() #dochód
    mag_po = models.FloatField() #magazyn po
    koszt_mag = models.FloatField() #koszt magazynowania
    otw_zam = models.FloatField() #otwarte zamówienie
    przy_zam = models.FloatField() #przyjęte zamówienie
    zreli_zam = models.FloatField() #zrealizowane zamówienie
    otw_zam_po = models.FloatField() #otwarte zamówienie po
    koszt_otw_zam = models.FloatField() #koszt otwartych zamówień
    budzet = models.FloatField() #budżet



