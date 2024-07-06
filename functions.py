import os
import streamlit as sl

FILE = r"todos.txt"

if not os.path.exists(FILE):
     with open(FILE, 'w') as file:
          pass

def get_todos(filepath=FILE):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(file_contents, filepath=FILE):
    with open(filepath, 'w') as file:
        file.writelines(file_contents)  


def checkbox_text(text):
    sl.checkbox(f"{text}", key=f"check_{text}", on_change=complete_web)


def complete_web():

    check_boxes = []
    completed_todos = []

    for item in sl.session_state:
         if item.startswith("check"):
            check_boxes.append(item)

    for check in check_boxes:
        if sl.session_state[check] == True:
            completed_todos.append(check)
    
    todos = get_todos()

    for todo in completed_todos:
        todo = todo.replace('check_', '')
        if todo in todos:
            todos.remove(todo)
    
    write_todos(todos)
            
        

