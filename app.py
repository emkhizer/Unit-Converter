import streamlit as st
import random

# Define unit conversions 🔄💡
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
    "Energy": {
        "Joule": 1, "Calorie": 4.184, "Kilowatt-hour": 3600000, "BTU": 1055.06
    },
    "Pressure": {
        "Pascal": 1, "Bar": 100000, "PSI": 6894.76, "mmHg": 133.322
    }
}

# Temperature conversion function 🌡️🔥❄️
def convert_temperature(value, from_unit, to_unit):
    """
    Yeh function sirf temperature ke liye conversion karta hai. 
    Agar category temperature nahi hai to yeh function kaam nahi karega.
    """
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

# General unit conversion function 🔢🔄
def convert_unit(value, from_unit, to_unit, category):
    """
    Yeh function kisi bhi category ke liye unit convert karega. 
    Agar category "Temperature" hai to special function call hoga.
    """
    if category == "Temperature":
        return convert_temperature(value, from_unit, to_unit)
    conversions = unit_conversions.get(category, {})
    base_value = value * conversions.get(from_unit, 1)
    return base_value / conversions.get(to_unit, 1)

# UI Enhancements 🎨✨
st.set_page_config(page_title="Unit Converter 🔄", page_icon="🛠️", layout="centered")
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 10px;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #45a049;
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

# Title and Stickers 🎉📏
st.markdown("<h1 style='text-align: center;'>✨ Ultimate Unit Converter 🚀✨</h1>", unsafe_allow_html=True)
st.image(random.choice(["https://i.imgur.com/6oHf60C.png", "https://i.imgur.com/IljXG6B.png"]), width=150)

# Category Selection 📌
category = st.selectbox("📂 Select a Category", list(unit_conversions.keys()))
units = list(unit_conversions[category].keys())

tab1, tab2 = st.columns(2)
with tab1:
    from_unit = st.selectbox("🔄 From", units)
with tab2:
    to_unit = st.selectbox("➡️ To", units)

# User Input 🔢
value = st.number_input("💡 Enter Value", value=1.0, format="%.6f")

# Convert Button 🚀
if st.button("Convert 🔄✨"):
    try:
        result = convert_unit(value, from_unit, to_unit, category)
        st.success(f"✅ {value} {from_unit} = {result:.6f} {to_unit}")
    except Exception as e:
        st.error(f"⚠️ Conversion error: {e}")
