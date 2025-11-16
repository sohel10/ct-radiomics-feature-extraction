import os
import pandas as pd

data_dir = "/mnt/c/Users/sohel/Downloads/Ai_health/radiomics"

# List all NIfTI files in folder
files = [f for f in os.listdir(data_dir) if f.endswith(".nii") or f.endswith(".nii.gz")]

# Sort them for clean ordering
files = sorted(files)

df = pd.DataFrame({"filename": files})

output_csv = os.path.join(data_dir, "radiomics_list.csv")
df.to_csv(output_csv, index=False)

print("✔ radiomics_list.csv created!")
print(f"Found {len(files)} NIfTI files.")
print(f"Saved to: {output_csv}")
