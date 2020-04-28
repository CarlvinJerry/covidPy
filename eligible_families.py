# Exercise Four----------------4 & 5 Eligibility

import pandas as pd

df = pd.read_excel(r'CS SAMPLE DATA.xlsx')

# Drop rows where at least one response is missing
df = df.dropna()

# Eligibles
eligibleAge = df[(df.AGE > 70) & (df['ON GOVERNMENT SUPPORT?'] == 'NO')]
eligibleTerminals = df[
    (df.AGE < 70) & (df['HEALTH CONDITIONS'].isin(['HIV POSITIVE', 'CANCER', 'ASTHMA', 'DIABETES'])) &
    (df['EMPLOYED?'] != 'YES-FORMAL')]
eligibleHealthy = df[(df['HEALTH CONDITIONS'] == 'NONE') & (df['EMPLOYED?'] == 'YES-INFORMAL') &
                     (df['NO. OF MINOR CHILDREN'] >= 3)]
eligibleHealthyUnemployed = df[
    (df['HEALTH CONDITIONS'] == 'NONE') & (df['EMPLOYED?'] == 'NO') & (df['NO. OF MINOR CHILDREN'] > 0)]

eligibles = pd.concat([eligibleAge, eligibleTerminals, eligibleHealthy, eligibleHealthyUnemployed], axis=0)

print(eligibles['NAME'])
