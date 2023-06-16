import pandas as pd
from datetime import datetime

def main():
    df = pd.read_csv('data.csv', index_col=0)
    for i in df.index:
        list = str(datetime.strptime(i, "%B %Y")).split(' ')[0].split('-')[0]
        df.rename(index={i: list}, inplace=True)

    new_df = (df.groupby(df.index).sum() / 12).round(2)
    new_df.drop("2004", axis=0)
    new_df.drop("2023", axis=0)
    print(new_df)
    new_df.to_csv('new_data.csv')
    

if __name__ == '__main__':
    main()