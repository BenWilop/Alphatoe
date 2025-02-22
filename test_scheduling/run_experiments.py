#!/usr/bin/env python3
import os
import subprocess

# Define hyperparameter lists
h1_values = [1, 2, 3]
h2_values = [10, 20, 30]

# File to record completed combinations
done_file = "completed.txt"

# Ensure the file exists
if not os.path.exists(done_file):
    with open(done_file, "w") as f:
        pass

# Read completed combinations into a set for quick lookup
with open(done_file, "r") as f:
    completed = set(line.strip() for line in f if line.strip())

# Iterate over all combinations
for h1 in h1_values:
    for h2 in h2_values:
        combo = f"{h1},{h2}"
        if combo in completed:
            print(f"Skipping already completed combination: {combo}")
            continue

        print(f"Running combination: {combo}")
        # Call main.py with the current hyperparameters
        result = subprocess.run(["python3", "main.py", "--h1", str(h1), "--h2", str(h2)])
        
        # Check if main.py ran successfully before logging the combination
        if result.returncode == 0:
            with open(done_file, "a") as f:
                f.write(combo + "\n")
        else:
            print(f"Combination {combo} failed. Not marking as completed.")
