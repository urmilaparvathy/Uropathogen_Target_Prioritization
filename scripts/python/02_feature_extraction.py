from Bio import SeqIO
import pandas as pd

fasta_file = "../../data/raw/GCF_000005845.2_ASM584v2_protein.faa"

records = []

for record in SeqIO.parse(fasta_file, "fasta"):
    seq = str(record.seq)
    length = len(seq)

    aa_counts = {
        "A_frac": seq.count("A") / length,
        "G_frac": seq.count("G") / length,
        "V_frac": seq.count("V") / length,
        "L_frac": seq.count("L") / length
    }

    records.append({
        "protein_id": record.id,
        "length": length,
        **aa_counts
    })

df = pd.DataFrame(records)

output_file = "../../data/processed/upec_protein_features.csv"
df.to_csv(output_file, index=False)

print(f"Feature table generated: {output_file}")
print(df.head())
