weather_c = eval(input())
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = {day: (WeatherC * 9 / 5 + 32) for (day, WeatherC) in weather_c.items()}


print(weather_f)
