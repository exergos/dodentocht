__author__ = 'Willem Lenaerts'

def dodentocht_algorithm():
    # 1. Alle tijd data voor alle deelnemers
    # model: dodentocht_tijd

    # Open dodentocht_tijd file.
    import csv
    with open("app_dodentocht/algorithms/data/dodentocht_tijd.csv" , "r") as f:

        # Specify delimiter for reader.
        d_tijd = list(csv.reader(f, delimiter=";"))
        # Manipulate data
        import datetime
        import pytz
        # Create localization
        brussels = pytz.timezone("Europe/Brussels")
        count = list()
        for i in range(len(d_tijd)-1):
            count.append(0)

        for i in range(len(d_tijd[0])):
            if d_tijd[0][i] != "Naam" and d_tijd[0][i] != "Rang" and d_tijd[0][i] != "Totaal":
                for j in range(len(d_tijd)-1):
                    # If no value ==> year = 2015 (better luck next time :) )
                    # Increment to make sure you can sort based on datetime's
                    if d_tijd[j+1][i] == "\xa0" or d_tijd[j+1][i] == "":
                        d_tijd[j+1][i] = brussels.localize(datetime.datetime.strptime(str(int("2015") + count[j]),"%Y"))
                        count[j] = count[j] + 1
                    else:
                        if i == 2: # start
                            d_tijd[j+1][i] = brussels.localize(datetime.datetime.strptime("09/09/2014 " + d_tijd[j+1][i],"%d/%m/%Y %H:%M"))
                        else:
                            d_tijd[j+1][i] = d_tijd[j+1][i-1] + datetime.timedelta(seconds=(brussels.localize(datetime.datetime.strptime("09/09/2014 " + d_tijd[j+1][i],"%d/%m/%Y %H:%M")) - d_tijd[j+1][i-1]).seconds)

    # 2. Alle snelheid data, voor alle deelnemers
    # model: dodentocht_snelheid

    # Open dodentocht_snelheid file.
    with open("app_dodentocht/algorithms/data/dodentocht_snelheid.csv" , "r") as f:

        # Specify delimiter for reader.
        d_snelheid = list(csv.reader(f, delimiter=";"))

    # 3. Snelheid gemiddelde per post
    # model: dodentocht_snelheid_avg
    with open("app_dodentocht/algorithms/data/dodentocht_snelheid_avg.csv" , "r") as f:
        # Specify delimiter for reader.
        d_snelheid_avg = list(csv.reader(f, delimiter=";"))

    # 4. Totaal gemiddelde
    # model: dodentocht_totaal_avg
    with open("app_dodentocht/algorithms/data/dodentocht_totaal_avg.csv" , "r") as f:
        # Specify delimiter for reader.
        d_totaal_avg = list(csv.reader(f, delimiter=";"))

    return list([d_tijd,d_snelheid,d_snelheid_avg,d_totaal_avg])