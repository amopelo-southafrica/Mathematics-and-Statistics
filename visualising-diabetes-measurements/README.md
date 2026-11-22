# Visualising Diabetes Measurements

This folder preserves the original educational notebook and supports its exploratory graphs of recorded glucose, BMI, age and an outcome indicator.

## Dataset correction

The original notebook requests `diabetes(1).csv` with columns `Outcome`, `Glucose` and `BMI`. The earlier file under that name contained a different 442-row progression dataset, so its shape and variables did not match the notebook.

- [`diabetes(1).csv`](diabetes(1).csv): **corrected 768-row outcome-labelled dataset**, recovered from the same user's HyperionDev M10T03 source, exact original Git SHA `db6f317685a4668bc0529b16ea1544022e780002`.
- [`diabetes.csv`](diabetes.csv): retained original 442-row progression dataset from M08T09. It is **not the appropriate input** for this notebook.
- [`diabetes_visualisation_corrected.ipynb`](diabetes_visualisation_corrected.ipynb): separately repaired notebook using nonzero medians; the original notebook is retained.
- [`diabetes_visualisation.ipynb`](diabetes_visualisation.ipynb): original analysis notebook, now able to load the matching filename and schema.

A full methodology and data-quality analysis is documented in the [AI Engineering research paper](https://github.com/amopelo-southafrica/AI-Engineering-and-Research/blob/main/Data-Analytics/visualising-diabetes-patterns/RESEARCH_PAPER.md) once built.

The dataset includes unrecorded or implausible zero values in several measurement columns. The notebook's median replacement method is descriptive preprocessing, not a validated clinical imputation method. This is educational analysis, not medical guidance.
