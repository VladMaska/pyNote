import argparse
from pynote.storage import Storage

def main():
    parser = argparse.ArgumentParser(description="pyNote - CLI note manager")
    parser.add_argument("command", choices=["add", "list", "search", "remove", "clear"])
    parser.add_argument("arg", nargs="?", help="Argument for the command")

    args = parser.parse_args()
    store = Storage()

    if args.command == "add" and args.arg:
        note = store.add_note(args.arg)
        print(f"Note added: {note.id}")
    elif args.command == "list":
        for n in store.list_notes():
            print(f"[{n.id}] {n.text} ({n.created_at})")
    elif args.command == "search" and args.arg:
        found = store.search_notes(args.arg)
        for n in found:
            print(f"[{n.id}] {n.text} ({n.created_at})")
    elif args.command == "remove" and args.arg:
        store.remove_note(args.arg)
        print(f"Note {args.arg} removed.")
    elif args.command == "clear":
        store.clear_notes()
        print("All notes cleared.")
    else:
        print("Invalid command or missing argument.")
