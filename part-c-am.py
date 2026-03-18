# Part C — Interview Ready

Q1 — What is the difference between *args and **kwargs? When would you use each?
Answer:
*args (Non-Keyword Arguments):
- It allows a function to accept any number of positional arguments.
- It stores them in a tuple.
- Use it when you don't know in advance how many parameters the user might pass (e.g., a function to sum any number of items).

**kwargs (Keyword Arguments):
- It allows a function to accept any number of keyword-value pairs (like dict).
- It stores them in a dictionary.
- Use it when you want to handle named parameters that might vary (e.g., student records where some might have 'age', others 'address', etc.).


# Q2 (Coding) — Create a class Student:
# ● Attributes: name, marks
# ● Methods: ○ Calculate grade (A/B/C) ○ Display student details using __str__
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "Grade A"
        elif self.marks >= 75:
            return "Grade B"
        elif self.marks >= 50:
            return "Grade C"
        else:
            return "Fail"

    def __str__(self):
        return f"Student: {self.name}, Marks: {self.marks}, Grade: {self.calculate_grade()}"

# Test Student Class
s1 = Student("John Doe", 88)
s2 = Student("Jane Smith", 94)
s3 = Student("Bob White", 65)

print(s1)
print(s2)
print(s3)


Q3 — What are dunder methods in Python? Why are they important? Give 3 examples.
Answer:
Dunder (Double UNDERscore) methods, also called magic methods, are built-in Python methods that start and end with double underscores (e.g., __init__).
They are important because they allow us to define how our custom objects behave with standard Python operations (like +, -, print(), and len()).

Examples:
1. __init__(): Called when an object is created. Used to initialize attributes.
2. __str__(): Defines what is shown when we print() an object.
3. __add__(): Defines how two objects of a class should be added using '+' operator.
