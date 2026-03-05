class FileProcessingError(Exception):
    """Base exception for file processing errors."""
    def __init__(self, message = "An error occured processing the file"):
        self.message = message
        super().__init__(message)

class InvalidDataError(FileProcessingError):
    """Raised when data validation fails."""
    def __init__(self, value, expected_type):
        self.value = value
        self.expected_type = expected_type
        super().__init__(f"Value '{value}' is an invalid {expected_type}")

class MissingFieldError(FileProcessingError):
    """Raised when a required field is missing."""
    def __init__(self, field):
        self.field = field
        super().__init__(f"Missing field: {field}")