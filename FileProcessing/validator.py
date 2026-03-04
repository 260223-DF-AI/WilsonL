import logger, exceptions
import datetime 

logger = logger.setup_logger(__name__, "debug")
errors = []

def validate_sales_record(record: dict, line_number):
    """
    Validate a single sales record.
    
    Required fields: date, store_id, product, quantity, price
    Validation rules:
    - date must be in YYYY-MM-DD format
    - quantity must be a positive integer
    - price must be a positive number
    
    Returns: Validated record with converted types
    Raises: InvalidDataError or MissingFieldError
    """
    logger.debug(f"Validating record: {record}")
    # assuming record is passed in as dict
    date, store_id, product, quantity, price = record["date"], record["store_id"], record["product"], record["quantity"], record["price"]

    # catch missing fields
    if date == "":
        e = exceptions.MissingFieldError("date")
        logger.warning(e)
        errors.append(e)
    if store_id == "":
        e = exceptions.MissingFieldError("store_id")
        logger.warning(e)
        errors.append(e)
    if product == "":
        e = exceptions.MissingFieldError("product")
        logger.warning(e)
        errors.append(e)
    if quantity == "":
        e = exceptions.MissingFieldError("quantity")
        logger.warning(e)
        errors.append(e)
    if price == "":
        e = exceptions.MissingFieldError("price")
        logger.warning(e)
        errors.append(e)
    # validate date: YYYY-MM-DD
    # using date object
    try:
        year, month, day = int(date[:5]), int(date[5:7]), int(date[8:])
        date = datetime.date(year, month, day)
    except:
        e = exceptions.InvalidDataError(date, "YYYY-MM-DD")
        logger.warning(e)
        errors.append(e)
    
    # validate quantity
    if not isinstance(quantity, int) or quantity < 0:
        e = exceptions.InvalidDataError(quantity, "positive integer")
        logger.warning(e)
        errors.append(e)

    # validate price
    if price < 0 or not isinstance(price, int, float):
        e = exceptions.InvalidDataError(price, "positive number")
        logger.warning(e)
        errors.append(e)
    
    record["date"], record["store_id"], record["product"], record["quantity"], record["price"] = date, store_id, product, quantity, price
    logger.debug(f"Record validation completed")

def validate_all_records(records):
    """
    Validate all records, collecting errors instead of stopping.
    
    Returns: Tuple of (valid_records, error_list)
    """
    errors.clear()
    logger.debug("Validating all records")
    for i in range(len(records)):
        record = records[i]
        validate_sales_record(record, i)
    logger.debug("All records validated")
    return (records, errors)