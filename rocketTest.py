import requests, datetime

nameCity = str(input("Veulliez entrer le nom d'une  ville: "))
dateOfToday = datetime.datetime.today().date()

api = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={nameCity}&appid=4c4d6818d534428052459f1ee5275af1&lang=fr&units=metric").json()

print(f"""
                ...Actuellement...

coordonnées:
    longitude: {api["coord"]["lon"]}
    latitude: {api["coord"]["lat"]}
    
Principal:
    degré: {api["main"]["temp"]}
    ressenti: {api["main"]["feels_like"]}
    MAX: {api["main"]["temp_max"]}
    MIN: {api["main"]["temp_min"]}
    
temps: {api["weather"][0]["description"]}
pression: {api["main"]["pressure"]}
humidité: {api["main"]["humidity"]}

vent:
    vitesse: {api["wind"]["speed"]}
    orientation: {api["wind"]["deg"]}
    

""")

api = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={api['coord']['lat']}&lon={api['coord']['lon']}&exclude=current,minutely,hourly,alerts&appid=5f1621b7117e51053803b885f7339239&lang=fr&units=metric").json()

for instance in api["daily"]:
    if datetime.date.fromtimestamp(instance["dt"]) == dateOfToday:
        title = "Aujourd'hui"
    else:
        title = datetime.date.fromtimestamp(instance["dt"])

    print(f"""
                    ...{title}...

    coordonnées:
        longitude: {api["lon"]}
        latitude: {api["lat"]}

    Principal:
        Chaleur:
            jour: {instance["temp"]["day"]}
            jour MAX: {instance["temp"]["max"]}
            jour MIN: {instance["temp"]["min"]}
            
            matin: {instance["temp"]["morn"]}
            soir: {instance["temp"]["eve"]}
            nuit: {instance["temp"]["night"]}
            
        Ressenti:
            jour: {instance["feels_like"]["day"]}
            nuit: {instance["feels_like"]["night"]}
            matin: {instance["feels_like"]["morn"]}
            soir: {instance["feels_like"]["eve"]}

    temps: {instance["weather"][0]["description"]}
    pression: {instance["pressure"]}
    humidité: {instance["humidity"]}

    vent:
        vitesse: {instance["wind_speed"]}
        orientation: {instance["wind_deg"]}
        rafale: {instance["wind_gust"]}
        
    chance de precipitation: {instance["pop"]*100}%
    UV MAX: {instance["uvi"]}
    nébulosité: {instance["clouds"]}
    
    
    """)

"""{
   "lat":48.8534,
   "lon":2.3488,
   "timezone":"Europe/Paris",
   "timezone_offset":7200,
   "daily":[
      {
         "dt":1618830000,
         "sunrise":1618807896,
         "sunset":1618858044,
         "moonrise":1618823700,
         "moonset":1618795140,
         "moon_phase":0.22,
         "temp":{
            "day":15.4,
            "min":6.08,
            "max":16.85,
            "night":12.71,
            "eve":16.46,
            "morn":6.08
         },
         "feels_like":{
            "day":14.01,
            "night":4.9,
            "eve":15.21,
            "morn":4.9
         },
         "pressure":1020,
         "humidity":39,
         "dew_point":1.53,
         "wind_speed":2.63,
         "wind_deg":352,
         "wind_gust":3.48,
         "weather":[
            {
               "id":800,
               "main":"Clear",
               "description":"ciel dégagé",
               "icon":"01d"
            }
         ],
         "clouds":5,
         "pop":0,
         "uvi":3.91
}}"""