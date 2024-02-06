from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables
import streamlit as st
import os
import mysql.connector

import google.generativeai as genai

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load google gemini model and provide sql query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrieve query from sql database
def read_sql_query(sql, db_params):
    try:
        # Remove triple backticks if present
        sql = sql.replace('```sql', '').replace('```', '')

        conn = mysql.connector.connect(**db_params)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
    except mysql.connector.Error as err:
        st.error(f"Error executing SQL query: {err}")
        return []


prompt = [
    """
    Converting English questions to SQL queries. 
    The SQL database contains a student table with columns name, class, section, and marks.
    """
]

# Creating Streamlit app
st.set_page_config(page_title="Retrieve SQL Query")
st.header("Using Gemini app to retrieve data")

question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(question, prompt)
    st.subheader("Required SQL Query Response from Gemini:")
    st.write(response)

    db_params = {
        "host": "localhost",
        "user": "root",
        "password": "kiit",
        "database": "project",
    }

    data = read_sql_query(response, db_params)
    st.subheader("Data retrieved from the database:")
    for row in data:
        st.write(row)

