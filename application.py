#!/usr/bin/env python
# coding: utf-8

# In[3]:


from flask import Flask,request,jsonify
from summrize_function import summarize


# In[5]:


# app = Flask(__name__)
# deployable

application = Flask(__name__)

#define route to accept list of messages in req body and retrun responses
@application.route('/Sumrize_messages',methods=['post'])
def handel_requests():
    try:
        #get json body req parse it as json to handel it
        data=request.get_json()
        #Expexting messages array in the object
        messages=data.get('messages',[]) #as list

        results=[]

        for idx,msg in enumerate(messages):
            summery=summarize(msg)
            results.append({"number":idx+1,"summery":summery})#we return json 

        return jsonify({"summries":results}),200 #retrun it as json body
    except Exception as err:
        return jsonify({"error":str(err)}),400

    
# This runs the app when this script is executed
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))  # <- use 8000 for aws bundel 
    application.run(host="0.0.0.0", port=port)


