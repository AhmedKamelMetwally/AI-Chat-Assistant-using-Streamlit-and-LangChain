from langchain.agents import AgentExecutor,AgentType,initialize_agent,load_tools
from langchain import HuggingFaceHub
import streamlit as st
from langchain.callbacks import StreamlitCallbackHandler
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = st.secrets["HUGGINGFACEHUB_API_TOKEN"]
def agent_load()->AgentExecutor:
    llm = HuggingFaceHub(repo_id="t5-small",
model_kwargs={"temperature":0, "max_length":180})
    tools=load_tools(tool_names=["wikipedia"],llm=llm)
    return initialize_agent(tools=tools,llm=llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)
chain=agent_load()

st_callback = StreamlitCallbackHandler(st.container())



if prompt := st.chat_input():
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(st.container())
        response = chain.run(prompt, callbacks=[st_callback])
        st.write(response)
