# Titanic Machine Learning Project

This project is a submission to the Kaggle Titanic machine learning competition:
https://www.kaggle.com/competitions/titanic

Co-made by btfcookies and VJ50.

## Project Overview

The goal of this project is to predict passenger survival on the Titanic using supervised machine learning.
All analysis and modeling are done in the notebook `main.ipynb` using the provided training data in `train.csv`.

## Data Preparation

The project includes a preprocessing pipeline that:

- **Normalizes passenger names**: Tokenizes and cleans names (e.g., "Braund, Mr. Owen Harris" → "Braund Mr Owen Harris")
- **Extracts ticket prefixes**: Separates ticket codes from ticket numbers (e.g., "STON/O2. 3101282" → prefix: "STON/O2.", number: "3101282")
- **Creates derived features**: Generates `Ticket_number`, `Ticket_item`, and cleaned `Name` columns

## Dependencies

This project currently uses:

- pandas
- matplotlib
- seaborn
- tensorflow
- os
Recommended environment:

- Python 3.10+
- pip / pip3
- Jupyter Notebook or VS Code Notebook support

Install dependencies with:

```bash
python -m pip install [dependency name]
```

## Project Structure

- `main.ipynb`: Main notebook for data exploration, feature work, training, and evaluation.
- `train.csv`: Kaggle Titanic training dataset used in this project.
- `test.csv`: Kaggle Titanic test dataset to check accuracy
- `README.md`: Project documentation.

## How To Run

1. Ensure `train.csv` is in the project root.
2. Install dependencies.
3. Open `main.ipynb` and run cells from top to bottom.

## Competition

Kaggle Competition: Titanic - Machine Learning from Disaster
https://www.kaggle.com/competitions/titanic
