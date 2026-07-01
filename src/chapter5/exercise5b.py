"""
Now let's learn how to modify lists using built-in methods!

Lists aren't just for storing data - you can add items, remove items, and change them.
This is useful for building up a forecast or updating weather data.
"""

# Start with a list of temperatures
forecast_temps = [72, 75, 78]
print("Starting forecast:", forecast_temps)

# Add a new temperature to the end using append()
forecast_temps.append(80)
print("After adding 80:", forecast_temps)

# Remove a specific temperature using remove()
forecast_temps.remove(72)
print("After removing 72:", forecast_temps)

# Check how many items are in the list using len()
print("Number of days in forecast:", len(forecast_temps))

# Check if a temperature is in the list using 'in'
if 78 in forecast_temps:
    print("78 degrees is in the forecast!")

"""
See how we can dynamically modify our lists? This is much more flexible than
creating separate variables for each piece of data.

Now let's practice modifying lists!
"""

# Create an empty list called 'weekly_forecast'
weekly_forcast = []
# Add the following temperatures to your list one by one using append(): 70, 73, 75, 77
weekly_forcast.append(70)
weekly_forcast.append(73)
weekly_forcast.append(75)
weekly_forcast.append(77)
# Print your weekly_forecast list
print(weekly_forcast)
# Add two more temperatures: 76 and 74
weekly_forcast.append(76)
weekly_forcast.append(74)
# Print the updated list
print(weekly_forcast)
# Print the length of your weekly_forecast list using len()
print(len(weekly_forcast))


# Create a list called 'rain_chances' with these values: [20, 40, 60, 30, 10]
rain_chances = [20, 40, 60, 30, 10]
# Print the number of days in the rain_chances list
print(len(rain_chances))
# Check if 60 is in the rain_chances list, if so print "High chance of rain this week!"
if 55 in rain_chances:
    print("High chance of rain this week!")
else:
    print("OK")
