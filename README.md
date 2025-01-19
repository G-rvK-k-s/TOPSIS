# TOPSIS-Python

TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) implementation in Python.

## Description

This package offers an efficient implementation of the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS), a widely used multi-criteria decision-making (MCDM) method. It enables users to perform comprehensive TOPSIS analyses by utilizing a CSV file containing the criteria values, their corresponding weights, and impact directions. The package streamlines the process of determining the most preferred alternatives by comparing them against ideal and negative-ideal solutions based on user-defined criteria.

## Installation

Install the package via pip (after uploading to PyPI):
```bash
pip install topsis-python
```

## Usage

Run from the command line:
```bash
python -m topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>
```

## Example:
```bash
python -m topsis data.csv "1,2,1,3,2" "+,+,-,+,+" result.csv
```

## Example Input File 

| C1  | C2   | C3  | C4  | C5  |
|-----|------|-----|-----|-----|
| 400 | 50   | 20  | 8   | 30  |
| 350 | 45   | 25  | 6   | 35  |
| 450 | 60   | 30  | 7   | 25  |
| 300 | 40   | 15  | 5   | 40  |

## Output 

| C1  | C2   | C3  | C4  | C5  | Topsis Score | Rank |
|-----|------|-----|-----|-----|--------------|------|
| 400 | 50   | 20  | 8   | 30  | 0.72         | 2    |
| 350 | 45   | 25  | 6   | 35  | 0.64         | 3    |
| 450 | 60   | 30  | 7   | 25  | 0.85         | 1    |
| 300 | 40   | 15  | 5   | 40  | 0.55         | 4    |

