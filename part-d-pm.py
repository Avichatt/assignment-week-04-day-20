# Part D — AI-Augmented Task

# 1. Prompt AI:
# "Explain normal distribution, Z-score, and hypothesis testing with a simple Python example."

# 2. Document prompt and output
# --- [AI-Generated Output] ---
# Normal Distribution: A bell-shaped curve where most data points are centered around the mean.
# Z-Score: A value that tells you how many standard deviations a point is away from the mean.
# Hypothesis Testing: A statistical method to check if our findings about samples are true for the whole population.

# Simple Python Example:
# import random

# data = [random.gauss(50, 10) for _ in range(100)]
# mean = sum(data) / 100
# std = (sum((x - mean)**2 for x in data) / 100) ** 0.5

# # Z-Score for a new value 60
# z = (60 - mean) / std
# print(f"Z-Score for value 60: {z}")

# # Basic Hypothesis Test (Checking if mean is 50)
# if abs(mean - 50) < 1.96 * (std / 10):
#     print("H0 (Mean is 50): Fail to reject.")
# else:
#     print("H0 (Mean is 50): Reject.")
# --- [End of AI Output] ---


# 3. Evaluate:

# ○ Is the explanation correct?
# Yes, it correctly defines all three concepts in simple terms for beginners.
# The bell-curve description for normal distribution and distance from mean for Z-score are standard.

# ○ Is the code logically correct and runnable?
# Let's test the AI implementation:
import random
data = [random.gauss(50, 10) for _ in range(100)]
mean = sum(data) / 100
std = (sum((x - mean)**2 for x in data) / 100) ** 0.5
z = (60 - mean) / std
print(f"Testing AI-suggested code: Z-Score for 60 is {z:.2f}")

# Evaluation: The code is logically correct. It calculates the mean, standard deviation, and a Z-score for the value 60.
# The hypothesis test logic uses the appropriate standard error (std/sqrt(n)) and z-critical value (1.96 for 95% confidence).
# One minor note: The sample size is 100, and sqrt(100) is 10, so the 1.96 * (std / 10) part is correct.
