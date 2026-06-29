"""
Now let's learn about functions with parameters!

Parameters let you pass information into functions, making them flexible and reusable.
Think of parameters like ingredients in a recipe - you can change them to get different results.

The example below shows how to use parameters in functions.
"""


def show_weather(city):
    print("Today's weather in", city, "is beautiful!")


# Call the function with different cities
show_weather("Houston")
show_weather("Austin")

"""
Notice how we can call the same function with different values? The parameter 'city'
acts like a variable inside the function, taking on whatever value we pass in.

Now let's practice creating functions with parameters!
"""

# Create a function called 'show_temperature' that takes a parameter called 'temp' and prints it
def show_temperature(temp):
    print("Today in Houston, the temperature today is ", temp)
# Call your function with the temperature 75
show_temperature(75)
# Create a function called 'show_city_weather' that takes two parameters: 'city' and 'condition'
def show_city_weather(city , condition):
    print(city , "is", condition , "today")
# and prints a message like "Houston is sunny today"
show_city_weather("Houston" , "Sunny")
# Call your function with "Dallas" and "cloudy"
show_city_weather("Dallas" , "cloudy")
# Create a function called 'show_forecast' that takes three parameters: 'city', 'high', and 'low'
# and prints a message like "Austin: High of 85, Low of 68"
def show_forecast(city , high , low):
    print(city , ":" , "High of " , high , "," , "Low of " , low )
# Call your function with your city and some temperatures
show_forecast("Houston" , 101 , 95)
