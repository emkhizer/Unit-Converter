import streamlit as st

# Define a dictionary of unit conversions for each category
unit_conversions = {
    "Length": {
        "Meter": 1, "Kilometer": 1000, "Centimeter": 0.01, "Millimeter": 0.001,
        "Mile": 1609.34, "Yard": 0.9144, "Foot": 0.3048, "Inch": 0.0254
    },
    "Mass": {
        "Kilogram": 1000, "Gram": 1, "Milligram": 0.001, "Pound": 453.592,
        "Ounce": 28.3495, "Ton": 1000000
    },
    "Temperature": {
        "Celsius": 1, "Fahrenheit": 1, "Kelvin": 1
    },
    "Volume": {
        "Liter": 1, "Milliliter": 0.001, "Gallon": 3.78541, "Quart": 0.946353,
        "Pint": 0.473176, "Cup": 0.236588, "Fluid Ounce": 0.0295735
    },
    "Speed": {
        "Meters/second": 1, "Kilometers/hour": 0.277778, "Miles/hour": 0.44704, "Knot": 0.514444
    },
    "Time": {
        "Second": 1, "Minute": 60, "Hour": 3600, "Day": 86400, "Week": 604800,
        "Month": 2592000, "Year": 31536000
    },
    "Area": {
        "Square Meter": 1, "Square Kilometer": 1000000, "Square Mile": 2589988.11,
        "Square Yard": 0.836127, "Square Foot": 0.092903, "Acre": 4046.86, "Hectare": 10000
    },
    "Data": {
        "Bit": 0.125, "Byte": 1, "Kilobyte": 1024, "Megabyte": 1048576,
        "Gigabyte": 1073741824, "Terabyte": 1099511627776
    }
}

def convert_to_base(value, unit, category):
    """Convert input value to base unit."""
    conversions = unit_conversions.get(category, {})
    return value * conversions.get(unit, 1)

def convert_from_base(base_value, unit, category):
    """Convert base value to target unit."""
    conversions = unit_conversions.get(category, {})
    return base_value * (1 / conversions.get(unit, 1))

def convert_temperature(value, from_unit, to_unit):
    """Handle temperature conversion separately."""
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    return value

# Streamlit app code
def app():
    # Add custom CSS for vibrant, modern look
    st.markdown("""
        <style>
            body {
                background: linear-gradient(45deg, #ff416c, #ff4b2b);
                font-family: 'Helvetica Neue', sans-serif;
                color: #fff;
                padding: 0;
                margin: 0;
            }
            .stButton>button {
                background-color: #ff416c;
                color: white;
                font-size: 18px;
                font-weight: bold;
                padding: 12px 24px;
                border-radius: 8px;
                border: none;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
                cursor: pointer;
                transition: background-color 0.3s ease, transform 0.2s ease;
            }
            .stButton>button:hover {
                background-color: #ff4b2b;
                transform: translateY(-2px);
            }
            .stSelectbox>div, .stTextInput>div, .stNumberInput>div {
                background-color: rgba(255, 255, 255, 0.2);
                border-radius: 8px;
                border: none;
                padding: 10px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
            }
            .stSelectbox>div:hover, .stTextInput>div:hover, .stNumberInput>div:hover {
                background-color: rgba(255, 255, 255, 0.3);
            }
            h1, h2 {
                text-align: center;
                font-weight: 700;
            }
            h1 {
                font-size: 3rem;
            }
            h2 {
                font-size: 1.5rem;
            }
            .stTextInput input, .stNumberInput input {
                background-color: rgba(255, 255, 255, 0.4);
                border: none;
                border-radius: 8px;
                padding: 12px;
                color: #fff;
                font-size: 18px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.title("Vibrant Unit Converter")

    # Category selector
    category = st.selectbox("Select Conversion Category", 
                            ["Length", "Mass", "Temperature", "Volume", "Speed", "Time", "Area", "Data"])

    # Select units
    units = list(unit_conversions.get(category, {}).keys())
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    
    # Input value
    value = st.number_input("Value to Convert", value=1.0, format="%.6f")
    
    if st.button("Convert"):
        try:
            if category == "Temperature":
                result = convert_temperature(value, from_unit, to_unit)
            else:
                base_value = convert_to_base(value, from_unit, category)
                result = convert_from_base(base_value, to_unit, category)
            st.success(f"Converted Value: {result:.6f} {to_unit}")
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    app()
