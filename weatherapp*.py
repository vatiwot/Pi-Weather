import requests

OPENWEATHER_API_KEY = '1085356b674bdaa8cc435af72ab1f110'


def get_weather(city_name):

    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OPENWEATHER_API_KEY}&units=metric"
    

    response = requests.get(weather_url)
    
    if response.status_code == 200:

        data = response.json()


        main = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']


        print(f"Weather in {city_name}:")
        print(f"Main: {main}")
        print(f"Description: {description}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
    else:
        print(f"Error fetching weather data for {city_name}. Status Code: {response.status_code}")


def main():
    while True:
        city_name = input("\nAdd meg a varos nevet! (or 'exit' to quit): ")
        if city_name.lower() == 'exit':
            print("Kilepes az appbol.")
            break
        else:
            get_weather(city_name)

if __name__ == "__main__":
    main()
