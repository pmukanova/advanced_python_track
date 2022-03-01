import pandas as pd
homelessness = pd.read_csv("/Users/perizatmenard/Documents/advanced_python/advanced_python_track/homelessness.csv")

# Select the individuals column
individuals = homelessness["individuals"]
ind_state = homelessness[["individuals", "state"]]

# Print the head of the result
print(individuals.head())