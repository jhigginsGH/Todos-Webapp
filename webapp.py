import streamlit as sl
import functions

sl.title("My Todos")


def add_todo():
    todo = sl.session_state["input_todo_box"]
    todos = functions.get_todos()
    todos.append(todo + '\n')
    functions.write_todos(todos)
    sl.session_state["input_todo_box"] = ''


todos = functions.get_todos()

for todo in todos:
    functions.checkbox_text(todo)

input_todo_box = sl.text_input(label='Enter Todo Here', label_visibility="hidden", placeholder="Enter Todo Here", key="input_todo_box", on_change=add_todo)