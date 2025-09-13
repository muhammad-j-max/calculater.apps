import streamlit as st

st.set_page_config(page_title="Simple Calculator App", page_icon="🧮")

st.title("🧮 Simple Calculator App")

# Sidebar for calculator selection
calc_type = st.sidebar.selectbox(
    "Choose Calculator",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

# User inputs
num1 = st.number_input("Enter first number", value=0.0, step=1.0)
num2 = st.number_input("Enter second number", value=0.0, step=1.0)

# Calculation
if calc_type == "Addition":
    result = num1 + num2
elif calc_type == "Subtraction":
    result = num1 - num2
elif calc_type == "Multiplication":
    result = num1 * num2
elif calc_type == "Division":
    if num2 == 0:
        st.error("Cannot divide by zero!")
        result = None
    else:
        result = num1 / num2

# Show result
if result is not None:
    st.success(f"Result of {calc_type}: {result}")
