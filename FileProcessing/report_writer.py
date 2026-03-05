import logger, transformer, validator
import datetime as dt

logger = logger.setup_logger(__name__, "debug")

def write_summary_report(filepath, valid_records, errors, aggregations):
    """
    Write a formatted summary report.
    
    Report should include:
    - Processing timestamp
    - Total records processed
    - Number of valid records
    - Number of errors (with details)
    - Sales by store
    - Top 5 products
    """
    logger.debug("Generating summary report")
    valid_records, error_records, = len(valid_records), len(errors),
    total_records = error_records + valid_records

    report = f"""=== Sales Processing Report ===
    Generated: {dt.datetime.now()}

    Processing Statistics:
      - Total records: {total_records}
      - Valid records: {valid_records}
      - Error records: {error_records}

    Errors:
    """
    logger.debug("Generating error report")
    for e in errors:
        report += f"  - {e}"

    # sales by store
    logger.debug("Generating sales by store")
    report += "\nSales by Store:"
    by_store = transformer.aggregate_by_store(valid_records)
    for store in by_store:
        report += f"  - {store}: ${by_store[store]}"
    
    # Top products
    report += "\nTop Products:"
    by_product = transformer.aggregate_by_product(valid_records)
    for product in by_product:
        report += f"  - {product}: {by_product[product]} units"
    logger.debug("Report generated")

    logger.debug(f"Writing report to CSV file {filepath}")
    try:
        with open(filepath, "w+") as f:
            f.write(report)
            logger.info("Report written")
    except FileNotFoundError as e:
        logger.error(e)
    except Exception as e:
        logger.error(e)
    logger.debug("Attempt to write report completed.")

def write_clean_csv(filepath, records):
    """
    Write validated records to a clean CSV file.
    """
    logger.debug(f"Writing records to CSV file {filepath}")
    try:
        with open(filepath, "w+") as f:
            csv_cols = ""
            
            for r in records:
                #convert dict record to csv string
                
                f.write(r)
            logger.info("Records written")
    except FileNotFoundError as e:
        logger.error(e)
    except Exception as e:
        logger.error(e)
    logger.debug("Attempt to write records completed.")


def write_error_log(filepath, errors):
    """
    Write processing errors to a log file.
    """
    logger.debug(f"Writing errors to CSV file {filepath}")
    try:
        with open(filepath, "w+") as f:
            for e in errors:
                f.write(e)
            logger.info("Errors written")
    except FileNotFoundError as e:
        logger.error(e)
    except Exception as e:
        logger.error(e)
    logger.debug("Attempt to write errors completed.")

    