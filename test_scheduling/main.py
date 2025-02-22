#!/usr/bin/env python3
# main.py

import argparse
from utils import add_hyperparameters

def main():
    parser = argparse.ArgumentParser(description="Run experiment with hyperparameters")
    parser.add_argument('--h1', type=int, required=True, help='First hyperparameter')
    parser.add_argument('--h2', type=int, required=True, help='Second hyperparameter')
    args = parser.parse_args()

    # Call the helper function from utils.py
    result = add_hyperparameters(args.h1, args.h2)
    print(f"Result of adding {args.h1} and {args.h2}: {result}")

if __name__ == "__main__":
    main()
