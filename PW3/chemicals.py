import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("chemicals_cancer.csv")
print(df.shape)
print(df.head())

# ---- Task 6: naive analysis ----
print("\n=== Naive correlation with malignancy ===")
print(df[["benzene", "cadmium"]].corrwith(df["malignancy"]))

# ---- Task 7: account for pollution_index ----
print("\n=== Correlation of cadmium with pollution_index ===")
print(df["cadmium"].corr(df["pollution_index"]))

print("\n=== Correlation with malignancy within narrow pollution bands ===")
for lo, hi in [(0, 20), (40, 60), (80, 100)]:
    s = df[(df["pollution_index"] > lo) & (df["pollution_index"] < hi)]
    print(f"\npollution_index in ({lo}, {hi}), n = {len(s)}")
    print(s[["benzene", "cadmium"]].corrwith(s["malignancy"]))

fig, axs = plt.subplots(2, 2, figsize=(10, 8))
axs[0, 0].scatter(df["benzene"], df["malignancy"], s=8)
axs[0, 0].set_title("All patients: benzene")
axs[0, 1].scatter(df["cadmium"], df["malignancy"], s=8)
axs[0, 1].set_title("All patients: cadmium")
s = df[(df["pollution_index"] > 40) & (df["pollution_index"] < 60)]
axs[1, 0].scatter(s["benzene"], s["malignancy"], s=8, color="C1")
axs[1, 0].set_title("Pollution 40-60: benzene")
axs[1, 1].scatter(s["cadmium"], s["malignancy"], s=8, color="C1")
axs[1, 1].set_title("Pollution 40-60: cadmium")
for ax in axs.ravel():
    ax.set_ylabel("malignancy")
axs[0, 0].set_xlabel("benzene"); axs[1, 0].set_xlabel("benzene")
axs[0, 1].set_xlabel("cadmium"); axs[1, 1].set_xlabel("cadmium")
plt.tight_layout()
plt.savefig("chemicals.png", dpi=150)
plt.close()
