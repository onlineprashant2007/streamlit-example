import streamlit as st
from streamlit import SessionState

# Function to create the "Create Strategy" page
def create_strategy_page(session_state):
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
        # Save the strategy to the session state
        if "saved_strategies" not in session_state:
            session_state.saved_strategies = []
        session_state.saved_strategies.append({
            "strategy_name": strategy_name,
            "tags": tags,
            "description": description,
        })

    # Display saved strategies
    if "saved_strategies" in session_state and len(session_state.saved_strategies) > 0:
        st.header("My Strategies")
        for i, strategy in enumerate(session_state.saved_strategies):
            st.write(f"### Strategy {i + 1}")
            st.write(f"**Strategy Name:** {strategy['strategy_name']}")
            st.write(f"**Tags:** {strategy['tags']}")
            st.write(f"**Description:** {strategy['description']}")

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

    # Create or get the SessionState
    session_state = SessionState.get(saved_strategies=[])

    # Create Strategy Page
    create_strategy_page(session_state)

if __name__ == "__main__":
    main()
