from project import pomo
from project import convert_to_seconds
from project import intro
import pytest

def test_pomo():
    with pytest.raises(ValueError):
        pomo("Name", "Task", 1, 1, "rounds")

def test_convert_to_seconds():
    assert convert_to_seconds(1) == 60
    assert convert_to_seconds(5) == 300
    assert convert_to_seconds(25) == 1500

def test_intro():
    assert intro("Name", "Task", 25, 5, 3) == "Name is working on Task for 75 minutes with 5 minute breaks! Do not disturb!"
    assert intro("Bobby Macdonald", "Drafting an English Essay", 40, 7, 2) == "Bobby Macdonald is working on Drafting an English Essay for 80 minutes with 7 minute breaks! Do not disturb!"
    assert intro("Angelina", "CS50P", 2, 1, 2) == "Angelina is working on CS50P for 4 minutes with 1 minute breaks! Do not disturb!"


