from langchain_core.prompts.prompt import PromptTemplate

GEN_SQL_PROMPT = PromptTemplate.from_template(
    """
    You are a PostgreSQL expert. Given an input question, first create a syntactically correct PostgreSQL query to run, then look at the results of the query and return the answer to the input question.
    Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per PostgreSQL. You can order the results to return the most informative data in the database.
    Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in double quotes (") to denote them as delimited identifiers.
    Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
    Pay attention to use CURRENT_DATE function to get the current date, if the question involves "today".
    
    Use the following format to return:
    ```sql
    write sql here
    ```
    
    Only use the following tables:
    {table_info}
    Each table is associated with a subject using EIS_ID
    
    Use the Chat history as a reference:
    {chat_history}
    
    Question: {question}
   """
)

ANSWER_PROMPT = PromptTemplate.from_template(
    """
    Given the following user question, corresponding SQL query, and SQL result, answer the user question.
    Question: {question}
    SQL Query: {query_sql}
    Table Info:{table_info}
    SQL Result: {query_result}
    
    Pay attention to answer in Chinese!The data in 'SQL Query' or 'SQL Result' do not need to be translated into Chinese.
    Pay attention to use COMMENT as a table header.
    If you need a table display, please return it in markdown format.
    Pay attention to use 'COMMENT' as a table header.
    """
)
