import requests

def get_weather(city):
    # Form the URL to fetch data
    url = f"https://wttr.in/{city}?M"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.text.strip()
            
            # Check if the city is not found
            if "Unknown location" in weather_data:
                print(f"City '{city}' not found.")
            else:
                weather_data = "\n".join(weather_data.splitlines()[:-1])
                print("Weather forecast:\n")
                print(weather_data)
        else:
            print(f"Error fetching data: status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")

# Main program
if __name__ == "__main__":
    city = input("Enter the city name: ").strip()
    if city:
        get_weather(city)
    else:
        print("City name was not entered.")