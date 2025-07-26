# pyNote

📝 **pyNote** is a simple and lightweight command-line note manager written in Python. It helps you quickly create, search, and organize your notes directly from the terminal. Notes are stored in a local JSON file.

---

## 🚀 Features

- Add, list, search, and remove notes
- Simple JSON-based storage (no DB needed)
- CLI interface using `argparse`
- Clean modular structure
- MIT licensed & open-source

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/pyNote.git
cd pyNote

# (Optional) create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🛠 Usage

```bash
# Add a new note
python main.py add "Buy groceries"

# List all notes
python main.py list

# Search for notes
python main.py search "groceries"

# Remove a note by ID
python main.py remove <note_id>

# Clear all notes
python main.py clear
```

### 🧪 Example

```bash
$ python main.py add "Read Python documentation"
Note added: 9e2c3a4b

$ python main.py list
[9e2c3a4b] Read Python documentation (2025-07-26T00:23:51.123456)
```

---

## 📁 Project Structure

```
pyNote/
├── main.py            # Entry point
├── cli.py             # CLI handler
├── pynote/
│   ├── __init__.py
│   ├── note.py        # Note model
│   └── storage.py     # JSON storage logic
├── tests/
│   └── test_basic.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 📌 Roadmap

-

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.