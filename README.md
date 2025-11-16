## 🧬 CT Radiomics Feature Extraction

Extract quantitative radiomics features (first-order, texture, wavelet) from CT scans and export them into a clean CSV file — ready for machine-learning, multimodal AI, or clinical modeling.

<p align="center"> <img src="media/radiomics_pipeline.png" alt="Radiomics Pipeline Overview" width="80%"> </p>
🧠 Radiomics Pipeline Overview

This project demonstrates an end-to-end radiomics workflow for medical imaging:

🧩 1. Image Loading

Reads .nii CT volumes

Uses SimpleITK for robust medical image I/O

Handles 3D images with native spacing

## 🧩 2. Automatic Mask Generation

If no segmentation mask is provided

Uses Otsu Thresholding + Largest Connected Component

Produces a clean binary ROI mask

🧩 3. Radiomics Feature Extraction

Powered by PyRadiomics v3.0.1:

First-order statistics

GLCM, GLSZM, GLRLM, NGTDM, Shape

LoG & Wavelet filtered textures

100+ high-dimensional imaging biomarkers

🧩 4. CSV Export

All features saved into:

radiomics_full_features.csv


Perfect for ML pipelines, multimodal fusion, and deep learning.

## 📊 Example Output
<p align="center"> <img src="media/radiomics_csv_preview.png" width="70%"> </p> <p align="center"> <em>Figure: Radiomics feature table containing 100+ quantitative biomarkers extracted from CT images.</em> </p>
⚙️ Setup Instructions (WSL2 + Ubuntu)
Step 1 — Create Isolated Environment
sudo apt update
sudo apt install python3-pip python3-venv -y

python3 -m venv radiomics-env
source radiomics-env/bin/activate

Step 2 — Install Dependencies
pip install --upgrade pip wheel setuptools
pip install SimpleITK nibabel pydicom versioneer
pip install --no-build-isolation https://github.com/AIM-Harvard/pyradiomics/archive/refs/tags/v3.0.1.zip
pip install pandas

📦 Code Structure
📁 radiomics-project/
│── 📄 analysis.py               # main extractor script
│── 📄 make_list.py              # auto-generates list of CT scans
│── 📄 params.yaml               # radiomics configuration
│── 📄 requirements.txt
│── 📄 radiomics_full_features.csv
│── 📁 media/
│     └── radiomics_pipeline.png
│     └── radiomics_csv_preview.png

🚀 Run the Pipeline

Generate list of CT files:

python3 make_list.py


Run radiomics extraction:

python3 analysis.py


CSV output generated:

radiomics_full_features.csv

## 📈 Sample of Extracted Metrics
Feature Group	Examples
First Order	Energy, Entropy, Mean, Variance
GLCM	Contrast, Homogeneity, Correlation
GLRLM	RunLengthNonUniformity, ShortRunEmphasis
GLSZM	ZoneVariance, SizeZoneNonUniformity
NGTDM	Coarseness, Strength
Wavelet	wavelet-LLH_GLCM_Contrast, etc.

A total of ~100–120 biomarkers per CT volume.

##📜 Requirements
SimpleITK
pyradiomics==3.0.1
nibabel
pydicom
pandas
numpy

## 📄 License

MIT License — free to use, modify, and distribute.

🙌 Acknowledgements

PyRadiomics (AIM Harvard Medical School)

SimpleITK & ITK

WSL2 Ubuntu for fast experimentation
