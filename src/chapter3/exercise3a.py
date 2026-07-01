"""
Let's learn how to create and use functions!

Functions are like recipes - they contain instructions that you can use over and over.
Think of them as your own custom commands that you create in Python.

The example below shows how to create a simple function and call it.
"""

def show_weather():
    print("Todays weather is beutiful")
    print("85 degrees")


# Call the function
show_weather()
"""
Did you see how we defined the function with 'def' and then called it by using its name
with parentheses? Functions let you organize your code and avoid repeating yourself.

Now let's practice creating your own weather functions!
"""


# Create a function called 'show_temperature' that prints a temperature message
def show_temperature():
    print("85 degrees")
# Call your function to test it
show_temperature()
# Create a function called 'show_forecast' that prints tomorrow's expected weather
def show_forecast():
    print("maybe cloudy")
# Call your show_forecast function
show_forecast()
# Create a function called 'show_season' that prints what season it is and typical weather
def show_season():
    print("summer super hot")
# Call your show_season function
show_season()

def definition_cold():
    print("not hot")
definition_cold()
