import pandas as pd

# 1. Load the data
url = "https://data.humdata.org/dataset/cod-ps-ken/resource/d4fed43d-8abe-48d2-987a-35c101292af3/download/ken_admpop_adm1_2019.csv"
df = pd.read_csv(url)

# 2. Calculate total national population and the percentage share column (using lowercase)
total_national_pop = df['T_TL'].sum()
df['population_share_%'] = (df['T_TL'] / total_national_pop) * 100

# 3. Sort by percentage share from largest to smallest using the exact same name
sorted_shares = df.sort_values(by='population_share_%', ascending=False)

# 4. Save our newly analyzed data to a brand new CSV file on your computer
sorted_shares.to_csv('kenya_population_analyzed.csv', index=False)
print("--- SUCCESS: File saved as 'kenya_population_analyzed.csv' ---")

# 5. Print the top 5
print(sorted_shares[['ADM1_NAME', 'T_TL', 'population_share_%']].head(5))