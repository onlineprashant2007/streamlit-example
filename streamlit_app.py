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
        st.write(tabs[selected_tab])
        # Add your login form or authentication logic here
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
    with st.beta_container():
        render_tabs()

if __name__ == "__main__":
    main()
