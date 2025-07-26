import json
import os
from pynote.note import Note

class Storage:
    def __init__(self, path="notes.json"):
        self.path = path
        self.notes = self.load()

    def load(self):
        if not os.path.exists(self.path):
            return []
        with open(self.path, "r") as f:
            return [Note.from_dict(n) for n in json.load(f)]

    def save(self):
        with open(self.path, "w") as f:
            json.dump([n.to_dict() for n in self.notes], f, indent=4)

    def add_note(self, text):
        note = Note(text)
        self.notes.append(note)
        self.save()
        return note

    def list_notes(self):
        return self.notes

    def search_notes(self, keyword):
        return [n for n in self.notes if keyword.lower() in n.text.lower()]

    def remove_note(self, note_id):
        self.notes = [n for n in self.notes if n.id != note_id]
        self.save()

    def clear_notes(self):
        self.notes = []
        self.save()
