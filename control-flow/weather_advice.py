weather_status = input("What's the weather like today? (sunny/rainy/cold): ")

if weather_status == "sunny":
    message = "Wear a t-shirt and sunglasses."
elif weather_status == "rainy":
    message = "Don't forget your umbrella and a raincoat."
elif weather_status == "cold":
    message = "Make sure to wear a warm coat and a scarf."
else:
    message = "Sorry, I don't have recommendations for this weather."

print(message)