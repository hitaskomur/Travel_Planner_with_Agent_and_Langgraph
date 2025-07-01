# ✈️ AI Travel Planner
This project is an AI-powered travel planner that generates personalized day-trip itineraries based on a user-specified city and interests. The application features a user-friendly web interface built with Streamlit and leverages a LangGraph-managed workflow to generate plans via the Groq API.
![Ekran görüntüsü 2025-07-01 115657](https://github.com/user-attachments/assets/c566d13a-94a9-413a-93bc-13c3a13de241)

## 🚀 Key Features
User-Friendly Interface: A simple and interactive web UI built with Streamlit.
Personalized Itineraries: Creates custom travel plans tailored to the destination city and user's interests (e.g., art, museums, coffee).
Fast Generation: Leverages the speed of the Groq API to generate plans in seconds.
Modular Workflow: Built with LangGraph for a manageable and scalable backend workflow.
## 🛠️ Setup
Follow these steps to run the project on your local machine.
Clone the Repository:
Generated bash
git clone https://github.com/Travel_Planner_with_Agent_and_Langgraph
.git
cd Travel_Planner_with_Agent_and_Langgraph
Use code with caution.
Bash
Create and Activate a Virtual Environment (Recommended):
Generated bash
### Windows
python -m venv venv
venv\Scripts\activate

### macOS / Linux
python3 -m venv venv
source venv/bin/activate
Use code with caution.
Bash
Install Dependencies:
All required packages are listed in the requirements.txt file. You can install them with a single command:
Generated bash
pip install -r requirements.txt
Use code with caution.
Bash
⚠️ Important: Set Up Your API Key
For the application to work, you must add your own Groq API key to the main.py file. The application will fail with an error if the API key is missing or invalid.
Open the main.py file.
Locate the following line:
Generated python
os.environ["GROQ_API_KEY"] = "your_api_key"
Use code with caution.
Python
Replace the placeholder key (gsk_...) with your own Groq API key.
## 🏃‍♀️ Running the Application
Once you have completed the setup steps, run the following command in your terminal to start the application:
Generated bash
streamlit run main.py
Use code with caution.
Bash
A new tab will automatically open in your browser, and you can start using the AI Travel Planner.
