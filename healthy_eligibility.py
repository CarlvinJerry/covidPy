# Exercise Three----------------3 PART b(ii)

import pandas as pd

df = pd.read_excel(r'CS SAMPLE DATA.xlsx')

# Drop rows where at least one response is missing
df = df.dropna()


# Iterate over each row
for i, row in df.iterrows():
    if (df.loc[i, 'HEALTH CONDITIONS'] == 'NONE') & (df.loc[i, 'EMPLOYED?'] == 'YES-FORMAL'):
        print(f"{row['NAME']} is not eligible for relief because they are formally employed and healthy.")
    elif (df.loc[i, 'HEALTH CONDITIONS'] == 'NONE') & (df.loc[i, 'EMPLOYED?'] == 'YES-INFORMAL') \
            & (df.loc[i, 'NO. OF MINOR CHILDREN'] >= 3):
        print(f"{row['NAME']} is eligible for relief because they are healthy, "
              f"informally employed and have three or more children.")
    elif (df.loc[i, 'HEALTH CONDITIONS'] == 'NONE') & (df.loc[i, 'EMPLOYED?'] == 'NO') \
            & (df.loc[i, 'NO. OF MINOR CHILDREN'] > 0):
        print(f"{row['NAME']} is eligible for relief because they are healthy, have at "
              f"least one child but unemployed.")

