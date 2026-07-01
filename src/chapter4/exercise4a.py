"""
Let's learn how to make decisions in our code using simple if and else statements!
"""

# Below this line
print("-----")
friends_online = 1
print(friends_online==2)

print("-----")
# Here's an example of a simple if/else statement
temperature = 85

if temperature > 80:
    print("It's hot outside!")
else:
    print("It's not too hot today!")

"""
Notice how we used 'if' to check a condition, and 'else' as the alternative.
The code inside each block is indented, and only one block will run.

Now let's practice with weather-themed conditionals!
"""

# Example 1: Check if it's sunny
weather_condition = "cloudy"

# Create an if statement that checks if weather_condition equals "sunny" and prints "Wear sunglasses!"
if weather_condition=="sunny":
    print("wear sunglasses")
# Create an else statement that prints "No sunglasses needed!"
else:
    print("no sunglasses needed")
# Test your code by changing the weather_condition variable to different values like "sunny" or "cloudy"

# Example 2: Temperature check
current_temp = 2

# Create an if statement that checks if current_temp is greater than 70 and prints "Perfect weather!"
if current_temp > 70:
    print("perfect weather")
# Create an else statement that prints "A bit chilly today!"
else:
    print("A bit chilly today")
# Test your code by changing the current_temp variable to different values
