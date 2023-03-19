import requests


class WeatherService:
    def __init__(self, url):
        self.__url = url

    def __get_key_for_url(self, key):
        if key in self.__url:
            return self.__url[key]

    def get_url_template(self):
        return self.__get_key_for_url("template")

    def get_url_params(self):
        return self.__get_key_for_url("payload")

    def get_weather(self, city):
        # явно преобразуем в string. чтобы убрать сообщение об ошибке
        url_weather = str(self.get_url_template()).format(city)

        response = requests.get(url_weather, self.get_url_params())
        response.raise_for_status()
        return response.text

url = {
    "template": "https://wttr.in/{}",
    # см. https://wttr.in/help
    "payload": {"T": "", "lang": "ru", "M": "", "n": "", "q": ""}
}

cities = ['London', 'svo', 'Череповец']
weather = WeatherService(url)

print(*[weather.get_weather(city) for city in cities])