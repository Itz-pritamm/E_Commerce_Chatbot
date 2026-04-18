from groq import Groq
import os
import re
import sqlite3
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

GROQ_MODEL = os.getenv('GROQ_MODEL')

db_path = Path(__file__).parent / "db.sqlite"

client_sql = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ---------------- SQL PROMPT ---------------- #
sql_prompt = """You are an expert in understanding the database schema and generating SQL queries for a natural language question asked
pertaining to the data you have.

<schema> 
table: product 

fields: 
product_link - string	
title - string	
brand - string	
price - integer	
discount - float	
avg_rating - float	
total_ratings - integer
</schema>

Use LOWER() with LIKE for text matching.
Always return SQL inside <SQL></SQL> tags.
"""

# ---------------- SQL GENERATION ---------------- #
def generate_sql_query(question):
    chat_completion = client_sql.chat.completions.create(
        messages=[
            {"role": "system", "content": sql_prompt},
            {"role": "user", "content": question}
        ],
        model=GROQ_MODEL,
        temperature=0.2,
        max_tokens=300
    )
    return chat_completion.choices[0].message.content


# ---------------- RUN SQL ---------------- #
def run_query(query):
    if query.strip().upper().startswith('SELECT'):
        with sqlite3.connect(db_path) as conn:
            df = pd.read_sql_query(query, conn)
            return df


# ---------------- DATA COMPREHENSION ---------------- #
def data_comprehension(question, df):

    if df is None or df.empty:
        return "No results found."

    # 🔥 CRITICAL FIX: LIMIT DATA
    df = df.head(3)  # only 3 rows

    # 🔥 Select only required columns
    columns_to_use = ['title', 'price', 'discount', 'avg_rating', 'product_link']
    df = df[[col for col in columns_to_use if col in df.columns]]

    # Convert to small readable text
    context = df.to_string(index=False)

    # Extra safety (token limit)
    context = context[:1500]

    prompt = f"""
Answer the question using the data below.

Question: {question}

Data:
{context}

Rules:
- Show results in list format
- Include title, price, discount, rating, and link
- Keep it simple and clean
"""

    chat_completion = client_sql.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model=GROQ_MODEL,
        max_tokens=300
    )

    return chat_completion.choices[0].message.content


# ---------------- MAIN CHAIN ---------------- #
def sql_chain(question):
    sql_query = generate_sql_query(question)

    pattern = "<SQL>(.*?)</SQL>"
    matches = re.findall(pattern, sql_query, re.DOTALL)

    if len(matches) == 0:
        return "Sorry, could not generate SQL query."

    query = matches[0].strip()
    print("Generated SQL:", query)

    df = run_query(query)

    if df is None:
        return "SQL execution failed."

    # 🔥 PASS DATAFRAME DIRECTLY (NOT dict)
    answer = data_comprehension(question, df)

    return answer


# ---------------- TEST ---------------- #
if __name__ == "__main__":
    question = "Show top 3 shoes in descending order of rating"
    answer = sql_chain(question)
    print(answer)
