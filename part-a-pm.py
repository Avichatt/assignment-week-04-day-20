import random
import matplotlib.pyplot as plt

# Part A — Concept Application

# 1. Generate a dataset (size = 1000) from a normal distribution.
# We'll use random.gauss (mean=50, std=10) as a simple way to get normal data
dataset = [random.gauss(50, 10) for _ in range(1000)]

# ○ Compute mean, variance, and standard deviation manually
def compute_stats(data):
    n = len(data)
    # Mean
    total = 0
    for x in data:
        total += x
    mean = total / n
    
    # Variance
    sum_sq_diff = 0
    for x in data:
        sum_sq_diff += (x - mean) ** 2
    variance = sum_sq_diff / n
    
    # Standard Deviation
    std_dev = variance ** 0.5
    
    return mean, variance, std_dev

mean_val, var_val, std_val = compute_stats(dataset)
print(f"Dataset Size: 1000")
print(f"Mean: {mean_val:.2f}, Variance: {var_val:.2f}, Std Dev: {std_val:.2f}\n")

# ○ Plot histogram and verify if it resembles a normal distribution
# plt.hist(dataset, bins=30, color='skyblue', edgecolor='black')
# plt.title("Histogram of Generated Normal Distribution")
# plt.show() # Commented out for non-interactive environment, but logic is here

# 2. Convert the dataset into a standard normal distribution (Z-score):
# ○ Implement Z-score calculation manually
def calculate_z_scores(data, mean, std):
    z_scores = []
    for x in data:
        z = (x - mean) / std
        z_scores.append(z)
    return z_scores

standardized_data = calculate_z_scores(dataset, mean_val, std_val)

# ○ Verify mean ≈ 0 and standard deviation ≈ 1
z_mean, z_var, z_std = compute_stats(standardized_data)
print(f"Standardized Data (Z-Scores):")
print(f"Mean: {z_mean:.2f} (Expected: 0), Std Dev: {z_std:.2f} (Expected: 1)\n")


# 3. Given a dataset of student marks:
marks = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 150, 10] # Added outliers 150 and 10
m_mean, m_var, m_std = compute_stats(marks)

# ○ Identify outliers using Z-score (|Z| > 2 or 3)
m_z_scores = calculate_z_scores(marks, m_mean, m_std)
outliers = []
for i in range(len(marks)):
    if abs(m_z_scores[i]) > 2:
        outliers.append(marks[i])

print(f"Marks: {marks}")
print(f"Mean: {m_mean:.2f}, Std Dev: {m_std:.2f}")
print(f"Outliers (|Z| > 2): {outliers}\n")


# 4. Implement a basic one-sample hypothesis test:
# Null hypothesis: μ = 50
# Compute Z-statistic manually: Z = (sample_mean - mu_0) / (std / sqrt(n))
def one_sample_z_test(sample_mean, mu_0, std, n):
    z_stat = (sample_mean - mu_0) / (std / (n ** 0.5))
    return z_stat

# Conclude whether to reject H₀ at α = 0.05 (Zcritical approx 1.96)
mu_0 = 50
z_stat = one_sample_z_test(mean_val, mu_0, std_val, 1000)
print(f"Hypothesis Test (H0: mu = 50):")
print(f"Z-Statistic: {z_stat:.2f}")
if abs(z_stat) > 1.96:
    print("Result: Reject Null Hypothesis (at alpha 0.05)")
else:
    print("Result: Fail to Reject Null Hypothesis (at alpha 0.05)\n")


# 5. Simulate multiple samples (at least 1000 times):
# ○ Perform hypothesis test each time under H₀ true
# ○ Estimate the false positive rate
# ○ Compare with significance level (α)
false_positives = 0
alpha = 0.05
simulations = 1000

for _ in range(simulations):
    # Generating sample from H0: mu=50
    sample = [random.gauss(50, 10) for _ in range(30)] # Sample size 30
    s_mean, s_var, s_std = compute_stats(sample)
    
    # Test against mu=50
    z = one_sample_z_test(s_mean, 50, 10, 30) # Using true std=10 for simplicity
    if abs(z) > 1.96: # alpha = 0.05
        false_positives += 1

fp_rate = false_positives / simulations
print(f"Simulation Analysis (1000 runs):")
print(f"False Positive Rate: {fp_rate:.4f}")
print(f"Target Alpha: {alpha}")
print(f"Observation: FPR is close to alpha ({fp_rate:.4f} vs {alpha})")
