import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq

# Load environment variables
load_dotenv()

# Set Groq API key in the environment
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    groq_api_key = "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"
    os.environ["GROQ_API_KEY"] = groq_api_key

# Create Groq client
client = Groq(api_key=groq_api_key)

# Define agent system prompts
FARMER_ADVISOR_PROMPT = """
You are a Farmer Advisor. Your role is to analyze soil, crop suitability, and financial goals for sustainable farming.

Instructions:
- Provide precise crop recommendations based on soil data.
- Include specific varieties suitable for the conditions.
- Consider sustainability and profitability in recommendations.
"""

WEB_SEARCH_PROMPT = """
You are a Web Search Agent. Your role is to search for current agricultural data and market trends.

Instructions:
- Search for relevant farming information.
- Find current market prices for agricultural products.
- Research sustainable farming practices.
"""

# Create a simple Streamlit app
st.title("Sustainable Farming AI Advisor")
st.write("Ask questions about soil analysis, crop recommendations, or sustainable farming practices.")

# Create tabs for different agents
tab1, tab2 = st.tabs(["Farmer Advisor", "Web Search Agent"])

with tab1:
    st.header("Farmer Advisor")
    st.write("Ask about crop recommendations, soil analysis, and sustainable farming practices.")
    
    farmer_query = st.text_area("Your question for the Farmer Advisor:", height=100)
    if st.button("Submit to Farmer Advisor"):
        if farmer_query:
            with st.spinner("Generating response..."):
                try:
                    response = client.chat.completions.create(
                        model="llama3-70b-8192",
                        messages=[
                            {"role": "system", "content": FARMER_ADVISOR_PROMPT},
                            {"role": "user", "content": farmer_query}
                        ],
                        temperature=0.7,
                        max_tokens=2048
                    )
                    st.markdown(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please enter a question.")

with tab2:
    st.header("Web Search Agent")
    st.write("Get information about current agricultural trends and market prices.")
    st.warning("Note: This is a simplified version. Real web search functionality requires additional implementation.")
    
    web_query = st.text_area("Your question for the Web Search Agent:", height=100)
    if st.button("Submit to Web Search Agent"):
        if web_query:
            with st.spinner("Generating response..."):
                try:
                    search_instruction = f"The user wants to know about: {web_query}\nProvide information as if you had searched for this agricultural topic online."
                    response = client.chat.completions.create(
                        model="llama3-70b-8192",
                        messages=[
                            {"role": "system", "content": WEB_SEARCH_PROMPT},
                            {"role": "user", "content": search_instruction}
                        ],
                        temperature=0.7,
                        max_tokens=2048
                    )
                    st.markdown(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please enter a question.")

# Add information footer
st.divider()
st.write("This is a simplified version of the Sustainable Farming AI Advisor.")
st.write("For more advanced features, consider implementing custom tools and agent capabilities.")

# Run the app
if __name__ == "__main__":
    # This is handled by Streamlit's CLI
    print("\n===== SUSTAINABLE FARMING AI ADVISOR =====")
    print("Starting playground app...")
    print("Run this with: streamlit run filename.py")
    print("Once started, open your browser at the URL displayed in the terminal\n")