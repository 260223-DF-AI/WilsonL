import logger

logger = logger.setup_logger(__name__, "debug")

def calculate_totals(records):
    """
    Calculate line totals (quantity * price) for each record.
    Returns: Records with added 'total' field
    """
    logger.debug("Calculating line totals")
    for record in records:
        record["total"] = record["quantity"] * record["price"]
    return records

def aggregate_by_store(records):
    """
    Aggregate sales by store_id.
    Returns: Dict mapping store_id to total sales
    """
    logger.debug("Calculating store sales data")
    store_sales = {}
    for record in records:
        store_id = record["store_id"]
        sale_total = record["total"]
        store_total = store_sales.get(store_id)
        if store_total == None:
            store_total = 0
        store_sales.update({store_id : store_total+sale_total})
    return store_sales

def aggregate_by_product(records):
    """
    Aggregate sales by product.
    Returns: Dict mapping product to total quantity sold
    """
    logger.debug("Calculating sales by product")
    product_sales = {}
    for record in records:
        product = record["product"]
        sale_total = record["quantity"]
        product_total = record.get("product") # returns 0 if product not added yet
        if product_total == None:
            product_total = 0
        product_sales.update({product: sale_total+product_total})
    return product_sales