import streamlit as st

def main():
    st.title("Calculator Table From View")

    # Create form for selecting products
    st.header("Select Products")
    exchange = st.selectbox("Exchange", options=[], key="exchange")
    product = st.selectbox("Ticker", options=[], key="product")
    next_button = st.button("Next")

    if next_button:
        st.header("Select Instruments")

        # Hide/show based on 'Next' button click
        col1, col2 = st.beta_columns(2)
        with col1:
            segment = st.selectbox("Segment", options=[], key="segment")
            expiry = st.selectbox("Expiry", options=[], key="expiry")
            strike = st.selectbox("Strike", options=[], key="strike")
            option_type = st.selectbox("Type", options=["Call", "Put"], key="optionType")
        with col2:
            side = st.radio("Side", ["Buy", "Sell"], index=0)
            quantity = st.number_input("Quantity", value=1, step=1, key="qty", min_value=1)
            lot_size = 750  # Replace with your actual lot size
            st.warning(f"Make sure you enter a quantity with a multiple of {lot_size}")

        add_button = st.button("Add", key="addItem")
        if add_button:
            # Add logic to store the selected instrument
            pass  # Placeholder for storing the instrument

if __name__ == "__main__":
    main()
