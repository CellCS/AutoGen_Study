#https://python.langchain.com/docs/get_started/quickstart/
#export OPENAI_API_KEY="..."

from langchain_openai import ChatOpenAI
llm = ChatOpenAI()

prompt_value=llm.invoke("give me one project name about data insight for a clinical trial study")
print(prompt_value)

from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a clinical trial study admin"),
    ("user", "{input}")
])
chain = prompt | llm
prompt_value=chain.invoke({"input": "how many standards for clinical trial study?"})
print(prompt_value)


from langchain_core.output_parsers import StrOutputParser
output_parser = StrOutputParser()
chain = prompt | llm | output_parser
prompt_value=chain.invoke({"input": "how many standards for clinical trial study?"})
print(prompt_value)