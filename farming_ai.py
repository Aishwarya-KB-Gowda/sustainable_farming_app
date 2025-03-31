import os
from dotenv import load_dotenv
import requests
import json

# Load API keys
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# If environment variable isn't working, use the direct key
if not groq_api_key:
    groq_api_key = "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"

# Function to call Groq API directly
def ask_groq(prompt, model="llama3-70b-8192"):
    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful farming advisor who specializes in sustainable agriculture. Provide specific recommendations based on soil, weather, and market conditions."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 1000
    }
    
    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=data
        )
        
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error occurred: {str(e)}"

# Main function to get farming advice
def get_farming_advice(soil_ph, rainfall_mm):
    prompt = f"""
    As a team of agricultural experts, please provide comprehensive advice on:
    
    1. What are the best crops to grow given soil pH of {soil_ph} and upcoming rainfall of {rainfall_mm}mm?
    2. How should I prepare the soil and manage irrigation with this rainfall amount?
    3. Which crops would be most profitable in current market conditions with these growing parameters?
    4. What sustainable farming practices would you recommend for these conditions?
    
    Please provide specific crop recommendations with your reasoning.
    """
    
    return ask_groq(prompt)

# Run the advisor
if __name__ == "__main__":
    print("Sustainable Farming Advisor")
    print("---------------------------")
    
    # Get advice for the specified parameters
    advice = get_farming_advice(6.5, 200)
    print("\nFarming Recommendations:")
    print(advice)
    
    # Allow for additional questions
    while True:
        print("\nAsk another question or type 'exit' to quit:")
        question = input("> ")
        if question.lower() == 'exit':
            break
        
        answer = ask_groq(question)
        print(answer)