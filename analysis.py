import pandas as pd

def load_inventory(filename):
    df = pd.read_csv(filename)
    return df

def get_low_stock(df):
    filtered_data = df[df['quantity'] <= 10]
    return filtered_data

if __name__ == "__main__":
    data = load_inventory('inventory.csv')
    print(get_low_stock(data))