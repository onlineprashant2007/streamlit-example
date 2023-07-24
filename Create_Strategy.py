import streamlit as st
# Function to create the "Create Strategy" page
def create_strategy_page():
    st.title("Create Strategy")

    # Input for Strategy Name
    strategy_name = st.text_input("Strategy Name")

    # Input for Tags
    tags = st.text_input("Tags", help="Separate tags with commas (e.g., tag1, tag2)")

    # Text area for Description
    st.write("Description:")
    description = st.text_area("Enter your strategy description here", height=150)

    # Text formatting options
    st.subheader("Text Formatting")
    bold_text = st.checkbox("Bold", key="bold_checkbox")
    italic_text = st.checkbox("Italic", key="italic_checkbox")
    code_text = st.checkbox("Code", key="code_checkbox")

    # Display the formatted text
    formatted_text = strategy_name
    if bold_text:
        formatted_text = f"**{formatted_text}**"
    if italic_text:
        formatted_text = f"*{formatted_text}*"
    if code_text:
        formatted_text = f"`{formatted_text}`"

    st.markdown("Formatted Text:")
    st.markdown(formatted_text)

    # Save strategy button
    if st.button("Save Strategy"):
        # Save the strategy logic goes here
        pass  # Placeholder for the save strategy logic

    # Initialize Variables section
    st.header("Initialize Variables")

    # Add+ button
    add_button = st.button("Add+")

    # Show variables on click of Add+ button
    if add_button:
        variable_name = st.text_input("Variable Name")
        set_no = st.selectbox("Set No.", ["Set No1", "Set No2", "Set No3"])
        selected_set_no = int(set_no.split()[-1])
        option_menu = st.selectbox("Option Menu", ["Nifty 50", "BankNifty", "FinNifty"])
        description = st.text_area(f"Description for Set No{selected_set_no}", height=100)

# Main app
def main():
    st.set_page_config(layout="wide")
    st.title("My Streamlit Dashboard")

    # Create Strategy Page
    create_strategy_page()

if __name__ == "__main__":
    main()
