# ACE-AI: an explainable digital assistant for chronic disease risk stratification and identification of potentially uncoded diagnoses in primary care
This repository contains research code accompanying the ACE-AI study. ACE-AI was developed to support chronic disease assessment in primary care by combining two complementary functions:
1. identification of existing record-based disease evidence, including potentially uncoded disease supported by structured electronic health record (EHR) data; and
2. multi-disease prediction of subsequent fulfilment of disease-defining criteria, with patient-level explanations generated using SHapley Additive exPlanations (SHAP).
The study was developed using Singapore's National Electronic Health Record (NEHR) and evaluated across eight chronic diseases:
- Diabetes Mellitus
- Dyslipidaemia
- Hypertension
- Stroke
- Heart Disease
- Renal Disease
- Osteoporosis
- Osteoarthritis
The source data used in the study are not distributed in this repository.

| File | Description |
|---|---|
| `ACE_BuildModel_Final.ipynb` | Model-development notebook containing data preparation, feature processing, multi-label neural-network training, prediction and model-evaluation code. |
| `Paper_FigTbl_2026_v2.ipynb` | Analysis notebook used to generate model-performance, clinical-utility and explainability analyses and associated manuscript/supplementary figures and tables. This includes SHAP-based analyses and other disease-specific evaluation outputs. |
| `Paper_Survey_FigTbl_2026_v1.ipynb` | Analysis notebook used to summarize the primary-care feasibility-pilot surveys and generate associated survey tables/figures. |
| `allimport_xai_v3.py` | Common Python imports used in explainability-related analysis workflows. |
