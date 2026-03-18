# Part C — Interview Ready

# Q1 — What is the difference between normal distribution and standard normal distribution?
# Answer:
# Normal Distribution: Any bell-shaped curve characterized by any mean (mu) and standard deviation (sigma).
# Standard Normal Distribution: A specific normal distribution where the mean (mu) is 0 and the standard deviation (sigma) is 1.

# Q2 (Coding) — Implement a function:
# z_score(x, mean, std)
# ● Return standardized value
# ● Apply on a dataset
def z_score(x, mean, std):
    return (x - mean) / std

def apply_z_score_to_dataset(data):
    # Calculate dataset stats manually for beginner
    n = len(data)
    mean_val = sum(data) / n
    var_val = sum((x - mean_val) ** 2 for x in data) / n
    std_val = var_val ** 0.5
    
    z_scores = []
    for x in data:
        z = z_score(x, mean_val, std_val)
        z_scores.append(z)
    return z_scores

dataset = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list_of_z_scores = apply_z_score_to_dataset(dataset)
print(f"Original: {dataset}")
print(f"Z-Scores: {[round(z, 2) for z in list_of_z_scores]}\n")


# Q3 — What is hypothesis testing? Explain:
# Hypothesis testing is a statistical method used to make inferences about a population based on sample data.

# ● Null hypothesis (H0): The default assumption or "status quo" (e.g., no effect or no difference).
# ● Alternative hypothesis (Ha/H1): What we want to prove or evidence of a difference/effect.
# ● p-value: Probability of getting the observed results (or more extreme) IF the null hypothesis is true.
# ● Significance level (α): The threshold (usually 0.05) below which we reject the null hypothesis.

print("Hypothesis Testing Summary:")
print("H0: Default assumption")
print("H1: What we want to test/prove")
print("p-value < alpha: Reject Null Hypothesis")
