# TOPSIS-Python

TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) implementation in Python.

## Description

This package provides a simple implementation of the TOPSIS method for multi-criteria decision-making. It allows users to perform a TOPSIS analysis using a CSV file with criteria values, weights, and impacts.

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
python -m topsis data.csv "1,2,1,1" "+,+,-,+" result.csv
```

## Example Input File 

| C1  | C2   | C3  | C4  |
|-----|------|-----|-----|
| 250 | 16   | 12  | 5   |
| 200 | 16   | 8   | 3   |
| 300 | 32   | 16  | 4   |
| 275 | 24   | 10  | 3   |

## Output 

| C1  | C2   | C3  | C4  | Topsis Score | Rank |
|-----|------|-----|-----|--------------|------|
| 250 | 16   | 12  | 5   | 0.63         | 2    |
| 200 | 16   | 8   | 3   | 0.37         | 4    |
| 300 | 32   | 16  | 4   | 0.78         | 1    |
| 275 | 24   | 10  | 3   | 0.52         | 3    |

