import requests
import json
import os.path
import time


DEFAULT_CONFIG = {
    "weather_file": os.path.join(os.getcwd(), "weather.txt"),
    "api_url": "https://api.weather.yandex.ru/v2/informers?lat={lat}&lon={lon}&lang=ru_RU",
    "api_key": None,
    "latitude": 55.751238,
    "longitude": 37.627762,
    "text": "{condition}, {temp}°C (ощущается {feels_like}°C)",
    "weather_statuses": {
        "clear": "Ясно",
        "partly-cloudy": "Малооблачно",
        "cloudy": "Облачно с прояснениями",
        "overcast": "Пасмурно",
        "light-rain": "Небольшой дождь",
        "rain": "Дождь",
        "heavy-rain": "Сильный дождь",
        "showers": "Ливень",
        "wet-snow": "Дождь со снегом",
        "light-snow": "Небольшой снег",
        "snow": "Снег",
        "snow-showers": "Снегопад",
        "hail": "Град",
        "thunderstorm": "Гроза",
        "thunderstorm-with-rain": "Дождь с грозой",
        "thunderstorm-with-hail": "Гроза с градом"
    },
    "version": "1.0.4",
    "config_created_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
}


def get_weather_forecast(config):
    full_url = config.get('api_url').format(
        lat=config.get('latitude'),
        lon=config.get('longitude')
    )

    headers = {
        'X-Yandex-API-Key': config.get('api_key')
    }

    response = requests.get(full_url, headers=headers)

    return response.json()


def save_forecast_to_file(forecast, config):
    weather_statuses = config.get('weather_statuses')

    temp = forecast.get('fact').get('temp')
    feels_like = forecast.get('fact').get('feels_like')

    condition_code = forecast.get('fact').get('condition')
    condition = weather_statuses.get(condition_code, condition_code.replace('-', ' ').capitalize())

    filepath = config.get('weather_file')

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(config.get('text').format(condition=condition, temp=temp, feels_like=feels_like))


def read_config():
    with open(os.path.join(os.getcwd(), 'config.json'), 'r') as file:
        return json.load(file)


def save_config(config):
    with open(os.path.join(os.getcwd(), 'config.json'), 'w') as file:
        file.write(json.dumps(config, indent=1))
        return config


def main():
    try:
        config = read_config()
        if 'version' not in config:
            raise Warning('Config version not found.')
    except:
        config = save_config(DEFAULT_CONFIG)

    if not config.get('api_key'):
        raise Warning("Required Yandex Weather API key.")

    forecast = get_weather_forecast(config)

    save_forecast_to_file(forecast, config)


if __name__ == "__main__":
    main()
