import argparse
import pandas as pd
import numpy as np
import os

def topsis(matrix, weights, impacts):
    # Convert matrix and weights to numpy arrays
    matrix = np.array(matrix, dtype=float)
    weights = np.array(weights, dtype=float)
    
    # Normalize the matrix
    normalized_matrix = matrix / np.sqrt((matrix ** 2).sum(axis=0))

    # Weighted normalization
    weighted_matrix = normalized_matrix * weights

    # Calculate ideal best and ideal worst
    ideal_best = [
        max(weighted_matrix[:, i]) if impacts[i] == '+' else min(weighted_matrix[:, i])
        for i in range(len(impacts))
    ]
    ideal_worst = [
        min(weighted_matrix[:, i]) if impacts[i] == '+' else max(weighted_matrix[:, i])
        for i in range(len(impacts))
    ]

    # Calculate distances
    distance_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
    distance_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

    # Calculate scores and ranks
    scores = distance_worst / (distance_best + distance_worst)
    ranks = scores.argsort()[::-1] + 1

    return scores, ranks

def main():
    parser = argparse.ArgumentParser(description="Perform TOPSIS analysis on a dataset.")
    parser.add_argument("input_file", help="Input CSV file path")
    parser.add_argument("weights", help="Comma-separated weights (e.g., 1,2,1,1)")
    parser.add_argument("impacts", help="Comma-separated impacts (e.g., +,+,-,+)")
    parser.add_argument("output_file", help="Output CSV file path")
    args = parser.parse_args()

    # Check if file exists
    if not os.path.isfile(args.input_file):
        print("Error: Input file does not exist.")
        return

    # Read input file
    try:
        data = pd.read_csv(args.input_file)
    except Exception as e:
        print(f"Error: Unable to read the input file. {e}")
        return

    # Print the data and its shape
    print("Data read from CSV file:")
    print(data)  # Check the loaded data
    print("Matrix shape (rows, criteria):", data.iloc[:, 1:].shape)

    # Validate input file
    if data.shape[1] < 3:
        print("Error: Input file must have at least 3 columns (1 for alternatives and others for criteria).")
        return

    try:
        weights = list(map(float, args.weights.split(',')))
        impacts = args.impacts.split(',')
    except ValueError:
        print("Error: Weights must be numeric and impacts must be '+' or '-'.")
        return

    if len(weights) != data.shape[1] - 1 or len(impacts) != data.shape[1] - 1:
        print(f"Debug: Number of criteria: {data.shape[1] - 1}")
        print(f"Debug: Number of weights: {len(weights)}")
        print(f"Debug: Number of impacts: {len(impacts)}")
        print("Error: Number of weights and impacts must match the number of criteria.")
        return

    if not all(i in ['+', '-'] for i in impacts):
        print("Error: Impacts must only contain '+' or '-'.")
        return

    # Perform TOPSIS
    try:
        matrix = data.iloc[:, 1:].values
        scores, ranks = topsis(matrix, weights, impacts)
    except Exception as e:
        print(f"Error: Failed to perform TOPSIS. {e}")
        return

    # Add results to the DataFrame
    data["Topsis Score"] = scores
    data["Rank"] = ranks

    # Save results
    try:
        data.to_csv(args.output_file, index=False)
        print(f"Results saved to {args.output_file}")
    except Exception as e:
        print(f"Error: Unable to save the results. {e}")

if __name__ == "__main__":
    main()
