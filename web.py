import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'].strip()
    if todo:
        todos.append(todo  + "\n")
        functions.write_todos(todos)
        st.session_state['new_todo'] = ""


st.title("Todo app")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{todo}_{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"{todo}_{index}"]
        st.rerun()

st.text_input(label="Add a new todo:", placeholder="Type here...", on_change=add_todo, key='new_todo')
st.write("---")
# st.session_state