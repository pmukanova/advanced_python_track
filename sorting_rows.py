
import pandas as pd
df = pd.read_csv("/Users/perizatmenard/Documents/advanced_python/advanced_python_track/homelessness.csv")
# Sort homelessness by region, then descending family members
homelessness_reg_fam = df.sort_values(["region", "family_members"], ascending=[True, False])

# Print the top few rows
print(homelessness_reg_fam.head())