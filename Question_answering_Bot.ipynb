{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "50fee931-8cb2-4f4b-8b92-658486d887ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "from langchain.agents import AgentExecutor,AgentType,initialize_agent,load_tools\n",
    "from langchain import HuggingFaceHub\n",
    "import streamlit as st\n",
    "from langchain.callbacks import StreamlitCallbackHandler"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "94abe834-eb24-488a-ba82-869ba0e81287",
   "metadata": {},
   "outputs": [],
   "source": [
    "os.environ[\"HUGGINGFACEHUB_API_TOKEN\"] = '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'\n",
    "def agent_load()->AgentExecutor:\n",
    "    llm = HuggingFaceHub(repo_id=\"t5-small\",\n",
    "model_kwargs={\"temperature\":0, \"max_length\":180})\n",
    "    tools=load_tools(tool_names=[\"wikipedia\"],llm=llm)\n",
    "    return initialize_agent(tools=tools,llm=llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)\n",
    " \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "4f3f1a4d-2950-49a4-9740-972dd1b6c08f",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\akmet\\anaconda3\\Lib\\site-packages\\langchain_core\\_api\\deprecation.py:119: LangChainDeprecationWarning: The function `initialize_agent` was deprecated in LangChain 0.1.0 and will be removed in 0.3.0. Use Use new agent constructor methods like create_react_agent, create_json_agent, create_structured_chat_agent, etc. instead.\n",
      "  warn_deprecated(\n"
     ]
    }
   ],
   "source": [
    "chain=agent_load()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "32b71086-a955-4a75-8aa3-54a783208563",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-05-07 15:12:28.885 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\akmet\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "from langchain.callbacks.streamlit import StreamlitCallbackHandler\n",
    "\n",
    "\n",
    "\n",
    "st.title(\"AI Chat Assistant\")\n",
    "\n",
    "\n",
    "if prompt := st.chat_input(\"Ask me anything...\"):\n",
    "    st.chat_message(\"user\").write(prompt)\n",
    "\n",
    "    with st.chat_message(\"assistant\"):\n",
    "        st_callback = StreamlitCallbackHandler(st.container())\n",
    "        response = chain.run(prompt, callbacks=[st_callback])\n",
    "        st.write(response)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
