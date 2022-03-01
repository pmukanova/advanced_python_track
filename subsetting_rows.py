import pandas as pd
homelessness = pd.read_csv("/Users/perizatmenard/Documents/advanced_python/advanced_python_track/homelessness.csv")

# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness["individuals"]>10000]

# Filter for rows where region is Mountain
mountain_reg = homelessness[homelessness["region"]=="Mountain"]

fam_lt_1k_pac = homelessness[(homelessness["family_members"]<1000) & (homelessness["region"] == "Pacific")]

# See the result
print(fam_lt_1k_pac)

# Subset for rows in South Atlantic or Mid-Atlantic regions
south_mid_atlantic = homelessness[homelessness["region"].isin(["South Atlantic","Mid-Atlantic"])]

# See the result
print(south_mid_atlantic)

# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness["state"].isin(canu)]

# See the result
print(mojave_homelessness)

