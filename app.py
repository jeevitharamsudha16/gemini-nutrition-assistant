from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Set up API key for Gemini
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("API Key is missing. Please set GOOGLE_API_KEY in your environment.")
else:
    genai.configure(api_key=api_key)

# Function to get the response from the Gemini model
def get_gemini_response(image_data, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([prompt, image_data[0]])
    return response.text

# Function to process the uploaded image
def process_image(uploaded_file):
    if uploaded_file:
        image_bytes = uploaded_file.getvalue()
        return [{"mime_type": uploaded_file.type, "data": image_bytes}]
    else:
        raise FileNotFoundError("No image uploaded")

# Set up Streamlit app configuration
st.set_page_config(page_title="Gemini Health App")
st.header("Gemini Health App 🍏")

# Input for user-specific details and meal image upload
user_input = st.text_input("Describe the meal or food (optional):", key="input")
uploaded_file = st.file_uploader("Upload a meal image", type=["jpg", "jpeg", "png"])

# Show the uploaded image
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Prompt for the Gemini model to process the image and text
nutrition_prompt = """
You are an experienced nutritionist. From the uploaded food image, please:
1. Identify all the visible food items and estimate their calorie count.
2. List each item with its estimated calorie content in the following format:
   - Item 1 - X calories
   - Item 2 - Y calories
3. At the end, provide the **total calorie count** for all items combined.
4. Additionally, evaluate whether the food items are generally good or bad for health based on their calorie count and nutritional content.
   - If an item is high in calories, suggest whether it's a healthy choice or not.
   - If an item is low in calories, suggest if it's beneficial for a healthy diet.
   - Provide tips for improving the meal's nutritional value (e.g., adding more vegetables, switching to low-fat options).
"""

# Button to trigger the calorie count prediction
if st.button("Calculate Total Calories 🍽️"):
    try:
        image_data = process_image(uploaded_file)
        result = get_gemini_response(image_data, nutrition_prompt)
        st.subheader("Calories and Health Analysis Result 🧠:")
        st.write(result)
    except FileNotFoundError:
        st.error("Please upload an image first.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
