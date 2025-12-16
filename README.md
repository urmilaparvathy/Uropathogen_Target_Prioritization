# Omics-Driven and Machine Learning–Based Prioritization of Therapeutic Targets in Uropathogens

## Overview
This repository presents a reproducible computational framework for prioritizing therapeutic targets in uropathogens using proteome-derived features and machine learning. The pipeline converts raw pathogen proteomes into structured feature matrices, applies biologically motivated heuristics for target labeling, and employs interpretable machine learning models to rank candidate targets. The framework is designed to support downstream experimental validation, including eco-friendly antimicrobial or nano-enabled intervention strategies.
## Objectives
- Integrate transcriptomic and functional features of uropathogen genes
- Engineer biologically meaningful features for target prioritization
- Apply machine learning models to rank potential therapeutic targets
- Generate reproducible and interpretable outputs suitable for downstream experimental validation

## Scope
This project is designed to be executable on a personal computer and serves as a computational module that can complement experimental nanocomposite or antimicrobial development studies.

## Technologies Used
- Python (pandas, scikit-learn, Biopython)
- R (for expression analysis)
- Linux/WSL
- Git/GitHub

## Key Components
- Proteome-level feature engineering (protein length and amino-acid composition)
- Heuristic-based biological labeling of potential targets
- Random Forest–based target prioritization
- Model interpretability through feature importance analysis
- Fully reproducible and executable on a personal computer

## Results
- Ranked list of uropathogen proteins with target probability scores
- Feature importance analysis highlighting key determinants of prioritization
- Publication-style tables and figures suitable for reporting

## Repository Structure
data/ # Raw and processed datasets
scripts/ # Python and R analysis scripts
results/ # Ranked targets and model outputs
figures/ # Plots and visualizations


