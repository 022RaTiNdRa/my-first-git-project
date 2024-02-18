import os
import json
from src.utils import add_student, delete_student, search_student

TEST_FILE = "data/test_students.json" 

def setup_module(module):
    with open(TEST_FILE, "w") as f:
        json.dump([], f)

def teardown_module(module):
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

def test_add_student():
    students = []
    add_student(students, "Rahul")
    assert "Rahul" in students

def test_delete_student():
    students = ["Rahul"]
    result = delete_student(students, "Rahul")
    assert result is True
    assert "Rahul" not in students

def test_search_student():
    students = ["Anita"]
    assert search_student(students, "Anita") is True
    assert search_student(students, "Rahul") is False
