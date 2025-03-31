import os
from dotenv import load_dotenv
from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.playground import Playground, serve_playground_app

# Load environment variables
load_dotenv()

# Set Groq API key in the environment
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    groq_api_key = "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"
    os.environ["GROQ_API_KEY"] = groq_api_key  # This ensures it's available in the environment

# Farmer Advisor - Using a more stable approach with string ID
farmer_advisor_agent = Agent(
    name="Farmer Advisor",
    role="Analyze soil, crop suitability, and financial goals for sustainable farming.",
    model="llama3-groq-70b-8192-tool-use-preview",  # String ID instead of object
    instructions=[
        "Provide precise crop recommendations based on soil data.",
        "Include specific varieties suitable for the conditions.",
        "Consider sustainability and profitability in recommendations."
    ],
    show_tool_calls=True,
    markdown=True,
)

# Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search for current agricultural data and market trends.",
    model="llama3-groq-70b-8192-tool-use-preview",  # String ID instead of object
    tools=[DuckDuckGo()],
    instructions=[
        "Search for relevant farming information.",
        "Find current market prices for agricultural products.",
        "Research sustainable farming practices."
    ],
    show_tool_calls=True,
    markdown=True,
)

# Create the playground with just two agents to reduce complexity
app = Playground(
    agents=[farmer_advisor_agent, web_search_agent]
).get_app()

# Run the playground app
if __name__ == "__main__":
    print("\n===== SUSTAINABLE FARMING AI ADVISOR =====")
    print("Starting playground app...")
    print("Once started, open your browser at http://localhost:8501\n")
    try:
        serve_playground_app("playground:app", reload=True)
    except Exception as e:
        print(f"\nError starting playground: {e}")
        print("\nTroubleshooting tips:")
        print("1. Check if the GROQ_API_KEY is valid and has sufficient quota")
        print("2. Try updating phidata: pip install -U phidata")
        print("3. Ensure you have all required dependencies installed")