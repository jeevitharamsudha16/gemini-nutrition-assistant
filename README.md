# Gemini-Nutrition-Assistant
**Gemini-Nutrition-Assistant** is an AI-powered web application that helps users analyze the nutritional content of their meals. Using the powerful Google Gemini model, the app can estimate the calorie count of food items from images and provide health evaluations along with practical nutrition improvement tips.
![Alt Text](https://github.com/jeevitharamsudha16/gemini-nutrition-assistant/blob/main/Snip20250612_21.png)

## Features
- **Food Image Upload**: Upload a meal image in JPG, JPEG, or PNG format.
- **Calorie Estimation**: Identifies food items in the image and estimates the calorie content for each item.
- **Health Assessment**: Analyzes whether the food items are healthy based on their calorie count and nutritional content.
- **Nutrition Improvement Tips**: Provides actionable suggestions for making meals healthier, such as adding more vegetables or switching to low-fat alternatives.
- **User Input**: Allows users to provide a text description of the meal for enhanced analysis.

## Technologies Used
- **Streamlit**: For building the interactive user interface.
- **Google Gemini (Generative AI)**: Used for analyzing food images and generating nutritional insights.
- **Python**: The primary language for backend logic and API integration.
- **PIL (Python Imaging Library)**: Handles image processing and display.
- **dotenv**: For managing environment variables (such as API keys).

## Getting Started

### Prerequisites
Make sure you have the following installed:

- Python 3.6 or later
- Streamlit
- Google Generative AI
- Pillow (PIL)
- dotenv

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/gemini-nutrition-assistant.git
   cd gemini-nutrition-assistant
   
2. Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the required dependencies:
pip install -r requirements.txt

4. Set up your Google API Key for accessing Gemini. Create a .env file in the root directory and add your API key:
GOOGLE_API_KEY=your_api_key_here

5. Running the Application
To run the app locally, use the following command:
streamlit run app.py

6. Open your browser and go to the URL provided by Streamlit (usually http://localhost:8501).

### Interact with application
1. **Upload a meal image or describe the meal in the text input.**
   ![Alt Text](https://github.com/jeevitharamsudha16/gemini-nutrition-assistant/blob/main/Snip20250612_22.png)
2. **Click on the "Calculate Total Calories" button.**
3. **The app will process the image and provide the estimated calories, a health evaluation of the meal, and tips for making it healthier.**
   ![Alt Text](https://github.com/jeevitharamsudha16/gemini-nutrition-assistant/blob/main/Snip20250612_23.png)


## Improvements for Gemini-Nutrition-Assistant App
1. Save Meal History: Allow users to store and revisit their past meals.
2. Set Custom Calorie Goals: Let users define their daily calorie intake target.
3. Nutrient Breakdown: Show detailed breakdowns of nutrients (protein, carbs, fats).
4. Healthier Alternatives: Suggest healthier options for high-calorie foods.
5. Recipe Suggestions: Recommend healthy recipes based on the meal items detected.

### Contributing
We welcome contributions to Gemini-Nutrition-Assistant! If you have suggestions for improvements, bug fixes, or new features, feel free to open an issue or submit a pull request.

### Steps to Contribute:
- Fork the repository
- Create a new branch (git checkout -b feature-branch)
- Commit your changes (git commit -m 'Add new feature')
- Push to your forked repository (git push origin feature-branch)
- Create a pull request from your fork to the main repository



