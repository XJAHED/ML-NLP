from sqlalchemy import create_engine
import os
import pandas as pd
import numpy as np

data = {
    'Name' : ['ABC','Jahed', 'Mijan', 'Yasin', 'Sazil'],
    'Age' : [10,25, np.nan, 15, 30],
    'City' : [np.nan, 'Chittagong', 'Dhaka', np.nan, 'Kulna']
}

df = pd.DataFrame(data)
print(df.head())

# avg_forword_fill
avg_age = df['Age'].mean()

df['Age'].fillna(avg_age, inplace=True)
# df['Age'].fillna(avg_age, inplace=True)

print(df)


# df__cons = df.fillna('unknow')
# print(df__cons)

# df['Age'].fillna(df['Age'].mean(),inplace=True)
# print(df)
# print(df.isnull().mean())

# df_drop = df.dropna(how='all')
# print(df_drop)



# threshold = 0.10  # ১০%
# missing_ratio = df.isnull().mean()  # প্রতি column এ missing এর ratio বের করো
# columns_to_drop = missing_ratio[missing_ratio >= threshold].index  # যেগুলো ১০% বা বেশি missing
# df_cleaned = df.drop(columns=columns_to_drop)

# print("Dropped columns:", list(columns_to_drop))
# print(df_cleaned)