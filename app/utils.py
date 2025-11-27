from typing import Callable
import functools

def event(f: Callable):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
        
    wrapper.is_event = True
    wrapper.event_name = "".join([s.capitalize() for s in wrapper.__name__.split('_')]) + "Event"
    return wrapper