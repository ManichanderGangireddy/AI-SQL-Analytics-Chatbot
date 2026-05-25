import streamlit as st
import os

from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_google_genai import ChatGoogleGenerativeAI

# ==========================================
# PAGE TITLE
# ==========================================

st.title("Enterprise SQL AI Chatbot 🤖")

# ==========================================
# ENTER API KEY
# ==========================================

api_key = st.text_input(
    "Enter Gemini API Key",
    type="password"
)

# ==========================================
# RUN ONLY IF API KEY EXISTS
# ==========================================

if api_key:

    # Set API key
    os.environ["GOOGLE_API_KEY"] = "AIzaSyDscEpoc1JTTWpL8nPwD4oX_3okJHGM-UQ"
    #" YOUR_API_KEY"

    try:

        # ==========================================
        # CONNECT DATABASE
        # ==========================================

        db = SQLDatabase.from_uri(
            "sqlite:///enterprise_sales.db"
        )

        # ==========================================
        # SEMANTIC LAYER
        # ==========================================

        semantic_layer = """
        You are a data analyst working with a SQL database.

        Business Definitions:
        - Profit = revenue - cost_to_build

        Table Relationships:
        - sales.product = products.product_name
        - sales.customer_id = customers.customer_id

        Rules:
        - Always use JOIN when needed
        - Only consider completed orders when asked
        """

        # ==========================================
        # GEMINI MODEL
        # ==========================================

        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0
        )

        # ==========================================
        # CREATE SQL AGENT
        # ==========================================

        agent_executor = create_sql_agent(
            llm=llm,
            db=db,
            agent_type="tool-calling",
            verbose=True,
            max_iterations=5,
            prefix=semantic_layer
        )

        # ==========================================
        # USER QUESTION
        # ==========================================

        question = st.text_input(
            "Ask a business question"
        )

        # ==========================================
        # GET RESPONSE
        # ==========================================

        if question:

            with st.spinner("Thinking..."):

               response = agent_executor.invoke({"input": question})
               st.subheader("🤖 AI Response")
               output = response["output"]
               if isinstance(output, list):
                try:
                        clean_text = output[0]["text"]
                        st.write(clean_text)
                except:
                    st.write(output)

                else:
                    st.write(output)
    except Exception as e:
        st.error(f"Error:{e}")   
                    