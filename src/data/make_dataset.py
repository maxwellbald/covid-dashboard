import pandas as pd


def read_data(path):
    ext = path.split('.')[-1].lower()
    if ext == 'csv':
        return pd.read_csv(path,sep=',')
    elif ext == 'json':
        return pd.read_json(path)
    else:
        raise Exception('Unsupported file format')
