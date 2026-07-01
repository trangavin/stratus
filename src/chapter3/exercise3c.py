"""
Now let's learn about functions that return values!

So far, our functions have printed results. But what if you want to use the result
in other calculations? That's where return values come in.

The example below shows how to return values from functions.
"""


def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


# Call the function and store the result
temp_celsius = convert_to_celsius(800)
print("75°F equals", temp_celsius, "°C")

"""
Notice how 'return' gives us back a value that we can store in a variable?
This is different from print - return lets us use the result later!

Now let's practice creating functions that return values!
"""

# Create a function called 'calculate_average' that takes two temperatures and returns their average
def calculate_average ( temperature1 , temperature2 ):
    average = ( temperature1 + temperature2 ) / 2
    return average


# Call your function with temperatures 75 and 85, store the result, and print it
average = calculate_average(3 , 5)
print("the average of temperature1 and temperature2 is " , average)
# Create a function called 'convert_to_fahrenheit' that takes celsius and returns fahrenheit
# Formula: (celsius * 9/5) + 32
def convert_to_farenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Test your function by converting 25°C to Fahrenheit and printing the result
fahrenheit = convert_to_farenheit(25)
print(fahrenheit)
fahrenheit = convert_to_farenheit(89)
print(fahrenheit)

def magic_function(favorite_number):
    return favorite_number * 100


result1 = magic_function(100)
result2 =magic_function(50)
print(result1)
print(result2)

