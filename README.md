# Enhancing the “California Insect Barcoding Initiative” through Predictive Analysis of Mantis Distribution
### *Arielle Chen, Charles Lehnen, Dylan Andrews, Brian Tinsley*

## Overview
This GitHub repository is focused on the predictive analysis of mantis distribution to support the California Insect Barcoding Initiative (CIBI). It's an interdisciplinary project that blends data analysis with ecological and conservation efforts.

## Repository Structure
- `code/`: Contains the scripts and methodologies for the analysis.
- `data/`: Includes the datasets utilized in the study.
- `documents/`: Contains all the project-related documentation.
- `github_scripts/`: Scripts used for GitHub related operations.
- `output/`: Stores the final outputs of the analysis, particularly.

## Usage
Navigate to the `code/` directory to access the analysis scripts. Alternatively, code can be accessed and run through [Google Colab](https://drive.google.com/drive/folders/1eUpt1BPaIIdC9e4XXCeb8lFeDx5LxbYm)

#### Workflow

1. **Download Climatic Data** (`code/climatic_data/climatic_analysis_Windows.ipynb`) or (`code/climatic_data/climatic_analysis_Google_Colab.ipynb`)[^1]. Output: `output/netcdf_files`.
2. **Map Climatic Data** (`code/climatic_data/climatic_analysis_Windows.ipynb`) or (`code/climatic_data/climatic_analysis_Google_Colab.ipynb`).
3. **Convert Climatic Data to CSV** (`code/climatic_data/climatic_analysis_Windows.ipynb`) or (`code/climatic_data/climatic_analysis_Google_Colab.ipynb`). Output: `output/climatic_data`, organized by timestamp.
4. **Ecoregion Analysis** (`code/ecoregion_stuff/`)[^2].
5. **Human Population Analysis** (`code/human_population.ipynb`)[^3].
6. **Linear Regression Analysis** (`code/Mantis Linear Regressions`).
7. **SVM Analysis** (`code/svm_for_predicting_native_species.ipynb`).
8. **Decision Tree Analysis** (`code/decision_tree_analysis.ipynb`). Output: `output/decision_trees`.
9. **Biodiversity Analyses and Preliminary Analyses** (`code/`).
10. **GBIF Biodiversity Data**[^4] and **County shapefiles**[^5] (`data/`).


## Citing Our Work
If you use this project or its data in your research, please cite it appropriately:

#### Example Citation
Chen, A., Lehnen, C., Andrews, D., & Tinsley, B. (2023). Enhancing the “California Insect Barcoding Initiative” through Predictive Analysis of Mantis Distribution. DSCI_550_Final_Project. GitHub repository. https://github.com/CharlesLehnen/DSCI_550_Final_Project

## License
This project is licensed under the BSD-3-Clause License.

## References
[^1]: Unidata, (2023): Integrated Data Viewer (IDV) version 6.2u1. [http://doi.org/10.5065/D6RN35XM](http://doi.org/10.5065/D6RN35XM)
[^2]: Griffith, Glenn E., et al. "Ecoregions of California." US Geological Survey Open-File Report 1021 (2016): 1-45.
[^3]: U.S. Census Bureau (2020). Total Population, 2020 American Community Survey 5-Year Estimates Detailed Tables. [https://data.census.gov/](https://data.census.gov/)
[^4]: Telenius, Anders. "Biodiversity information goes public: GBIF at your service." Nordic Journal of Botany 29.3 (2011): 378-381.
[^5]: Database of Global Administrative Areas (2022). GADM database of Global Administrative Areas, version 4.1. [https://gadm.org](https://gadm.org)