"""
Let's learn about lists - a way to store multiple items in a single variable!

Lists are like containers that hold multiple values. Think of them as a week's worth
of weather data stored together instead of in separate variables.

The example below shows how to create a list and access its items.
"""

# Here's a list of temperatures for a week
weekly_temperatures = [75, 78, 72, 80, 76, 74, 71]
print(weekly_temperatures)

# Access individual temperatures by their index (position)
# Remember: Python starts counting at 0!
print(weekly_temperatures[0])  # First temperature
print(weekly_temperatures[3])  # Fourth temperature

"""
Notice how we can access any item by its position using square brackets and an index?
The first item is at index 0, the second at index 1, and so on.

Now let's practice creating and accessing lists!
"""

# Create a list called 'cities' with at least 4 city names
cities = ["Houston" , "Austin" , "Dallas" , "New York City"]
# Print the entire cities list
print(cities)
# Print the first city in your list (index 0)
print(cities[0])
# Print the third city in your list (index 2)
print(cities[2])
# Create a list called 'weather_conditions' with at least 5 weather conditions like "sunny", "rainy", etc.
weather_conditions = ["sunny" , "rainy" , "cloudy" , "snowy" , "cold"]
# Print the weather_conditions list
print(weather_conditions)
# Print the last weather condition using a negative index (use -1)
print(weather_conditions [-1])
# Print the second to last weather condition
print(weather_conditions [-2])
# Create a list called 'high_temps' with 7 temperature values representing a week
high_temps = [13 , 32 , 73 , 24 , 95, 62, 57]
# Print the temperature for the first day (Monday)
print(high_temps [0])
# Print the temperature for the last day (Sunday)
print(high_temps [-1])
