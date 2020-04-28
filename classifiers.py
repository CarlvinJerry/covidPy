# Exercise Six----------------6 Classification of vulnerable families

import pandas as pd
import numpy as np


df = pd.read_excel(r'CS SAMPLE DATA.xlsx')

# Drop rows where at least one response is missing
df = df.dropna()

# Vulnerable families------
eligibleAge = df[(df.AGE > 70) & (df['ON GOVERNMENT SUPPORT?'] == 'NO')]
eligibleTerminals = df[
    (df.AGE < 70) & (df['HEALTH CONDITIONS'].isin(['HIV POSITIVE', 'CANCER', 'ASTHMA', 'DIABETES'])) &
    (df['EMPLOYED?'] != 'YES-FORMAL')]
eligibleHealthy = df[(df['HEALTH CONDITIONS'] == 'NONE') & (df['EMPLOYED?'] == 'YES-INFORMAL') &
                     (df['NO. OF MINOR CHILDREN'] >= 3)]
eligibleHealthyUnemployed = df[
    (df['HEALTH CONDITIONS'] == 'NONE') & (df['EMPLOYED?'] == 'NO') & (df['NO. OF MINOR CHILDREN'] > 0)]

eligibles = pd.concat([eligibleAge, eligibleTerminals, eligibleHealthy, eligibleHealthyUnemployed], axis=0)

df = eligibles

# Conditions for classification----
conditions = [
    # RED-----
    (df['AGE'] > 70) & (df['ON GOVERNMENT SUPPORT?'] == 'NO'),
    (df['HEALTH CONDITIONS'].isin(['HIV POSITIVE', 'CANCER', 'ASTHMA', 'DIABETES'])) & (
            df['NO. OF MINOR CHILDREN'] >= 2),

    # AMBER-----
    (df['HEALTH CONDITIONS'].isin(['HIV POSITIVE', 'CANCER', 'ASTHMA', 'DIABETES'])) & (
            df['NO. OF MINOR CHILDREN'] <= 1),
    (df['HEALTH CONDITIONS'] == 'NONE') & (df['EMPLOYED?'] == 'YES-INFORMAL') & (df['NO. OF MINOR CHILDREN'] > 4),
    (df['HEALTH CONDITIONS'] == 'NONE') & (df['EMPLOYED?'] == 'NO') & (df['NO. OF MINOR CHILDREN'] >= 2),

    # GREEN----
    (df['HEALTH CONDITIONS'] == 'NONE') & (df['EMPLOYED?'] == 'NO') & (df['NO. OF MINOR CHILDREN'] == 1),
    (df['HEALTH CONDITIONS'] == 'NONE') & (df['EMPLOYED?'] == 'YES-INFORMAL') & (df['NO. OF MINOR CHILDREN'] == 3)
]

choices = ['RED', 'RED', 'AMBER', 'AMBER', 'AMBER', 'GREEN', 'GREEN']
df['CLASS'] = np.select(conditions, choices, default='black')
print(df[['NAME','CLASS']])
