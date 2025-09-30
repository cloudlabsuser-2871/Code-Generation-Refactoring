import requests

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp_c = data['main']['temp']
        temp_f = temp_c * 9/5 + 32
        humidity = data['main']['humidity']
        condition = data['weather'][0]['description']
        print(f"Weather in {city}:")
        print(f"Temperature: {temp_f:.1f}°F")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition}")
    else:
        print(f"Failed to get weather data for {city}. Error: {response.status_code}")

def main():
    api_key = "63222fb2880747a530f26312a8d11f93"
    city = input("☁️ Enter city name: ")
    get_weather(city, api_key)

if __name__ == "__main__":
    main()
