# Chapter 4: Making Decisions with Conditionals

Conditionals allow your program to make decisions, choosing one path over another depending on, well, conditions. Just like you decide what to wear based on the weather, your programs can decide what to do based on different conditions.

## Booleans: True or False

Before we make decisions, we need to understand **booleans**. A boolean is a simple data type that can only be `True` or `False`. This is how you would set a variable to the two boolean values:

```python
is_sunny = True
is_raining = False
```

Think of booleans like yes/no questions: "Is it sunny?" - Yes (`True`) or No (`False`).

## Comparison Operators

To make decisions, we often compare using **comparison operators**:

```python
temperature = 75

temperature > 70    # True (75 is greater than 70)
temperature < 60    # False (75 is not less than 60)
temperature == 75   # True (75 equals 75)
temperature != 80   # True (75 does not equal 80)
temperature >= 75   # True (75 is greater than or equal to 75)
temperature <= 70   # False (75 is not less than or equal to 70)
```

It's funny to see two equal signs. In Python this is how we ask the question "Is this equal to that?" One equal sign is used for assigning values to a variable, as you'll recall from chapter 2.

## Making Decisions with if Statements

The `if` statement lets your program make decisions:

```python
temperature = 75

if temperature > 80:
    print("It's hot outside!")
```

Just like functions, the code inside the `if` statement must be indented. Python only runs this code when the condition is `True`.

## Adding More Options with elif

What if you want to check multiple conditions? Use `elif` (which means "else if"):

```python
temperature = 55

if temperature > 80:
    print("It's hot!")
elif temperature > 60:
    print("It's warm!")
elif temperature > 40:
    print("It's cool!")
```

Here, the code first checks if the temperature is greater than 80. If it is, it prints "It's hot!". If not, it checks if the temperature is greater than 60, and so on. So in the case that temperature is 65, this is the exact set of steps that our program follows:

1. Check if 65 > 80: No
2. Check if 65 > 60: Yes - print "It's warm!"

Python checks each condition in order and runs the first one that's `True`. If none of them are `True`, just like before, the program will simply move on.

## The Default Choice with else

Sometimes you want a default action when none of your conditions are met. Use `else`:

```python
weather = "cloudy"

if weather == "sunny":
    print("Wear sunglasses!")
elif weather == "rainy":
    print("Bring an umbrella!")
else:
    print("Check the weather again!")
```

## Logical Operators

You can combine conditions using **logical operators**:

- `and` - Both conditions must be True
- `or` - At least one condition must be True

```python
temperature = 75
humidity = 60

if temperature > 70 and humidity < 70:
    print("Perfect weather!")

if weather == "sunny" or weather == "partly cloudy":
    print("Good day for a picnic!")
```

## Why Use Conditionals?

Conditionals make your programs intelligent. You'll use them throughout your coding journey for all sorts of cool functionality.
