# Exercise Zero----------------0 Import exel file

import pandas as pd

df = pd.read_excel(r'CS SAMPLE DATA.xlsx')

# Drop rows where at least one response is missing
df = df.dropna()
print(df)
