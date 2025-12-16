import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load labeled data
data_file = "../../data/processed/upec_labeled_targets.csv"
df = pd.read_csv(data_file)

# Features and labels
feature_cols = ["length", "A_frac", "G_frac", "V_frac", "L_frac"]
X = df[feature_cols]
y = df["target_label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Train Random Forest
rf = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)
rf.fit(X_train, y_train)

# Evaluate
y_pred = rf.predict(X_test)
print(classification_report(y_test, y_pred))

# Predict probabilities for all proteins
df["target_probability"] = rf.predict_proba(X)[:, 1]

# Rank targets
df_ranked = df.sort_values("target_probability", ascending=False)

# Save results
output_file = "../../results/upec_ranked_targets.csv"
df_ranked.to_csv(output_file, index=False)

print(f"Ranked targets saved to: {output_file}")
print(df_ranked.head(10))
