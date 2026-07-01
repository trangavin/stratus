# Chapter 5: Lists

## What are Lists?

A list is a collection of items stored in a single variable. Think of it like a shopping list or a to-do list - it's a way to group related items together. In Python, you can store multiple values in one list.

For example, instead of creating separate variables for each day's temperature:
```python
day1_temp = 75
day2_temp = 78
day3_temp = 72
```

You can store them all in one list:
```python
weekly_temps = [75, 78, 72, 80, 76, 74, 71]
```

## Creating Lists

Lists are created using square brackets `[]` with items separated by commas:

```python
temperatures = [75, 78, 72, 80, 76]
cities = ["Houston", "Austin", "Dallas", "San Antonio"]
weather_conditions = ["sunny", "cloudy", "rainy", "sunny", "partly cloudy"]
```

You can even create an empty list:
```python
forecast = []
```

## Accessing List Items

Each item in a list has a position called an **index**. Python starts counting from 0, not 1!

```python
cities = ["Houston", "Austin", "Dallas", "San Antonio", "Chicago"]

print(cities[0])  # Output: Houston (first item)
print(cities[1])  # Output: Austin (second item)
print(cities[3])  # Output: San Antonio (fourth item)
print(cities[4])
```

You can also access items from the end using negative indices:
```python
print(cities[-1])  # Output: San Antonio (last item)
print(cities[-2])  # Output: Dallas (second to last)
```

## Modifying Lists

You can change items in a list by accessing them by index:

```python
temperatures = [75, 78, 72, 80, 76]
temperatures[2] = 85  # Change the third temperature
print(temperatures)  # Output: [75, 78, 85, 80, 76]
```

## List Methods

Python provides useful methods to work with lists:

### append() - Add an item to the end
```python
temperatures = [75, 78, 72]
temperatures.append(80)
print(temperatures)  # Output: [75, 78, 72, 80]
```

### insert() - Add an item at a specific position
```python
cities = ["Houston", "Dallas"]
cities.insert(1, "Austin")  # Insert at index 1
print(cities)  # Output: ["Houston", "Austin", "Dallas"]
```

### remove() - Remove a specific item
```python
weather = ["sunny", "rainy", "cloudy"]
weather.remove("rainy")
print(weather)  # Output: ["sunny", "cloudy"]
```

### pop() - Remove an item by index (removes last item if no index given)
```python
temperatures = [75, 78, 72, 80]
removed_temp = temperatures.pop(1)  # Remove item at index 1
print(temperatures)  # Output: [75, 72, 80]
print(removed_temp)  # Output: 78
```

## List Length and Membership

Find out how many items are in a list using `len()`:

```python
temperatures = [75, 78, 72, 80, 76]
print(len(temperatures))  # Output: 5
```

Check if an item exists in a list using `in`:

```python
cities = ["Houston", "Austin", "Dallas"]

if "Austin" in cities:
    print("Austin is in the list!")

if "Seattle" not in cities:
    print("Seattle is not in the list!")
```

## Why Use Lists?

1. **Organization** - Group related data together instead of many separate variables
2. **Efficiency** - Manage multiple items with one variable name
3. **Flexibility** - Easily add, remove, or modify items
4. **Scalability** - Handle any number of items, from zero to thousands

Lists are essential for working with collections of data, whether it's weather forecasts, student names, or product prices. You'll use lists constantly in your programming journey!
