import pandas as pd

def load_inventory(filename):
    df = pd.read_csv(filename)
    return df

def get_low_stock(df):
    filtered_data = df[df['quantity'] <= 10]
    return filtered_data

def get_inventory_value(df):
    total_value = (df['quantity'] * df['unit_price']).sum()
    return total_value

if __name__ == "__main__":
    data = load_inventory('inventory.csv')
    low_stock = get_low_stock(data)
    total_inventory_value = get_inventory_value(data)
    print(total_inventory_value)