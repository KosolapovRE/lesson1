city_weather = {"city" : "Москва", "temperature" : "20"}
print(city_weather)
print(city_weather["city"])
city_weather["temperature"] = int(city_weather["temperature"]) - 5
print(city_weather)
city_weather["country"] = "Россия"
city_weather["date"] = '27.05.2019'
city_weather.get("national", "russian")
print(city_weather)