# app.py
import streamlit as st
from Create_Strategy import create_strategy_page, SessionState  # Import the create_strategy_page function and SessionState class

# Define your tabs and their content
tabs = {
    "Dashboard": "This is the dashboard content.",
    "Strategies": "Here are the available strategies.",
    "Services": "Explore our services.",
    "My Subscriber Reports": "View your subscriber reports.",
    "Login": "Login to access premium features.",
}

# Function to create custom tab layout
def render_tabs():
    st.write("### Welcome to My App!")
    st.sidebar.title("Navigation")
    selected_tab = st.sidebar.radio("", list(tabs.keys()))

    # Display the selected tab content
    if selected_tab == "Strategies":
        st.write(tabs[selected_tab])
        st.write("## Strategies")

        # Create the dropdown menu with options
        selected_option = st.selectbox("Select an option:", ["Create", "Deployed", "My Strategies", "Marketplace", "BackTest"])

        # Handle the selected option
        if selected_option == "Create":
            session_state = SessionState()  # Create a SessionState instance
            create_strategy_page(session_state)  # Pass the SessionState instance to the "Create Strategy" page function
        elif selected_option == "Deployed":
            st.write("You selected 'Deployed'. Implement your 'Deployed' logic here.")
        elif selected_option == "My Strategies":
            st.write("You selected 'My Strategies'. Implement your 'My Strategies' logic here.")
        elif selected_option == "Marketplace":
            st.write("You selected 'Marketplace'. Implement your 'Marketplace' logic here.")
        elif selected_option == "BackTest":
            st.write("You selected 'BackTest'. Implement your 'BackTest' logic here.")
        else:
            st.write("Please select an option from the dropdown menu.")

    else:
        st.write(tabs[selected_tab])

# Custom CSS to display tabs horizontally
custom_css = """
<style>
    .tabs {
        display: flex;
        justify-content: space-around;
        margin-top: 1rem;
    }
</style>
"""

# Main app
def main():
    st.set_page_config(layout="wide")
    st.title("My Streamlit Dashboard")
    
    # Inject the custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)

    # Call the custom tab layout function
    with st.container():
        render_tabs()

if __name__ == "__main__":
    main()
