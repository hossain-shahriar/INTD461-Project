import pandas as pd

# Input and output file names
input_file = "original_bengali_idioms.csv"      # your original CSV
output_file = "bengali_idioms.csv"  # the shuffled CSV

# Read the CSV
df = pd.read_csv(input_file)

# Shuffle the rows (random_state is optional, just for reproducibility)
shuffled_df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save to new CSV (without the extra index column)
shuffled_df.to_csv(output_file, index=False)

print(f"Shuffled file saved as: {output_file}")
