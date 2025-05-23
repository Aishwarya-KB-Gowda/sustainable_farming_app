# 🌾 Farmer Advisor Agentic AI System

A Smart Farming Assistant powered by Agentic AI and Machine Learning to help farmers make informed decisions about crop yield predictions and market prices using AI-driven insights.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.15.0-red)](https://streamlit.io/)
[![CrewAI](https://img.shields.io/badge/CrewAI-0.1.5-green)](https://github.com/crewai/crewai)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.2.0-orange)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🚀 Project Overview

This project solves **Problem Statement 3: Data-Driven AI for Sustainable Farming** using an innovative multi-agent AI system. It supports farmers by providing:

- **Crop yield predictions** based on weather and soil data.
- **Market price predictions** for crops using economic indicators.
- **Intelligent recommendations** from two AI agents: `FarmerAdvisor` and `MarketResearcher`.

---

## 🧠 Technologies Used

| Category              | Tools / Libraries                        |
|-----------------------|------------------------------------------|
| **Frontend**          | Streamlit                                |
| **ML Models**         | Random Forest (Scikit-learn)             |
| **Agents**            | CrewAI with Ollama API (Gemma 2B model)  |
| **Database**          | SQLite                                   |
| **Backend Logic**     | Python                                   |
| **Data Sources**      | CSV files for training datasets          |
| **Integration**       | Scweu AI to link AI agents seamlessly    |

---

## 📁 Project Structure

```
FARMER_ADVISOR_AGENTIC_AI/
├── agents/
│   ├── farmer_advisor.py
│   └── market_researcher.py
├── database/
│   ├── save_results.py
│   └── sustainable_farming.db
├── models/
│   ├── ml_model1.py
│   └── ollama_inference.py
├── app.py
├── app1.py
├── crewai_manager.py
├── farmer_advisor_dataset.csv
├── market_researcher_dataset.csv
├── requirements.txt
└── README.md
```

---

## 🔍 Key Components

- `app1.py`: Streamlit UI to interact with the system.
- `crewai_manager.py`: Coordinates the agents and ML model responses.
- `ml_model1.py`: Houses crop yield and market price prediction models.
- `farmer_advisor.py`: AI Agent that gives farming suggestions.
- `market_researcher.py`: AI Agent analyzing market trends.
- `ollama_inference.py`: Handles interaction with the Ollama API.
- `save_results.py`: Saves results and recommendations to SQLite DB.

---

## 🧪 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Farmer-Advisor-Agentic-AI.git
   cd Farmer-Advisor-Agentic-AI
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app1.py
   ```

## 📊 Sample Output

✅ Predicted crop yield: 23.5 tons per hectare  
✅ Market price suggestion: ₹19/kg  
✅ Agent Advice: "Based on current soil and weather conditions, consider using drip irrigation for better efficiency..."

## 🏆 Highlights

- 🧠 Used Agentic AI for explainable and interactive decision-making.
- 🤖 Integrated LLMs (Gemma 2B via Ollama) for natural language insights.
- 🛠️ Built a modular, scalable AI architecture with real-world application potential.

## 📌 Future Scope

- 🌿 Add more agents (e.g., Pest Control Advisor)
- ☁️ Integrate weather APIs for real-time prediction
- 📱 Deploy on cloud with a mobile-friendly UI

## 👥 Contributors

- [Your Name](https://github.com/yourusername)
- [Team Member 1](https://github.com/teammember1)
- [Team Member 2](https://github.com/teammember2)

## 🎥 Demo

Check out our [demo video](https://youtu.be/your-demo-link) to see the Farmer Advisor Agentic AI System in action!

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 