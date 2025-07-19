import cProfile
import pstats
import io
from functools import wraps

def profile(sort_by='cumulative', limit=10):
    """
    A decorator that profiles the execution of a function using cProfile.

    Args:
        sort_by (str): The stat to sort the results by (e.g., 'cumulative', 'time', 'calls').
                       See pstats.Stats.sort_stats for available options.
        limit (int): The number of lines to print from the profiling results.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            profiler = cProfile.Profile()
            profiler.enable()  # Start profiling

            result = func(*args, **kwargs) # Execute the decorated function

            profiler.disable() # Stop profiling

            # Process and print the profiling results
            s = io.StringIO()
            ps = pstats.Stats(profiler, stream=s).sort_stats(sort_by)
            ps.print_stats(limit)
            print(f"\n--- Profiling results for '{func.__name__}' ---\n")
            print(s.getvalue())
            print(f"--- End profiling results for '{func.__name__}' ---\n")
            
            return result
        return wrapper
    return decorator
