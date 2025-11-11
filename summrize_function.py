#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from dotenv import load_dotenv


# In[2]:


import openai


# In[4]:


#coonnect to Open ai
load_dotenv()
Open_Ai_Key=os.getenv('OpenAiKey')
print('Connected' if Open_Ai_Key  else 'fail')


# In[6]:


#write the prompt to the llm
openai.api_key=Open_Ai_Key
#send req
def summarize(msg):
    try:
        response = openai.ChatCompletion.create(
            model='gpt-4',
            messages=[
                {"role": "system",
                 "content": "Summarize the user feedback messages with max 5 words for each message, be concise, identify the problem."},
                {"role": "user", "content": f"{msg}"}
            ],
            max_tokens=30,
            temperature=0.3
        )

        summaries = response['choices'][0]['message']['content']  # extract response
        return summaries

    except Exception as err:
        print("Error:", err)
        return None


# In[18]:


messages=['the system loggs me out whenever i log in in certin hours idk why so frusutrting!!!!!!!!!!!!','idk where the log out button is?']
summries=[]
for idx,msg in enumerate(messages):
    
    summrized_message=summarize(msg)
    summries.append((idx+1,summrized_message))

for idx, summary in enumerate(summries):
    print(f"Message {idx}: {summary[1]}")

    

