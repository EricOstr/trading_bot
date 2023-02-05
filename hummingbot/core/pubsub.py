
from enum import Enum
import logging
import random
from typing import List, TYPE_CHECKING

# from hummingbot.logger import HummingbotLogger
if TYPE_CHECKING:
    from hummingbot.core.event.event_listener import EventListener
# from hummingbot.core.event.event_listener cimport EventListener

# class_logger = None

class PubSub:

    ADD_LISTENER_GC_PROBABILITY = 0.005

    # @classmethod
    # def logger(cls) -> HummingbotLogger:
    #     global class_logger
    #     if class_logger is None:
    #         class_logger = logging.getLogger(__name__)
    #     return class_logger

    def __init__(self):
        self._events = dict() # keys are event int, values are set() EventListener objects

    def add_listener(self, event_tag: Enum, listener: "EventListener"):
        self.c_add_listener(event_tag.value, listener)

    def remove_listener(self, event_tag: Enum, listener: "EventListener"):
        self.c_remove_listener(event_tag.value, listener)

    def get_listeners(self, event_tag: Enum):
        return self.c_get_listeners(event_tag.value)

    def trigger_event(self, event_tag: Enum, message: any):
        self.c_trigger_event(event_tag.value, message)

    # cdef c_log_exception(self, int64_t event_tag, object arg):
    #     self.logger().error(f"Unexpected error while processing event {event_tag}.", exc_info=True)


    def c_add_listener(self, event_type: int, listener: "EventListener"):
        # adds EventListener
        if event_type not in self._events:
            self._events[event_type] = set()
        self._events[event_type].add(listener)


    def c_remove_listener(self, event_tag, listener: "EventListener"):
        if event_tag in self._events:
            if listener in self._events[event_tag]:
                self._events[event_tag].remove(listener)


    def c_get_listeners(self, event_tag):
        return self._events.get('event_tag', set())


    def c_trigger_event(self, event_tag, arg):
        ''' 
        event_tag will be something like 'MarketEvent.BuyOrderCreated'
        arg will be an event e.g.  
        
        '''
        for listener in self._events.get(event_tag, set()):
            try:
                listener.c_set_event_info(event_tag, self)
                listener.c_call(arg)
            except Exception:
                # self.c_log_exception(event_tag, arg)
                pass
            finally:
                listener.c_set_event_info(0, None)



