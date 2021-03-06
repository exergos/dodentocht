from django.db import models

# Create your models here.

class dodentocht_tijd(models.Model):
    Rang = models.IntegerField(default=0)
    Naam = models.TextField(default='')
    Start = models.DateTimeField()
    Weert = models.DateTimeField()
    Bornem = models.DateTimeField()
    Wintam = models.DateTimeField()
    Ruisbroek = models.DateTimeField()
    Breendonk = models.DateTimeField()
    Steenhuffel = models.DateTimeField()
    Peizegem = models.DateTimeField()
    Buggenhout = models.DateTimeField()
    Opdorp = models.DateTimeField()
    Lippelo = models.DateTimeField()
    Puurs = models.DateTimeField()
    Oppuurs = models.DateTimeField()
    Sint_Amands = models.DateTimeField()
    Branst = models.DateTimeField()
    Aankomst = models.DateTimeField()
    Totaal = models.TextField(default='')

class dodentocht_snelheid(models.Model):
    Rang = models.IntegerField(default=0)
    Naam = models.TextField(default='')
    Start = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Weert = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Bornem = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Wintam = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Ruisbroek = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Breendonk = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Steenhuffel = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Peizegem = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Buggenhout = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Opdorp = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Lippelo = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Puurs = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Oppuurs = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Sint_Amands = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Branst = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Aankomst = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Totaal = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)

class dodentocht_snelheid_avg(models.Model):
    Start = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Weert = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Bornem = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Wintam = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Ruisbroek = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Breendonk = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Steenhuffel = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Peizegem = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Buggenhout = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Opdorp = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Lippelo = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Puurs = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Oppuurs = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Sint_Amands = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Branst = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Aankomst = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Totaal = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)

class dodentocht_totaal_avg(models.Model):
    Data = models.TextField(default='')
    Start = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Weert = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Bornem = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Wintam = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Ruisbroek = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Breendonk = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Steenhuffel = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Peizegem = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Buggenhout = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Opdorp = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Lippelo = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Puurs = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Oppuurs = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Sint_Amands = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Branst = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)
    Aankomst = models.DecimalField(max_digits= 30, decimal_places= 5,default=0)