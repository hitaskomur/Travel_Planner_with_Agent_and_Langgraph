import os
from langgraph.graph import StateGraph , START, END
from typing import TypedDict , Dict, List, Annotated
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from IPython.display import display,Image

import streamlit as st

os.environ["GROQ_API_KEY"] = "your_api_key"
model="meta-llama/llama-4-scout-17b-16e-instruct"

llm = ChatGroq(model=model)
try:

    llm = ChatGroq(model=model) 
except (KeyError, ImportError):
    st.error("Couldn't find GROQ API KEY. Please check it.")
    st.stop()



class PlannerState(TypedDict):
    messages: Annotated[List[HumanMessage | AIMessage], "Chat History"]
    city: str
    interests: List[str]
    itinerary: str


itinerary_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful travel assistant. Create a day trip itinerary for {city} based on the user's interests: {interests}. Provide a brief, bulleted itinerary."),
    ("human", "Create an itinerary for my day trip.")
])


chain = itinerary_prompt | llm


def create_itinerary(state: PlannerState) -> PlannerState:

    with st.spinner(f"Creating a perfect plan for {state['city']}..."):
        response = chain.invoke({
            "city": state["city"],
            "interests": ", ".join(state["interests"])
        }).content


    return {
        **state,
        "messages": state["messages"] + [AIMessage(content=response)],
        "itinerary": response,
    }


workflow = StateGraph(PlannerState)


workflow.add_node("create_itinerary", create_itinerary)
workflow.add_edge(START, "create_itinerary")
workflow.add_edge("create_itinerary", END)

app = workflow.compile()





st.set_page_config(page_title="AI Travel Planner", page_icon="🌍")
st.title("✈️ AI Travel Planner")
st.markdown("Specify the city you will go to and your interests, and I will prepare a daily trip plan specifically for you!")


if "itinerary" not in st.session_state:
    st.session_state.itinerary = ""


with st.form("planner_form"):

    city = st.text_input("Which city you want to visit?", placeholder="Ex: Paris")

 
    interests_str = st.text_input("What is your interests? (comma-seperated)", placeholder="Ex: art, museum, coffee")


    submitted = st.form_submit_button("Make a plan!")


if submitted:
 
    if not city or not interests_str:
        st.warning("Please type city name and interests.")
    else:
 
        interests_list = [interest.strip() for interest in interests_str.split(",")]


        initial_state = {
            "messages": [HumanMessage(content=f"Make a plan for {city} and depends on user interests: {interests_str} ")],
            "city": city,
            "interests": interests_list,
            "itinerary": "",
        }

 
        final_state = app.invoke(initial_state)


        st.session_state.itinerary = final_state.get("itinerary", "An error occured when making plan.")



if st.session_state.itinerary:
    st.divider()
    st.subheader("Here is your trip plan:", anchor=False)
    st.markdown(st.session_state.itinerary)