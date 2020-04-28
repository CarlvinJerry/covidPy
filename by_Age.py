# Exercise One----------------1 PART a

import pandas as pd

df = pd.read_excel(r'CS SAMPLE DATA.xlsx')

# Drop rows where at least one response is missing
df = df.dropna()

# Subset data for age
age_DF = pd.DataFrame(df, columns=['NAME', 'AGE', 'ON GOVERNMENT SUPPORT?'])
# print each response:
# Is Age > 70? and not on government relief?
is_above_70 = age_DF[(age_DF.AGE > 70) & (age_DF['ON GOVERNMENT SUPPORT?'] == 'NO')]
# Iterate over each row
for index, row in is_above_70.iterrows():
    print(f"{row['NAME']} is eligible for relief based on their age.")

