import pandas as pd

def load_inventory(filename):
    df = pd.read_csv(filename)
    return df

def get_low_stock(df):
    filtered_data = df[df['quantity'] <= 10]
    return filtered_data

def get_inventory_value(df):
    total_value = (df['quantity'] * df['unit_price']).sum().round(2)
    return total_value

def get_category_summary(df):
    new_df = df.copy()
    new_df['total_value'] = (new_df['quantity'] * new_df['unit_price'])
    grouped = new_df.groupby('category')
    return grouped.agg({'quantity': 'sum','total_value':'sum'}).round(2)


if __name__ == "__main__":
    data = load_inventory('inventory.csv')
    low_stock = get_low_stock(data)
    total_inventory_value = get_inventory_value(data)
    category_summary = get_category_summary(data)
    print(category_summary)