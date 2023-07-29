import pandas as pd


def get_fraudulent_for_control_data_percentage():
    df1 = pd.read_csv('train_data/control_data_percentage.csv')
    
    df2 = pd.read_csv('train_data/DataSet Users purchases June - Sheet1.csv')
    df2.drop_duplicates(inplace=True)

    common_cols = [col for col in df1.columns if col in df2.columns and col not in ['deposit_fraud', 'deposit_disputed', 'fraudulent']]

    df1 = df1.merge(df2, on=common_cols, how='left', suffixes=('', '_y'))

    for col in ['deposit_fraud', 'deposit_disputed', 'fraudulent']:
        df1[col].fillna(df1[col + '_y'], inplace=True)
        df1.drop(col + '_y', axis=1, inplace=True)

    df1.to_csv('output.csv', index=False)
