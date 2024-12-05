import os
import streamlit as st
from PIL import Image
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Set up the API key for Google Gemini 1.5 Flash model
api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

# Streamlit app setup
st.set_page_config(page_title="Invoice Extractor", page_icon="📄")
st.title("Invoice Extractor Using Gemini 1.5 Flash Model")

# File uploader for invoice images
uploaded_file = st.file_uploader("Upload an invoice image (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

# Function to process and extract specific information using Google Gemini 1.5 Flash API
def extract_invoice_data_from_image(image):
    try:
        # Define the prompt to ask the model about specific invoice details
        prompt = """
        You are an expert in understanding invoices. I need you to extract the following details:
        - Invoice Number
        - Date
        - Total Amount
        - Number of items
        - Supplier name
        
        Please extract the relevant details and provide only the required information.
        """

        # Send the image to Gemini 1.5 Flash model for content generation
        model = genai.GenerativeModel('gemini-1.5-flash')  # Use gemini-1.5-flash
        response = model.generate_content([image, prompt])

        # Print the entire response to help debug
        print("Full Response from Gemini:", response)

        # Access the response content
        if response and len(response.candidates) > 0:
            candidate = response.candidates[0]
            content = candidate.content.parts[0].text

            # Now let's parse the content to extract individual fields
            extracted_data = {}
            for line in content.split("\n"):
                if line.startswith("-"):
                    key, value = line[2:].split(":", 1)
                    extracted_data[key.strip()] = value.strip()

            return extracted_data

        else:
            return "No relevant information detected in the image."

    except Exception as e:
        return f"Error: {e}"

# If an image is uploaded
if uploaded_file is not None:
    # Open the image using PIL for display
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Invoice Image", use_container_width=True)  # Updated to use_container_width
    
    # Extract specific details from the image using the Gemini 1.5 Flash API
    extracted_data = extract_invoice_data_from_image(image)  # Passing the PIL Image instead of bytes
    
    # Display extracted information
    st.subheader("Extracted Information:")
    if isinstance(extracted_data, dict):
        for key, value in extracted_data.items():
            st.write(f"**{key}:** {value}")
    else:
        st.write(extracted_data)

else:
    st.info("Please upload an invoice image to extract the data.")
