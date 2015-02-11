from django.shortcuts import render
# Create your views here.
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render

# Import models to use in website (database - site connection)

# Import forms
from app_dodentocht import forms

# Import models
from app_dodentocht.models import dodentocht_tijd
from app_dodentocht.models import dodentocht_snelheid
from app_dodentocht.models import dodentocht_snelheid_avg
from app_dodentocht.models import dodentocht_totaal_avg
from app_dodentocht.models import requests

# To make list of lists that are not copies of each other
from itertools import repeat

# To make Google Charts accept Decimal Data
import json
import decimal

# For datetime objects
import datetime
import pytz
# To make sure transition from Django to Template (javascript) is smooth
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

# Definition to make datetime python object JSON serializable
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, datetime.timedelta):
            return (datetime.datetime.min + obj).time().isoformat()
        else:
            return super(DateTimeEncoder, self).default(obj)

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            your_name = form.cleaned_data['your_name']


            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    # When first rendering the site, this is what is used
    else:
        form = forms.NameForm()


    # Get names from database to use autocomplete:

    your_name_db_namen = dodentocht_tijd.objects.all().values_list("Naam")
    names = list()
    for i in range(len(your_name_db_namen)):
        names.append(your_name_db_namen[i][0])

    return render(request, 'index.html', {'form': form, "names" : names})

def results(request):
    # create a form instance and populate it with data from the request:
    form = forms.NameForm(request.POST)

    # # check whether it's valid:
    # if request.is_ajax():
    #     #if  'Change comp' in request.POST:
    #     # Save it to requests
    #     ##########################################
    #     # Store requested participant in database
    #     # Create model to write to database:
    #     get_status = requests() #imported class from model
    #     # 1. IP Address
    #     x_forwarded_for = request.META.get('REMOTE_ADDR')
    #     if x_forwarded_for:
    #         ip_address = x_forwarded_for.split(',')[-1].strip()
    #     else:
    #         ip_address = request.META.get('REMOTE_ADDR')
    #     get_status.ip_address= ip_address
    #
    #     # 2. Date
    #     # Create localization
    #     brussels = pytz.timezone("Europe/Brussels")
    #     get_status.pub_date = brussels.localize(datetime.datetime.today()) #import datetime
    #
    #     # 3. Requested name
    #     comp_name = form['your_name']
    #     get_status.name_requested = comp_name
    #
    #     # 4. Comp or not?
    #     comp = 1
    #     get_status.comp = comp
    #
    #     # Save
    #     get_status.save()
    #     ###########################################
    #
    #     # Now compare with new request (instead of average)
    #     context_dict = dodentocht_query(form,ip_address,"compare")
    if form.is_valid():
        if "yourname" in request.POST:
            ##########################################
            # Store requested participant in database
            # Create model to write to database:
            get_status = requests() #imported class from model
            # 1. IP Address
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip_address = x_forwarded_for.split(',')[-1].strip()
            else:
                ip_address = request.META.get('REMOTE_ADDR')
            get_status.ip_address= ip_address

            # 2. Date
            # Create localization
            brussels = pytz.timezone("Europe/Brussels")
            get_status.pub_date = brussels.localize(datetime.datetime.today()) #import datetime

            # 3. Requested name
            your_name = form.cleaned_data['your_name']
            get_status.name_requested = your_name

            # 4. Comp or not?
            comp = 0
            get_status.comp = comp

            # Save
            get_status.save()
            ###########################################

            # Process request
            context_dict = dodentocht_query(form,ip_address,'average')

            # Get names from database to use autocomplete:
            your_name_db_namen = dodentocht_tijd.objects.all().values_list("Naam")
            names = list()
            for i in range(len(your_name_db_namen)):
                names.append(your_name_db_namen[i][0])

            # add names to context_dict
            context_dict["names"] =  names

            # create empty forms
            form_yourname = forms.NameForm(auto_id='id_%s_1')
            form_comp = forms.NameForm(auto_id='id_%s_2')

            # add form_comp to context_dict
            context_dict['form_yourname'] = form_yourname
            context_dict['form_comp'] = form_comp

            return render(request, 'results.html', context_dict)
        if request.POST.get('form_name') == "form_compare":
            #if  'Change comp' in request.POST:
            # Save it to requests
            ##########################################
            # Store requested participant in database
            # Create model to write to database:
            get_status = requests() #imported class from model
            # 1. IP Address
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip_address = x_forwarded_for.split(',')[-1].strip()
            else:
                ip_address = request.META.get('REMOTE_ADDR')
            get_status.ip_address= ip_address

            # 2. Date
            # Create localization
            brussels = pytz.timezone("Europe/Brussels")
            get_status.pub_date = brussels.localize(datetime.datetime.today()) #import datetime

            # 3. Requested name
            comp_name = form.cleaned_data['your_name']
            get_status.name_requested = comp_name

            # 4. Comp or not?
            comp = 1
            get_status.comp = comp

            # Save
            get_status.save()
            ###########################################

            # Now compare with new request (instead of average)
            context_dict = dodentocht_query(form,ip_address,"compare")
        if request.POST.get('form_name') == "form_your_name":
            # if 'Change yourname' in request.POST:
            # Save it to requests
            ##########################################
            # Store requested participant in database
            # Create model to write to database:
            get_status = requests() #imported class from model
            # 1. IP Address
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip_address = x_forwarded_for.split(',')[-1].strip()
            else:
                ip_address = request.META.get('REMOTE_ADDR')
            get_status.ip_address= ip_address

            # 2. Date
            # Create localization
            brussels = pytz.timezone("Europe/Brussels")
            get_status.pub_date = brussels.localize(datetime.datetime.today()) #import datetime

            # 3. Requested name
            comp_name = form.cleaned_data['your_name']
            get_status.name_requested = comp_name

            # 4. Comp or not?
            comp = 0
            get_status.comp = comp

            # Save
            get_status.save()
            ###########################################

            # Now compare with new request
            try:
                comp_name = requests.objects.filter(comp__exact=1).latest("pub_date").name_requested
                context_dict = dodentocht_query(form,ip_address,"compare")
            except requests.DoesNotExist:
                context_dict = dodentocht_query(form,ip_address,"average")

    return HttpResponse(json.dumps(context_dict), content_type = "application/json")

def dodentocht_query(form,ip_address, compare_string):
    if compare_string == 'average':
        # process the data in form.cleaned_data as required
        your_name = form.cleaned_data['your_name']

        # Lookup in database
        your_name_db_namen = dodentocht_tijd.objects.all().values_list("Naam")
        names = list()
        for i in range(len(your_name_db_namen)):
            names.append(your_name_db_namen[i][0])

        your_name_db_tijd = dodentocht_tijd.objects.filter(Naam=your_name)
        your_name_db_snelheid = dodentocht_snelheid.objects.filter(Naam=your_name)
        your_name_db_snelheid_comp = dodentocht_snelheid_avg.objects.all()
        your_name_db_km = dodentocht_totaal_avg.objects.filter(Data="Km")
        your_name_db_participants = dodentocht_totaal_avg.objects.filter(Data="In race")
        your_name_db_opgaves = dodentocht_totaal_avg.objects.filter(Data="Opgaves per post")
        your_name_db_inrace = dodentocht_totaal_avg.objects.filter(Data="In race")


        import pytz
        # Create localization
        brussels = pytz.timezone("Europe/Brussels")

        # Make output
        # Header: name and rank of participant, total number of participants, total number of participant who finished race
        names_selected = list()
        names_selected.append(your_name)
        names_selected.append("Gemiddeld")

        names_selected_position = list()
        names_selected_position.append(your_name_db_tijd.values()[0]["Rang"])
        names_selected_position.append(0)

        participants = list()
        participants.append(int(your_name_db_participants.values()[0]["Start"]))
        participants.append(int(your_name_db_participants.values()[0]["Aankomst"]))

        # Table: posts and time/speed
        posts = list()
        km = list()
        time = list()
        speed = list()
        speed_comp = list()
        opgaves = list()
        inrace = list()
        data_keys = list(your_name_db_tijd.values()[0])
        for key in data_keys:
            if type(your_name_db_tijd.values()[0][key]) is datetime.datetime:
                posts.append(key)
                km.append(round(your_name_db_km.values()[0][key],2))
                time.append(your_name_db_tijd.values()[0][key])
                speed.append(round(your_name_db_snelheid.values()[0][key],1))
                speed_comp.append(round(your_name_db_snelheid_comp.values()[0][key],1))
                opgaves.append(int(your_name_db_opgaves.values()[0][key]))
                inrace.append(int(your_name_db_inrace.values()[0][key]))

        # Sort based on datetimes
        time, speed, speed_comp, posts, km, opgaves, inrace = (list(t) for t in zip(*sorted(zip(time, speed, speed_comp, posts, km, opgaves, inrace))))

        # time_total & time_comp_total
        import math
        for i in range(15,0,-1):
            if time[i].month is 9:
                a = time[i] - time[0]
                hours = str(a.days*24 + math.floor(a.seconds/3600))
                minutes = str(int((a.seconds - math.floor(a.seconds/3600)*3600)/60))
                if len(minutes) == 1:
                    minutes = "0" + minutes
                time_total = hours + ":" + minutes
                speed_total = round(3600*(km[-1] - km[0])/(a.days*24*3600 + a.seconds),1)
                break

        # Round last entry in km (aankomst = 100 km) to int
        km[-1] = int(km[-1])

        # Verander Sint_Amands in Sint-Amands
        for i in range(len(posts)):
            if "_" in posts[i]:
                posts[i] = posts[i].replace("_","-")

        # Change datetimes to correct timezone and output format
        time_graph = list()
        time_graph_comp = list()
        time_comp = list()
        for i in range(len(time)):
            time_graph.append(time[i].astimezone(brussels))
            time[i] = time[i].astimezone(brussels).strftime("%H:%M")

            if i == 0:
                time_graph_comp.append(time_graph[i])

            else:
                time_graph_comp.append(time_graph_comp[i-1] + datetime.timedelta(seconds=int(((km[i]-km[i-1])/speed_comp[i])*3600)))
            time_comp.append(time_graph_comp[i].astimezone(brussels).strftime("%H:%M"))
        # time_graph = time

        time_comp_total = str(time_graph_comp[-1] - time_graph_comp[0])[:-3]
        b = time_graph_comp[-1] - time_graph_comp[0]
        speed_comp_total = round(3600*(km[-1] - km[0])/b.seconds,1)

        # JSON for communication between Server & Web App
        # Strings no prob (so no JSON necessary for posts (but use SAFE in template))
        # Compare speeds in radar chart
        names = json.dumps(names)
        names_selected = json.dumps(names_selected)
        names_selected_position = json.dumps(names_selected_position)
        participants = json.dumps(participants)
        posts = json.dumps(posts)
        speed = json.dumps(speed, cls=DecimalEncoder)
        speed_comp = json.dumps(speed_comp, cls=DecimalEncoder)
        time_graph = json.dumps(time_graph, cls=DateTimeEncoder)
        time_graph_comp = json.dumps(time_graph_comp, cls=DateTimeEncoder)
        time = json.dumps(time)
        time_comp = json.dumps(time_comp)
        km = json.dumps(km, cls=DecimalEncoder)
        time_total = json.dumps(time_total)
        speed_total = json.dumps(speed_total, cls=DecimalEncoder)
        time_comp_total = json.dumps(time_comp_total)
        speed_comp_total = json.dumps(speed_comp_total, cls=DecimalEncoder)
        opgaves = json.dumps(opgaves, cls=DecimalEncoder)
        inrace = json.dumps(inrace, cls=DecimalEncoder)

        context_dict = {'names' : names, "names_selected" : names_selected, "names_selected_position" : names_selected_position,
                        "participants" : participants, "posts" : posts, "speed" : speed, "speed_comp" : speed_comp,
                        'time_graph' : time_graph, 'time_graph_comp' : time_graph_comp, 'time' : time, "time_comp" : time_comp, "km" : km,
                        "time_total" : time_total, "time_comp_total" : time_comp_total, "speed_total" : speed_total, "speed_comp_total" : speed_comp_total, "opgaves" : opgaves, "inrace" : inrace}

    # If compare is not average, but another person
    else:
        if compare_string == "compare":
            # Retain data from initially requested person (=latest by that IP Address)
            your_name = requests.objects.filter(comp__exact=0).filter(ip_address__exact=ip_address).latest("pub_date").name_requested
            comp_name = requests.objects.filter(comp__exact=1).filter(ip_address__exact=ip_address).latest("pub_date").name_requested

            # Lookup in database
            your_name_db_namen = dodentocht_tijd.objects.all().values_list("Naam")
            names = list()
            for i in range(len(your_name_db_namen)):
                names.append(your_name_db_namen[i][0])

            your_name_db_tijd = dodentocht_tijd.objects.filter(Naam=your_name)
            your_name_db_snelheid = dodentocht_snelheid.objects.filter(Naam=your_name)
            your_name_db_km = dodentocht_totaal_avg.objects.filter(Data="Km")
            your_name_db_participants = dodentocht_totaal_avg.objects.filter(Data="In race")
            your_name_db_opgaves = dodentocht_totaal_avg.objects.filter(Data="Opgaves per post")
            your_name_db_inrace = dodentocht_totaal_avg.objects.filter(Data="In race")

            comp_name_db_tijd = dodentocht_tijd.objects.filter(Naam=comp_name)
            comp_name_db_snelheid = dodentocht_snelheid.objects.filter(Naam=comp_name)

            import pytz
            # Create localization
            brussels = pytz.timezone("Europe/Brussels")

            # Make output
            # Header: name and rank of participant, total number of participants, total number of participant who finished race
            names_selected = list()
            names_selected.append(your_name)
            names_selected.append(comp_name)

            names_selected_position = list()
            names_selected_position.append(your_name_db_tijd.values()[0]["Rang"])
            names_selected_position.append(comp_name_db_tijd.values()[0]["Rang"])

            participants = list()
            participants.append(int(your_name_db_participants.values()[0]["Start"]))
            participants.append(int(your_name_db_participants.values()[0]["Aankomst"]))

            # Table: posts and time/speed
            posts = list()
            km = list()
            time = list()
            time_comp = list()
            speed = list()
            speed_comp = list()
            opgaves = list()
            inrace = list()
            data_keys = list(your_name_db_tijd.values()[0])
            for key in data_keys:
                if type(your_name_db_tijd.values()[0][key]) is datetime.datetime:
                    posts.append(key)
                    km.append(round(your_name_db_km.values()[0][key],2))
                    time.append(your_name_db_tijd.values()[0][key])
                    time_comp.append(comp_name_db_tijd.values()[0][key])
                    speed.append(round(your_name_db_snelheid.values()[0][key],1))
                    speed_comp.append(round(comp_name_db_snelheid.values()[0][key],1))
                    opgaves.append(int(your_name_db_opgaves.values()[0][key]))
                    inrace.append(int(your_name_db_inrace.values()[0][key]))

            # Sort based on datetimes
            time, time_comp, speed, speed_comp, posts, km, opgaves, inrace = (list(t) for t in zip(*sorted(zip(time, time_comp, speed, speed_comp, posts, km, opgaves, inrace))))

            # time_total & time_comp_total
            import math
            for i in range(15,0,-1):
                if time[i].month is 9:
                    a = time[i] - time[0]
                    hours = str(a.days*24 + math.floor(a.seconds/3600))
                    minutes = str(int((a.seconds - math.floor(a.seconds/3600)*3600)/60))
                    if len(minutes) == 1:
                        minutes = "0" + minutes
                    time_total = hours + ":" + minutes
                    speed_total = round(3600*(km[-1] - km[0])/(a.days*24*3600 + a.seconds),1)
                    break

            for i in range(15,0,-1):
                if time_comp[i].month is 9:
                    b = time_comp[i] - time_comp[0]
                    hours = str(b.days*24 + math.floor(b.seconds/3600))
                    minutes = str(int((b.seconds - math.floor(b.seconds/3600)*3600)/60))
                    if len(minutes) == 1:
                        minutes = "0" + minutes
                    time_comp_total = hours + ":" + minutes
                    speed_comp_total = round(3600*(km[-1] - km[0])/(b.days*24*3600 + b.seconds),1)
                    break

            # Round last entry in km (aankomst = 100 km) to int
            km[-1] = int(km[-1])

            # Verander Sint_Amands in Sint-Amands
            for i in range(len(posts)):
                if "_" in posts[i]:
                    posts[i] = posts[i].replace("_","-")

            # Change datetimes to correct timezone and output format
            time_graph = list()
            time_graph_comp = list()
            for i in range(len(time)):
                time_graph.append(time[i].astimezone(brussels))
                time[i] = time[i].astimezone(brussels).strftime("%H:%M")

                time_graph_comp.append(time_comp[i].astimezone(brussels))
                time_comp[i] = time_comp[i].astimezone(brussels).strftime("%H:%M")

            # JSON for communication between Server & Web App
            # Strings no prob (so no JSON necessary for posts (but use SAFE in template))
            # Compare speeds in radar chart
            names = json.dumps(names)
            names_selected = json.dumps(names_selected)
            names_selected_position = json.dumps(names_selected_position)
            participants = json.dumps(participants)
            posts = json.dumps(posts)
            speed = json.dumps(speed, cls=DecimalEncoder)
            speed_comp = json.dumps(speed_comp, cls=DecimalEncoder)
            time_graph = json.dumps(time_graph, cls=DateTimeEncoder)
            time_graph_comp = json.dumps(time_graph_comp, cls=DateTimeEncoder)
            time = json.dumps(time)
            time_comp = json.dumps(time_comp)
            km = json.dumps(km, cls=DecimalEncoder)
            time_total = json.dumps(time_total)
            speed_total = json.dumps(speed_total, cls=DecimalEncoder)
            time_comp_total = json.dumps(time_comp_total)
            speed_comp_total = json.dumps(speed_comp_total, cls=DecimalEncoder)
            opgaves = json.dumps(opgaves)
            inrace = json.dumps(inrace)

            context_dict = {'names' : names, "names_selected" : names_selected, "names_selected_position" : names_selected_position,
                            "participants" : participants, "posts" : posts, "speed" : speed, "speed_comp" : speed_comp,
                            'time_graph' : time_graph, 'time_graph_comp' : time_graph_comp, 'time' : time, "time_comp" : time_comp, "km" : km,
                            "time_total" : time_total, "time_comp_total" : time_comp_total, "speed_total" : speed_total, "speed_comp_total" : speed_comp_total,
                            "opgaves" : opgaves, "inrace" : inrace}
    return context_dict