import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# ---------- 1. Load ----------
df = pd.read_csv("heart.csv")
print(df.shape)
print(df.head())
cols = ["age", "chol", "trestbps", "thalach"]
print(df[cols].describe())

# ---------- 2. Distributions ----------
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
for ax, c in zip(axs.ravel(), cols):
    ax.hist(df[c], bins=20, edgecolor="black")
    ax.set_title(c)
plt.tight_layout()
plt.savefig("distributions.png", dpi=150)
plt.close()

# ---------- 3. Normality ----------
print("\n=== Normality ===")
for c in cols:
    w, p = stats.shapiro(df[c])
    print(f"{c:9s} Shapiro p = {p:.4g}, skew = {stats.skew(df[c]):.2f}")

fig, axs = plt.subplots(2, 2, figsize=(10, 8))
for ax, c in zip(axs.ravel(), cols):
    stats.probplot(df[c], dist="norm", plot=ax)
    ax.set_title(f"Q-Q plot: {c}")
plt.tight_layout()
plt.savefig("qqplots.png", dpi=150)
plt.close()

# ---------- 4. thalach: disease vs healthy ----------
sick = df.loc[df["target"] == 1, "thalach"]
healthy = df.loc[df["target"] == 0, "thalach"]

print("\n=== thalach: disease vs healthy ===")
print("Shapiro p, disease:", stats.shapiro(sick).pvalue)
print("Shapiro p, healthy:", stats.shapiro(healthy).pvalue)
t, p_t = stats.ttest_ind(sick, healthy, equal_var=False)
print(f"Welch t-test: t = {t:.3f}, p = {p_t:.3g}")
u, p_u = stats.mannwhitneyu(sick, healthy, alternative="two-sided")
print(f"Mann-Whitney: U = {u:.1f}, p = {p_u:.3g}")

means = [sick.mean(), healthy.mean()]
sems = [stats.sem(sick), stats.sem(healthy)]
print(f"disease: mean = {means[0]:.2f}, SEM = {sems[0]:.2f}, n = {len(sick)}")
print(f"healthy: mean = {means[1]:.2f}, SEM = {sems[1]:.2f}, n = {len(healthy)}")

plt.figure(figsize=(4, 5))
plt.errorbar(["disease", "healthy"], means, yerr=sems, fmt="o", capsize=6)
plt.ylabel("mean thalach (bpm) +/- SEM")
plt.tight_layout()
plt.savefig("thalach_means.png", dpi=150)
plt.close()

# ---------- 5. age vs thalach ----------
r, p_r = stats.pearsonr(df["age"], df["thalach"])
rho, p_rho = stats.spearmanr(df["age"], df["thalach"])
print(f"\nPearson r = {r:.3f} (p = {p_r:.3g}), Spearman rho = {rho:.3f} (p = {p_rho:.3g})")

slope, intercept = np.polyfit(df["age"], df["thalach"], 1)
xs = np.linspace(df["age"].min(), df["age"].max(), 100)
plt.figure(figsize=(6, 5))
plt.scatter(df["age"], df["thalach"], s=12)
plt.plot(xs, slope * xs + intercept, "r-")
plt.xlabel("age")
plt.ylabel("thalach (max heart rate)")
plt.savefig("age_thalach.png", dpi=150)
plt.close()

# ---------- Bonus: entropy of target ----------
p = df["target"].value_counts(normalize=True)
H = -(p * np.log2(p)).sum()
print("\nproportions:\n", p)
print(f"entropy of target = {H:.3f} bits (max for 2 classes = 1)")
