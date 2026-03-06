from functools import wraps
import time
import logger_custom

logger_custom = logger_custom.setup_logger(__name__)

def timer(func):
    """
    Measure and print function execution time.
    
    Usage:
        @timer
        def slow_function():
            time.sleep(1)
    
    Output: "slow_function took 1.0023 seconds"
    """
    @wraps(func)
    def time_wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Function {func} took {end-start} seconds to execute")
    return time_wrapper

def logger(func):
    """
    Log function calls with arguments and return value.
    
    Usage:
        @logger
        def add(a, b):
            return a + b
        
        add(2, 3)
    
    Output:
        "Calling add(2, 3)"
        "add returned 5"
    """
    @wraps(func)
    def log_wrapper(*args, **kwargs):
        logger_custom.debug(f"Calling {func}({args, kwargs})")
        r = func(*args, **kwargs)
        logger_custom.info(f"{func} returned {r}")
    return log_wrapper

def retry(func, max_attempts=3, delay=1, exceptions=(Exception,)):
    """
    Retry a function on failure.
    
    Args:
        max_attempts: Maximum number of retry attempts
        delay: Seconds to wait between retries
        exceptions: Tuple of exceptions to catch
    
    Usage:
        @retry(max_attempts=3, delay=0.5)
        def flaky_api_call():
            # might fail sometimes
            pass
    """
    @wraps(func)
    def retry_wrapper(*args, **kwargs):
        for i in range(max_attempts):
            func(*args, **kwargs)
            time.sleep(delay)
        return retry_wrapper

def cache(max_size=128):
    """
    Cache function results.
    Similar to lru_cache but with visible cache inspection.
    
    Usage:
        @cache(max_size=100)
        def expensive_computation(x):
            return x ** 2
        
        expensive_computation(5)  # Computes
        expensive_computation(5)  # Returns cached
        
        # Inspect cache
        expensive_computation.cache_info()
        expensive_computation.cache_clear()
    """
    pass