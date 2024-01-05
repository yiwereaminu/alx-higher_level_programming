#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # Get all names defined in the module
    module_names = dir(hidden_4)

    # Filter names that do not start with __
    filtered_n = [name for name in module_names if not name.startswith("__")]

    # Sort the names in alphabetical order
    sorted_names = sorted(filtered_n)

    # Print each name on a new line
    for name in sorted_names:
        print(name)
