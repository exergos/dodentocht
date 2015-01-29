# This file will populate database
import os

def populate():
    # Remove previous data in table
    import django
    django.setup()

    # Remove previous data
    dodentocht_tijd.objects.all().delete()
    dodentocht_snelheid.objects.all().delete()
    dodentocht_snelheid_avg.objects.all().delete()
    dodentocht_totaal_avg.objects.all().delete()

    from app_dodentocht.algorithms.dodentocht_algorithm import dodentocht_algorithm
    d = dodentocht_algorithm()
    d_tijd = d[0]
    d_snelheid = d[1]
    d_snelheid_avg = d[2]
    d_totaal_avg = d[3]

    # Populate db with d_tijd
    d = dict()

    for i in range(len(d_tijd)-1):
        for j in range(len(d_tijd[0])):
            d[d_tijd[0][j]] = d_tijd[i+1][j]
        dodentocht_tijd.objects.create(**d)

    # Populate db with d_snelheid
    d = dict()

    for i in range(len(d_snelheid)-1):
        for j in range(len(d_snelheid[0])):
            d[d_snelheid[0][j]] = d_snelheid[i+1][j]
        dodentocht_snelheid.objects.create(**d)

    # Populate db with d_snelheid_avg
    d = dict()

    for i in range(len(d_snelheid_avg)-1):
        for j in range(len(d_snelheid_avg[0])):
            d[d_snelheid_avg[0][j]] = d_snelheid_avg[i+1][j]
        dodentocht_snelheid_avg.objects.create(**d)

    # Populate db with d_totaal_avg
    d = dict()

    for i in range(len(d_totaal_avg)-1):
        for j in range(len(d_totaal_avg[0])):
            d[d_totaal_avg[0][j]] = d_totaal_avg[i+1][j]
        dodentocht_totaal_avg.objects.create(**d)
        
# Start execution here!
if __name__ == '__main__':
    print("Starting dodentocht database population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dodentocht.settings')
    from app_dodentocht.models import dodentocht_tijd
    from app_dodentocht.models import dodentocht_snelheid
    from app_dodentocht.models import dodentocht_snelheid_avg
    from app_dodentocht.models import dodentocht_totaal_avg

    populate()