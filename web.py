import func
import streamlit as st

todos = func.get_todos()


def add_todo():
    new_todo = st.session_state['new_todo'] + '\n'
    todos.append(new_todo)
    func.write_todos(todos)


st.title('My To-Do App')
st.write('This app will hopefully help you to increase your productivity'
         'and stop procrastination.')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        func.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter To-Do", label_visibility='hidden', placeholder='What do you need todo...?',
              on_change=add_todo, key='new_todo')

