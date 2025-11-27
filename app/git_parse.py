from typing import Final
from datetime import datetime



class GitParser:
    _TEMPLATE: Final[str] = "- {time} | {type} in {repo_name}" 
    EVENTS_MAP: Final[dict[str,str]] = {
        "CreateEvent": "__parse_createevent_payload"
    }

    def __init__(self):
        pass

    def parse_event(self, event: dict):
        callable_object = self.EVENTS_MAP.get(event.get("type"), None)
        if callable_object:
            method = getattr(self, "_" + type(self).__name__ + callable_object)
            call = method(event.get("payload"))
        else:
            call = callable_object 


        return self._TEMPLATE.format(
            time=datetime.fromisoformat(event.get("created_at")).today().strftime("%d.%m.%y %H:%M:%S"),
            type=call,
            repo_name=event.get("repo").get("name") or None
        )

    def parse_events(self, events: list[dict]) -> list[str]:
        queue: list[str] = []
        for e in events:
            queue.append(self.parse_event(e))
        return queue
    
    def __parse_createevent_payload(self, payload: dict) -> str:
        type_res = payload.get('ref')
        if not type_res:
            return "Create repo - "
        
        return f"{payload.get('ref')} {payload.get('ref_type')} created"
