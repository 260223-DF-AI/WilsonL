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
    d_list = []
    with open(filepath, "r") as f:
        contents = f.read()
        for line in contents:
            line = line.strip().split(",")
            entry = {
                "date": line[0],
                "store_id": line[1],
                "product": line[2],
                "quantity": line[3],
                "price": line[4]
            }
            d_list.append(entry)
    return d_list