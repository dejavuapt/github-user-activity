from typing import Final, Callable
from datetime import datetime
from app.utils import event
import inspect


class GitEventsParser:
    _TEMPLATE: Final[str] = "- {time} | {action} in {repo}" 

    def __init__(self):
        pass

    def _parse_event(self, event: dict):
        action: str = event.get("type")
        name2method: dict = { getattr(m, "event_name", 'None'): m 
                      for _, m in inspect.getmembers(type(self), predicate=inspect.isfunction) if getattr(m, 'is_event', False) }
        method: Callable = name2method.get(action, None)
        formated_action: str = method(self, event.get('payload')) if method else action

        return self._TEMPLATE.format(
            time=datetime.fromisoformat(event.get("created_at")).strftime("%d.%m.%y %H:%M:%S"),
            action=formated_action,
            repo=event.get("repo").get("name") or None
        )

    def parse_events(self, events: list[dict]) -> list[str]:
        queue: list[str] = []
        for e in events:
            queue.append(self._parse_event(e))
            # break
        return queue
    
    @event
    def create(self, payload: dict) -> str:
        type_res = payload.get('ref')
        if not type_res:
            return "Create repo - "
        
        return f"{payload.get('ref')} {payload.get('ref_type')} created"

    @event
    def issue_comment(self, payload: dict[str, str]) -> str:
        return "issue_comment"