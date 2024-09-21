import streamlit as st
from agents.orchestrator import Orchestrator

def main():
    st.title("Enterprise AI Assistant")

    # Initialize orchestrator
    orchestrator = Orchestrator()

    user_input = st.text_input("Ask your question:")

    if st.button("Submit"):
        if user_input:
            # Process the query using the orchestrator
            response = orchestrator.process_query(user_input)
            st.write("Response:", response)
        else:
            st.write("Please enter a question.")

if __name__ == "__main__":
    main()
