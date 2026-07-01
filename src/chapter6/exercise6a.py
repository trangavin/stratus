"""
Let's learn about for loops - a way to repeat code for each item in a list!

In Chapter 5, you learned to create lists. Now you'll learn to process every item
in a list without writing repetitive code. Loops make your code shorter and more powerful!
"""

# Here's a list of temperatures for the week
weekly_temps = [75, 78, 72, 80, 76, 74, 71]

# Use a for loop to print each temperature
for temp in weekly_temps:
    print("Temperature:", temp)

"""
Notice how the loop automatically goes through each item in the list?
The variable 'temp' takes on each value, one at a time.

Now let's practice using for loops!
"""

# Create a list called 'cities' with at least 4 city names
cities = ["Houston" , "Austin" , "Chicago" , "Dallas"]
# Use a for loop to print each city
for city in cities:
    print(city)
# Create a list called 'weather_conditions' with 5 weather conditions

# Use a for loop to print each weather condition with a message like "Today's weather: sunny"

# Using the range() function, print the numbers 1 through 7 (representing days of the week)
for days in range(1, 8):
    print("Day" , days)
