import pandas as pd
import os

# Paths
path1 = r'C:\Users\SANAD\IntelliGuard\datasets\augmented_dataset_v2.csv'
path2 = r'C:\Users\SANAD\IntelliGuard\datasets\hard_prompts_50k.csv'
output_path = r'C:\Users\SANAD\IntelliGuard\datasets\intelliguard_brain_master_v2.csv'

# Load datasets
df1 = pd.read_csv(path1)
df2 = pd.read_csv(path2)

# Normalize column names if needed
# df1 usually has: text,category,label,target_layer
# df2 has: text,category,label,target_layer

# Merge
combined_df = pd.concat([df1, df2], ignore_index=True)

# Shuffle
combined_df = combined_df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save
combined_df.to_csv(output_path, index=False)

print(f"Merged {len(df1)} and {len(df2)} samples.")
print(f"Total samples: {len(combined_df)}")
print(f"Saved to: {output_path}")
