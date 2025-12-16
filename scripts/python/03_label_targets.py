import pandas as pd

input_file = "../../data/processed/upec_protein_features.csv"
output_file = "../../data/processed/upec_labeled_targets.csv"

df = pd.read_csv(input_file)

# Simple biological heuristics
df["target_label"] = (
    (df["length"] >= 100) &
    (df["length"] <= 600)
).astype(int)

print(df["target_label"].value_counts())

df.to_csv(output_file, index=False)
print(f"Labeled target file saved: {output_file}")
