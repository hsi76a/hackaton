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
    # api request takes 4 parameters:
    # - longitude and latitude
    # - api key
    # -part, dit is welke deel-databases je wilt niet wilt raadplegen, denk daarbij aan houerly, 3 hoouerly, 5 day forcast, zie apidocs
    # https://openweathermap.org/api/one-call-api
    part = "minutely,hourly,daily"
    resp = requests.get(
        f"# https://api.openweathermap.org/data/2.5/onecall?lat={lattitude}&lon={longitude}&exclude={part}&units=metric&appid={config.ows_api_key}")
    resp_list = resp.json()

    if len(resp_list) == 0:
        return False
    return resp_list
