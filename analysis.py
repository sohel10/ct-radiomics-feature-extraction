import os
import pandas as pd
import SimpleITK as sitk
from radiomics import featureextractor

# -----------------------------
# 1. PATHS
# -----------------------------
data_dir = "/mnt/c/Users/sohel/Downloads/Ai_health/radiomics"
csv_file = os.path.join(data_dir, "radiomics_list.csv")
output_csv = os.path.join(data_dir, "radiomics_features.csv")
param_file = os.path.join(data_dir, "params.yaml")

# -----------------------------
# 2. LOAD NIFTI LIST
# -----------------------------
df = pd.read_csv(csv_file)
filenames = df["filename"].tolist()

# -----------------------------
# 3. PyRadiomics Extractor (with YAML settings)
# -----------------------------
extractor = featureextractor.RadiomicsFeatureExtractor(param_file)
print("Radiomics extractor configured!")

# -----------------------------
# 4. PROCESS IMAGES
# -----------------------------
results = []

for fname in filenames:
    nii_path = os.path.join(data_dir, fname)

    if not os.path.exists(nii_path):
        print(f"⚠ Missing file: {fname}")
        continue

    print(f"\nExtracting: {fname}")

    # Load image
    image = sitk.ReadImage(nii_path)

    # -----------------------------
    # SAFE MASK (avoids GLCM crash)
    # -----------------------------
    # Step 1 — Otsu threshold
    mask = sitk.OtsuThreshold(image, 0, 1)

    # Step 2 — Keep only the largest connected component
    cc = sitk.ConnectedComponent(mask)
    stats = sitk.LabelShapeStatisticsImageFilter()
    stats.Execute(cc)

    # Find the largest ROI
    largest_label = max(stats.GetLabels(), key=lambda l: stats.GetPhysicalSize(l))

    # Make final clean mask
    mask = sitk.BinaryThreshold(
        cc,
        lowerThreshold=largest_label,
        upperThreshold=largest_label,
        insideValue=1,
        outsideValue=0
    )

    # -----------------------------
    # 5. EXTRACT FEATURES
    # -----------------------------
    try:
        feature_vector = extractor.execute(image, mask)

        clean_features = {
            k: float(v) for k, v in feature_vector.items()
            if isinstance(v, (int, float))
        }
        clean_features["filename"] = fname

        results.append(clean_features)

    except Exception as e:
        print(f"❌ ERROR processing {fname}: {e}")
        continue

# -----------------------------
# 6. SAVE RESULTS
# -----------------------------
output_df = pd.DataFrame(results)
output_df.to_csv(output_csv, index=False)

print("\n---------------------------------------")
print("✔ DONE! Saved radiomics features to:")
print(output_csv)
print("---------------------------------------")
