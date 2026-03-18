# Part D — AI-Augmented Task

# 1. Prompt AI:
# "Explain Python dunder methods with examples for beginners and include a custom class implementation."

# 2. Document prompt and output
# --- [AI-Generated Output] ---
# Dunder methods (short for "Double UNDERscore") are special methods that start and end with two underscores, like `__init__` or `__str__`.
# They are often called "Magic Methods" because they allow you to define how your objects behave with built-in Python syntax.

# Basic Examples:
# - `__init__`: Initializes a new instance of a class.
# - `__str__`: Returns a string representation of the object when you call `print()`.
# - `__len__`: Returns the "length" of the object when you call `len()`.

# Custom Class Implementation:
# class Book:
#     def __init__(self, title, pages):
#         self.title = title
#         self.pages = pages
#
#     def __str__(self):
#         return f"'{self.title}' with {self.pages} pages"
#
#     def __len__(self):
#         return self.pages

# my_book = Book("Python for Beginners", 300)
# print(my_book)        # Uses __str__
# print(len(my_book))   # Uses __len__
# --- [End of AI Output] ---


# 3. Evaluate:

# ○ Are the examples correct?
# Yes, the examples of `__init__`, `__str__`, and `__len__` are correct and clearly explain their purpose for beginners.

# ○ Is the class implementation working?
# Let's test the AI implementation:
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' with {self.pages} pages"

    def __len__(self):
        return self.pages

my_book = Book("Python for Beginners", 300)
print(f"Testing AI-suggested class: {my_book}")
print(f"Length (pages): {len(my_book)}")

# Evaluation: The class works perfectly and returns the expected values.
# The explanation is clear and easy to understand for beginners.
