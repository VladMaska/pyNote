import uuid
from datetime import datetime

class Note:
    def __init__(self, text, id=None, created_at=None):
        self.id = id or str(uuid.uuid4())[:8]
        self.text = text
        self.created_at = created_at or datetime.now().isoformat()

    def to_dict(self):
        return {"id": self.id, "text": self.text, "created_at": self.created_at}

    @staticmethod
    def from_dict(data):
        return Note(data["text"], data["id"], data["created_at"])
