# Inputs for weather prediction
temperature = 30  # Example temperature in °C
humidity = 50      # Example humidity in %
wind_speed = 10    # Example wind speed in km/h

# Weather prediction formula
prediction = 0.5 * temperature**2 - 0.2 * humidity + 0.1 * wind_speed - 15

# Determine weather category
if prediction > 300:
    category = "Sunny"
elif 200 < prediction <= 300:
    category = "Cloudy"
elif 100 < prediction <= 200:
    category = "Rainy"
else:
    category = "Stormy"

# Output result
print(f"Prediction: {prediction:.2f}")
print(f"Weather Category: {category}")
