import random
import matplotlib.pyplot as plt

# Part B — Stretch Problem

# 1. Compare Normal Distribution vs Standard Normal Distribution:
# ○ Generate both distributions
normal_dist = [random.gauss(100, 15) for _ in range(1000)] # Mean=100, Std=15
standard_normal_dist = [random.gauss(0, 1) for _ in range(1000)] # Mean=0, Std=1

# ○ Plot and explain differences
# plt.hist(normal_dist, bins=30, alpha=0.5, label='Normal Dist (mean=100, std=15)')
# plt.hist(standard_normal_dist, bins=30, alpha=0.5, label='Standard Normal Dist (mean=0, std=1)')
# plt.legend()
# plt.title("Normal vs Standard Normal Distribution")
# plt.show() # Logic for plotting

print("Comparing Normal vs Standard Normal Distribution:")
print("1. Normal Distribution: Centered at its mean (e.g., 100) and spread by its std dev (e.g., 15).")
print("2. Standard Normal Distribution: Special case where mean is always 0 and std dev is always 1.\n")


# 2. Perform hypothesis testing on two groups:
# ○ Compute difference in means
group_a = [random.gauss(75, 10) for _ in range(50)]
group_b = [random.gauss(80, 10) for _ in range(50)]

def mean(data):
    return sum(data) / len(data)

mean_a = mean(group_a)
mean_b = mean(group_b)
diff = mean_b - mean_a

# ○ Interpret results (basic comparison)
print("Difference in means for Group A and Group B:")
print(f"Mean Group A: {mean_a:.2f}, Mean Group B: {mean_b:.2f}")
print(f"Difference (B - A): {diff:.2f}")
if abs(diff) > 2: # Basic heuristic for comparison
    print("Interpretation: There seems to be a notable difference between group means.")
else:
    print("Interpretation: The difference is small and might be due to chance.\n")


# 3. Explain:
# ○ When should you standardize data?
# Answer: You should standardize when features in your dataset have different scales (e.g., Weight in kg vs Height in cm or Age vs Salary).
# Standardization puts them on the same scale (mean=0, std=1), making them comparable.

# ○ Why Z-score is important in machine learning?
# Answer:
# 1. Prevents features with larger scales from dominating those with smaller ones.
# 2. Helps gradient descent converge faster by creating a more 'even' surface.
# 3. Many algorithms (like SVM or k-Nearest Neighbors) rely on distance between points, so scaling is crucial.
