import streamlit as st
import streamlit.components.v1 as components

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
    if selected_tab == "Login":
        st.title("Login")
        # Add your login form or authentication logic here
        # For example:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.button("Login")
        if login_button:
            # Implement your authentication logic here

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

    # Grid layout to display login on the right side
    col1, col2 = st.beta_columns([2, 1])
    with col1:
        render_tabs()
    with col2:
        st.image("path/to/your/image.png", width=100)  # Replace with your logo or any other content

if __name__ == "__main__":
    main()
