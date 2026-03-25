import pandas as pd

def load_inventory(filename):
    df = pd.read_csv(filename)
    return df

if __name__ == "__main__":
    print(load_inventory('inventory.csv'))