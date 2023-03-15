import requests

def get_weather(url, params):
    response = requests.get(url, params)
    response.raise_for_status()
    
    return response


url = {
    "template" : "https://wttr.in/{}",
    "payload"  : {"T": "", "lang": "ru", "M": "", "n":"", "q":""}
}
#url_payload = {"T": "", "lang": "ru", "M": "", "n":"", "q":""}
#url["payload"] = {"T": "", "lang": "ru", "M": "", "n":"", "q":""}

cities = ['London', 'svo','Череповец']
for city in cities:
    url_weather = url["template"].format(city)    
    response_weather = get_weather(url_weather, url["payload"])

    #print(response_weather.url) #для контроля
    print(response_weather.text)



