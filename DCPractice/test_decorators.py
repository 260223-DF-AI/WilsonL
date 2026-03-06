import pytest
from decorators import timer, retry, cache

def test_timer_returns_result():
    """Timer decorator should not affect return value."""

    def add_no_timer(a, b):
        return a + b
    
    @timer
    def add_with_timer(a, b):
        return a + b
    
    a, b = 2, 3
    assert(add_no_timer(a, b) == add_with_timer(a, b))

def test_retry_succeeds_eventually():
    """Retry should succeed if function works within attempts."""
    @retry(max_attempts=3)
    def add(a, b):
        return a+b
    

def test_cache_returns_cached_value():
    """Cache should return same value without recomputing."""
    pass

def test_cache_info_tracks_hits():
    """Cache info should track hits and misses."""
    pass
