import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

# Load data
data_file = "../../data/processed/upec_labeled_targets.csv"
df = pd.read_csv(data_file)

feature_cols = ["length", "A_frac", "G_frac", "V_frac", "L_frac"]
X = df[feature_cols]
y = df["target_label"]

# Train model
rf = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)
rf.fit(X, y)

# Feature importance
importances = rf.feature_importances_

importance_df = pd.DataFrame({
    "feature": feature_cols,
    "importance": importances
}).sort_values("importance", ascending=False)

# Save table
importance_df.to_csv("../../results/feature_importance.csv", index=False)

# Plot
plt.figure(figsize=(6, 4))
plt.barh(importance_df["feature"], importance_df["importance"])
plt.xlabel("Importance Score")
plt.ylabel("Feature")
plt.title("Feature Importance for Target Prioritization")
plt.gca().invert_yaxis()
plt.tight_layout()

# Save figure
plt.savefig("../../figures/feature_importance.png", dpi=300)
plt.close()

print("Feature importance analysis completed.")
print(importance_df)
