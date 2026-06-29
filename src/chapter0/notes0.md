# Chapter 0: Intro & Hello World

## About this course

- This is the first course for ACA students.
- Prerequisites: Basic computer & typing skills.

## What is Coding

Coding is creating instructions for computers using programming languages to solve problems.

## What are Programming Languages?

Programming languages, like human languages, are a way for us to communicate with computers. They have their own grammar and vocabulary.

## A Note on AI

Here are my opinions on AI, and my recommendation to all students of programming:

1. AI is here to stay, explore AI coding tools and find one that fits your needs
2. AI can be very beneficial to learning when used responsibly. Coding is primarily a practice & muscle-memory skill in the beginning. Do not substitute coding exercises with AI generated code.
3. AI writes excellent code at times, and terrible code at other times. Only your journey to improving your coding "sense" can help you differentiate.

## What is Python

Python is a popular programming language. It was created in 1991 by Guido van Rossum.

Python is a good first language because it's simple and easy to read. It's also highly marketable - used by Google, Facebook, and Netflix for web development, data analysis, AI, and more.

## What is VS Code?

VS Code (Visual Studio Code) is a popular code editor developed by Microsoft. It is an application that you can use to write and edit your code.

You'll need to be familiar with 3 parts:

1. The **Explorer**: A view that shows your project files and folders.
2. The **Editor**: Where you edit your code files.
3. The **Terminal**: Where you can tell your computer to run commands such as running your code.

## Comments

Comments are lines in your code that aren't executed. They're used to explain code or leave notes.

In Python, comments start with a `#` symbol.

## Docstrings

Docstrings are like multiline comments. That's all you need to know for now.

## Print

The classic first program in any language is to print "Hello, World!" to the screen. In Python, you can do this with the `print()` function. Try this out in `exercise0.py`.

## Functions

The `print()` you've been using is actually called a **function**. Functions are like verbs or actions that tell the computer what to do.

`print()` is a command that says "display this text on the screen" - the computer already knows how to do this.

### Arguments

The text inside the parentheses is called an **argument** - it's the input to the function.

```python
print("Hello World")
```

`"Hello World"` is the argument you're giving to the function.

### Calling Functions

To call a function, write its name followed by parentheses and its argument.

```python
print("Hello World")
```

You'll discover many other built-in functions as you learn. Later, you'll create your own!

## Quotes

You'll notice quotes inside the print function in exercises. Make sure to do this in your exercise. We'll cover this in Chapter 2.

## Commands

To run any Python file in your terminal, use this command pattern:

```
uv run python path/to/your/file.py
```

**Examples:**

- `uv run python src/chapter0/exercise0a.py`
- `uv run python src/chapter1/exercise1a.py`
- `uv run python answers/chapter0/answers0a.py`

**Note:** If unsure of your current location, type `pwd` to see where you are.
