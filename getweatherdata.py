from requests import get
import json

def get_weather_data(place, API_key=None):
    with get(
            f'https://api.openweathermap.org/data/2.5/weather?q={place}&units=metric&appid={API_key}'
    ) as f:
        res = f.text

        res_json = json.loads(res)

    res_json['timezone'] = f'UTC{res_json['timezone']/3600.0:+g}'

    res_json = {
        'name' : res_json['name'],
        'coord' : res_json['coord'],
        'country' : res_json['sys']['country'],
        'feels_like' : res_json['main']['feels_like'],
        'timezone' : res_json['timezone']
    }

    with open('data.json', 'w') as f:
        json.dump(res_json, f, ensure_ascii=False, indent=4)

    print(res_json)

