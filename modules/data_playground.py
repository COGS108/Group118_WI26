import pandas as pd
import glob
import os

folder = 'data/00-raw/vezina'
pattern = os.path.join(folder, "vezina_*.csv")

files = glob.glob(pattern)
print(files)
dfs=[]
for i in files:
    df_season = pd.read_csv(i)
    season = os.path.basename(i).split('_')[1].split(".")[0]
    
    df_season['season'] = int(season)
    dfs.append(df_season)

combined = pd.concat(dfs, ignore_index=True)
final_path = 'data/00-raw/vezina/test_vezina_combined.csv'
combined.to_csv(final_path, index=False)



