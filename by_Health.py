# Exercise Two----------------2 PART b(i)


import pandas as pd

df = pd.read_excel(r'CS SAMPLE DATA.xlsx')

# Drop rows where at least one response is missing
df = df.dropna()
# Drop rows where at least one response is missing
df = df.dropna()

# Subset data for health conditions
health_DF = pd.DataFrame(df, columns=['NAME', 'AGE', 'HEALTH CONDITIONS', 'EMPLOYED?'])

# Age < 70? , not formarly employed and has a terminal disease.
terminal_Diseases = ['HIV POSITIVE', 'CANCER', 'ASTHMA', 'DIABETES']
is_below_70 = health_DF[(health_DF.AGE < 70) & (health_DF['HEALTH CONDITIONS'].isin(terminal_Diseases)) &
                        (health_DF['EMPLOYED?'] != 'YES-FORMAL')]
# Iterate over each row
for index, row in is_below_70.iterrows():
    print(f"{row['NAME']} is eligible for relief since they suffer from a terminal illness.")
