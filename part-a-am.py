# Part A — Concept Application

# 1. Using only loops (no built-in functions), implement:
# ○ Find the maximum and minimum element in a list
def find_max_min(nums):
    if not nums:
        return None, None
    
    max_val = nums[0]
    min_val = nums[0]
    
    for num in nums:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
            
    return max_val, min_val

example_list = [10, 5, 20, 15, 3]
max_v, min_v = find_max_min(example_list)
print(f"List: {example_list}\nMax: {max_v}, Min: {min_v}\n")

# ○ Count frequency of each element using a dictionary
def count_frequency(elements):
    freq_dict = {}
    for item in elements:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict

fruit_list = ["apple", "banana", "apple", "cherry", "banana", "apple"]
frequencies = count_frequency(fruit_list)
print(f"Frequencies: {frequencies}\n")


# 2. Using a while loop, implement:
# ○ Reverse a number (e.g., 123 → 321)
def reverse_number(num):
    rev = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp = temp // 10
    return rev

number = 1234
reversed_num = reverse_number(number)
print(f"Original: {number}, Reversed: {reversed_num}")

# ○ Check whether a number is a palindrome
def is_palindrome(num):
    return num == reverse_number(num)

print(f"Is 121 a palindrome? {is_palindrome(121)}")
print(f"Is 123 a palindrome? {is_palindrome(123)}\n")


# 3. Work with tuples and dictionaries:
# ○ Convert a list of tuples [(key, value)] into a dictionary without using built-in conversion
def list_to_dict(pairs):
    new_dict = {}
    for key, value in pairs:
        new_dict[key] = value
    return new_dict

tuple_list = [("name", "John"), ("age", 25), ("city", "New York")]
converted_dict = list_to_dict(tuple_list)
print(f"Converted Dict: {converted_dict}")

# ○ Find the key with the highest value in a dictionary using loops only
def find_highest_key(d):
    highest_key = None
    highest_val = -1 # Assuming positive numbers or small enough
    
    first = True
    for key in d:
        if first:
            highest_key = key
            highest_val = d[key]
            first = False
        else:
            if d[key] > highest_val:
                highest_val = d[key]
                highest_key = key
    return highest_key

scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
best_student = find_highest_key(scores)
print(f"Student with highest marks: {best_student}\n")


# 4. Implement a function using *args:
# ○ Accept multiple numbers and return their sum and average (without using sum())
def sum_and_avg(*args):
    total = 0
    count = 0
    for num in args:
        total += num
        count += 1
    
    avg = total / count if count > 0 else 0
    return total, avg

total, avg = sum_and_avg(10, 20, 30, 40)
print(f"Numbers: (10, 20, 30, 40)\nSum: {total}, Average: {avg}\n")


# 5. Implement a function using **kwargs:
# ○ Accept student names and marks
# ○ Return the student with highest marks
def find_top_student(**kwargs):
    top_student = None
    top_mark = -1
    
    first = True
    for name, mark in kwargs.items():
        if first:
            top_student = name
            top_mark = mark
            first = False
        else:
            if mark > top_mark:
                top_mark = mark
                top_student = name
    return top_student

top = find_top_student(Sam=88, Sara=95, Tom=72)
print(f"Top Student from kwargs: {top}")
