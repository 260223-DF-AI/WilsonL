import logger
import exceptions

logger = logger.setup_logger(__name__, "info")

def read_csv_file(filepath):
    """
    Read a CSV file and return a list of dictionaries.
    
    Should handle:
    - FileNotFoundError
    - UnicodeDecodeError (try utf-8, then latin-1)
    - Empty files
    
    Returns: List of dictionaries (one per row)
    Raises: FileProcessingError with descriptive message
    """
    logger.debug(f"Attempting to read csv file {filepath}")
    d_list = [] # list to return

    try:
        with open(filepath, "r") as f:
            # split the contents by line
            contents = f.read().split("\n")
            logger.debug("File read and split")

            # go through the file, line by line
            for i, line in enumerate(contents):
                logger.debug(f"Line {i}: {line}")
                if i == 0:
                    continue # ignore column names
                entry = {
                    "date": line[0],
                    "store_id": line[1],
                    "product": line[2],
                    "quantity": line[3],
                    "price": line[4]
                }

                d_list.append(entry)
                logger.debug(f"Entry appended: {entry}")
    except FileNotFoundError as e:
        logger.error(f"File not found error: {e}")
    except UnicodeDecodeError as e:
        logger.error(f"UnicodeDecodeError: {e}")
    except exceptions.FileProcessingError as e:
        logger.error(f"FileProcessingError: {e}")
    except Exception as e:
        logger.error(f"Other exception: {e}")
    else:
        logger.info(f"File successfully read:  {filepath}")
    return d_list

# test cases
# read_csv_file("WilsonL/FileProcessing/data/nice_sales.csv") #.csv with perfect sales data
# read_csv_file("WilsonL/FileProcessing/data/sample_sales.csv")
# read_csv_file("nosuchfile.py") # no such file
# read_csv_file("WilsonL/FileProcessing/data/empty_file.csv") # empty file
