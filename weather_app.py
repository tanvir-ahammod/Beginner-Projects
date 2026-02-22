import requests

API_KEY = "your_api_key_here"
# Note: You need to sign up at https://openweathermap.org/ to get a free API key and replace "your_api_key_here" with that key.

while True:
    city = input("Enter city (or type 'quit' to exit): ")
    if city.lower() == "quit":
        break

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        print(f"Weather in {city}: {temp}°C, {desc}")
    else:
        print("City not found.")