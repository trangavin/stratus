"""
Let's practice working with strings!

Strings are text wrapped in quotes. You can think of them like messages or labels.
You can combine strings together and create weather reports and messages.

The examples below show different ways to work with strings.
"""

# Create a variable called weather_condition and assign it a value of either "sunny" or "rainy"
weather_condition="sunny"
# Create another variable called city and assign it your city.
city="Houston"
# Using the variables you just created, print a message that says: "In Houston, it is rainy".
# Instead of "Houston" and "rainy", it should say whatever values you set your variables to.
print("In " + city + ", it is " + weather_condition)
# Now try making a third variable called temperature and assign it a value like "75 degrees".
temperature="75 degrees"
# Now use all 3 variables to print a custom message about the temperature and weather in your city.
print("In " + city + ", it is super " + weather_condition + ", because it is " + temperature + " outside.")
code1="In " + city + ", it is super " + weather_condition + ", because it is " + temperature + " outside."
print(code1 * 3)
