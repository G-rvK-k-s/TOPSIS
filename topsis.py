import argparse
import pandas as pd
import numpy as np
import os

def calculate_topsis(decision_matrix, weight_vector, impact_vector):
    # Ensure the inputs are numpy arrays
    decision_matrix = np.array(decision_matrix, dtype=float)
    weight_vector = np.array(weight_vector, dtype=float)

    # Step 1: Normalize the decision matrix
    norm_matrix = decision_matrix / np.sqrt((decision_matrix ** 2).sum(axis=0))

    # Step 2: Apply weights to the normalized matrix
    weighted_matrix = norm_matrix * weight_vector

    # Step 3: Determine the ideal best and worst values
    ideal_best = [
        max(weighted_matrix[:, col]) if impact_vector[col] == '+' else min(weighted_matrix[:, col])
        for col in range(len(impact_vector))
    ]
    ideal_worst = [
        min(weighted_matrix[:, col]) if impact_vector[col] == '+' else max(weighted_matrix[:, col])
        for col in range(len(impact_vector))
    ]

    # Step 4: Compute distances from the ideal best and worst
    distance_to_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
    distance_to_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

    # Step 5: Calculate performance scores and ranks
    scores = distance_to_worst / (distance_to_best + distance_to_worst)
    rankings = scores.argsort()[::-1] + 1

    return scores, rankings

def main():
    parser = argparse.ArgumentParser(description="Conduct a TOPSIS analysis on a dataset.")
    parser.add_argument("input_file", help="Path to the input CSV file")
    parser.add_argument("weights", help="Comma-separated weights (e.g., 1,1,2,1)")
    parser.add_argument("impacts", help="Comma-separated impacts (e.g., +,+,-,+)")
    parser.add_argument("output_file", help="Path to save the output CSV file")
    args = parser.parse_args()

    # Check if the input file exists
    if not os.path.exists(args.input_file):
        print("Error: The specified input file does not exist.")
        return

    # Load the dataset
    try:
        data = pd.read_csv(args.input_file)
    except Exception as e:
        print(f"Error: Failed to load the input file. Details: {e}")
        return

    print("Loaded data:")
    print(data.head())  # Display the first few rows of the dataset

    # Validate the dataset format
    if data.shape[1] < 3:
        print("Error: The input file must include at least three columns.")
        return

    try:
        weights = [float(w) for w in args.weights.split(',')]
        impacts = args.impacts.split(',')
    except ValueError:
        print("Error: Ensure weights are numeric and impacts are valid (+ or -).")
        return

    if len(weights) != data.shape[1] - 1 or len(impacts) != data.shape[1] - 1:
        print("Error: The number of weights and impacts must match the number of criteria columns.")
        return

    if not all(impact in ['+', '-'] for impact in impacts):
        print("Error: Impacts can only be '+' or '-'.")
        return

    # Run the TOPSIS analysis
    try:
        criteria_matrix = data.iloc[:, 1:].values
        scores, rankings = calculate_topsis(criteria_matrix, weights, impacts)
    except Exception as e:
        print(f"Error: An issue occurred during the TOPSIS calculation. Details: {e}")
        return

    # Append the results to the dataset
    data["Topsis Score"] = scores
    data["Rank"] = rankings

    # Save the updated dataset
    try:
        data.to_csv(args.output_file, index=False)
        print(f"Results have been successfully saved to {args.output_file}")
    except Exception as e:
        print(f"Error: Unable to save the results. Details: {e}")

if __name__ == "__main__":
    main()
