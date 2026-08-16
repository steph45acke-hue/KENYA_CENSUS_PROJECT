import pandas as pd
from sqlalchemy import create_engine

# 1. Load your analyzed data
df = pd.read_csv('kenya_population_analyzed.csv')

# 2. Rename the column to remove the '%' symbol completely
df = df.rename(columns={'population_share_%': 'population_share_percent'})

# 3. Select only the clean columns we need
df_clean = df[['ADM1_NAME', 'T_TL', 'population_share_percent']]

# 4. Connect to your local MySQL database using your password
engine = create_engine("mysql+mysqlconnector://root:stephen0111301468@localhost/KenyaCensusDB")

# 5. Drop the old table and let Pandas create and populate it fresh automatically
df_clean.to_sql('county_population', con=engine, if_exists='replace', index=False)

print("--- SUCCESS: Table recreated and data fully loaded by Python! ---")