import streamlit as st

# Create a to-do list
def todo_list():
    st.title("To-Do List")
    
    # Get user input for new task
    task = st.text_input("Add a new task:")

    # Store tasks in a list
    tasks = st.session_state.get("tasks", [])

    # Add task to list
    if st.button("Add Task"):
        if task:
            tasks.append(task)
            st.session_state.tasks = tasks
            st.success("Task added successfully!")
        else:
            st.warning("Please enter a task.")

    # Display tasks
    if tasks:
        st.write("### Your Tasks:")
        for i, t in enumerate(tasks, start=1):
            st.write(f"{i}. {t}")
    else:
        st.write("Your to-do list is empty.")

# Run the app
if __name__ == "__main__":
    todo_list()
