import pandas as pd
import re
column = ['Target', 'ID', 'Date', 'Flag', 'User', 'Comments']
df = pd.read_csv('tweets.csv', encoding='latin1', names=column)

# print(df.columns.tolist())
# print(df.info()) # missing values, data types read
# print(df.isnull().sum()) # output total missing values sum
# print(df.duplicated().sum()) # output total duplicate rows

# print(df.describe())
# df['sentiment'] = df['Target'].map({0: 'Negative', 2: 'Neutral', 4: 'Positive'})
# print(df.columns)

# lowercase and uppercase the comments
# df_lower = pd.Series(['lower'], index=df.columns).str.lower()
df_lower = df['Comments'].str.upper()

# remove URLS
url_pattern = r'https?://\S+|www\.\S+|@\w+|#\w+'
df['Comments'] = df['Comments'].apply(lambda x: re.sub(url_pattern, '',x))

print(df)

