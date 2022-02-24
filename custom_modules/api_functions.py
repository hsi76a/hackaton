import requests
import config

# https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}

# def get_random_cars_brand(brand):
#     brand_upper = brand.upper()
#     brand_modified = brand_upper.split(" ")
#     filters = ['merk', 'handelsbenaming', 'eerste_kleur']
#     filters_list = [f"{filters[key]}={value}"
#                     for key, value
#                     in enumerate(brand_modified)]

#     filters_str = "&".join(filters_list)
#     resp = requests.get(f'https://opendata.rdw.nl/resource/m9d7-ebf2.json?{filters_str}')
#     resp_list = resp.json()

#     if len(resp_list) == 0:
#         return False
#     return resp_list


def get_weer_op_locatie(lattitude, longitude):
    part = "minutely,hourly,daily"
    resp = requests.get(
        f"https://api.openweathermap.org/data/2.5/onecall?lat={lattitude}&lon={longitude}&exclude={part}&units=metric&appid={config.ows_api_key}")
    resp_list = resp.json()

    if len(resp_list) == 0:
        return False
    return resp_list


def get_verkeers_info(plaatsnaam):
    url = "https://api.rwsverkeersinfo.nl/api/weatheralerts/"
    response = requests.request("GET", url)
    list_weercode = response.json()
    list_weercode['results'][0]['code']

    url = "https://api.rwsverkeersinfo.nl/api/obstructions/"
    response = requests.request("GET", url)
    list_wegobstructie = response.json()
    items_wegobstructie = ['directionText', 'isCurrent',
                           'roadNumber', 'timeStart', 'timeEnd']
    wegobstuctie_weercode_list = []
    for item in list_wegobstructie['results']:
        if plaatsnaam in item["directionText"] and item["isCurrent"] == True:
            templist = []
            for item_nested in items_wegobstructie:
                try:
                    templist.append(item[item_nested])

                except KeyError:
                    continue
            templist.append(list_weercode['results'][0]['code'])
            wegobstuctie_weercode_list.append(templist)

    if len(wegobstuctie_weercode_list) == 0 and list_weercode['results'][0]['code'] >= "":
        boodschap = f"Geen afsluitingen, let op KNMI geeft weercode {list_weercode['results'][0]['code']} af !!!"
    elif len(wegobstuctie_weercode_list) == 0:
        boodschap = "Geen afsluitingen, of weercode"
    else:
        boodschap = ""
    return (boodschap, wegobstuctie_weercode_list)
