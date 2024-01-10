# Student Management System (CLI)

## 📌 Overview
A command-line based Student Management System built using Python.
The project demonstrates clean code structure,   persistent storage,  
unit testing, and Git/GitHub workflow. 

---

## 🛠 Technologies Used
- Python
- Git & GitHub
- Pytest (unit testing)

---

## 📂 Project Structure
```
project/
├── src/
│   ├── main.py        # CLI entry point
│   └── utils.py       # Core logic
├── data/
│   └── students.json  # Persistent storage
├── tests/
│   └── test_utils.py  # Unit tests
├── README.md

```

## 🚀 Features
- Add student
- View student list
- Search student
- Delete student
- Persistent JSON-based storage
- Command-line interface (CLI)
- Unit testing with pytest

---

## ▶️ How to Run

Add student:
python src/main.py add --name Rahul

List students:
python src/main.py list

Search student:
python src/main.py search --name Rahul

Delete student:
python src/main.py delete --name Rahul

## Run Tests
python -m pytest

### 1️⃣ Clone the repository
```bash
git clone https://github.com/022RaTiNdRa/my-first-git-project.git
cd my-first-git-project
