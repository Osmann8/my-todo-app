import streamlit as st

with open("todos.txt","r") as file:
    todos = file.readlines()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    with open("todos.txt","w") as file:
        file.writelines(todos)


st.title("My Todo App")


for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        with open("todos.txt","w") as file:
            file.writelines(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="",placeholder="Add new todo",key="new_todo",
              on_change=add_todo)
st.session_state




