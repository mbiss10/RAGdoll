from flask import Flask, request, render_template
from single_qa_agent import SingleQaAgent
import json

app = Flask(__name__)

class InteractiveAgentSession():
    def __init__(self):
        self.agent = SingleQaAgent("./data/dev_david/db_cs_with_sources.pkl",
                          temperature=0, num_docs_to_retrieve=7)

    def ask_agent(self, req):
        # Adds data from python client request
        try:
            question = req.get_json().get('question')
            response = self.agent.ask(question)
            return json.dumps({'status' : 200, 'success' : response.get('output_text')})
        except:
            print("Unable to get client data.")
            return json.dumps({'status' : 500, 'success' : "Internal Server Error"})


session = InteractiveAgentSession()

@app.route('/agent', methods=['POST'])
def api_agent_ask():
    return session.ask_agent(request)


