import pandas as pd

def load_data(filepath):
    """
    Load the orders dataset.
    - Parse dates correctly
    - Handle missing values
    - Return a clean DataFrame
    """
    df = pd.read_csv(filepath)
    df = clean_data(df)
    return df

def explore_data(df):
    """
    Print basic statistics about the dataset:
    - Shape (rows, columns)
    - Data types
    - Missing value counts
    - Basic statistics for numeric columns
    - Date range covered
    """
    print(df.shape)
    print(df.info)
    print(df.columns)
    print(df.dtypes)
    print(f"About quantity: {df['quantity'].describe()}")
    print(f"About price: {df['price'].describe()}")
    earliest_date = df.groupby("order_date")["order_date"].min()
    latest_date = df.groupby("order_date")["order_date"].max()
    print(f"Date range: {earliest_date} to {latest_date}")

def clean_data(df: pd.DataFrame):
    """
    Clean the dataset:
    - Remove duplicates
    - Fill or drop missing values (document your strategy)
    - Standardize text columns (strip whitespace, consistent case)
    - Add calculated columns: 'total_amount' = quantity * unit_price
    """
    df.drop_duplicates()
    # critical fields: drop if missing
    df.dropna(subset=["order_id", "product_name", "quantity", "unit_price"])
    # non-critical fields: fill & keep
    df.fillna("n/a")
    # strip whitespace/standardize case for text columns
    df[["customer_id", "product_name", "category", "region"]] = df[["customer_id", "product_name", "category", "region"]].apply(lambda x: x.str.strip().tolower())
    # total_cost column
    df["total_cost"] = df["quantity"] * df["unit_price"]

def add_time_features(df):
    """
    Add time-based features:
    - day_of_week (0=Monday, 6=Sunday)
    - month
    - quarter
    - is_weekend (boolean)
    """
    pass

def sales_by_category(df):
    """
    Calculate total sales and order count by category.
    Returns: DataFrame with columns [category, total_sales, order_count, avg_order_value]
    Sorted by total_sales descending.
    """
    pass

def sales_by_region(df):
    """
    Calculate total sales by region.
    Returns: DataFrame with columns [region, total_sales, percentage_of_total]
    """
    pass

def top_products(df, n=10):
    """
    Find top N products by total sales.
    Returns: DataFrame with columns [product_name, category, total_sales, units_sold]
    """
    pass

def daily_sales_trend(df):
    """
    Calculate daily sales totals.
    Returns: DataFrame with columns [date, total_sales, order_count]
    """
    pass

def customer_analysis(df):
    """
    Analyze customer purchasing behavior.
    Returns: DataFrame with columns [customer_id, total_spent, order_count, 
             avg_order_value, favorite_category]
    """
    pass

def weekend_vs_weekday(df):
    """
    Compare weekend vs weekday sales.
    Returns: Dict with weekend and weekday total sales and percentages.
    """
    pass