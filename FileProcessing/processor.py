import logger, report_writer, validator, file_reader

logger = logger.setup_logger(__name__, "debug")

def process_sales_file(input_path, output_dir):
    """
    Main processing pipeline.
    
    1. Read the input file
    2. Validate all records
    3. Transform valid records
    4. Generate reports
    5. Handle any errors gracefully
    
    Returns: ProcessingResult with statistics
    """
    logger.debug(f"Processing sales file {input_path}")
    record_error_tuple = validator.validate_all_records(file_reader.read_csv_file(input_path))
    clean_records, errors = record_error_tuple[0], record_error_tuple[1]
    report_writer.write_clean_csv(f"{output_dir}/clean_records.csv", clean_records)
    report_writer.write_error_log(f"{output_dir}/error_log.txt", errors)
    report_writer.write_summary_report(f"{output_dir}/summary_report.txt", clean_records, errors, "")
    logger.info(f"Sales file processed: {input_path}")

if __name__ == "__main__":
    # Process from command line
    input_path = input("Enter input path: ")
    output_dir = input("Enter output directory: ")
    input_path = "WilsonL/FileProcessing/data/nice_sales.csv"
    output_dir = "WilsonL/FileProcessing/data"
    try:
        process_sales_file(input_path, output_dir)
    except Exception as e:
        logger.error(f"Error: {e}")