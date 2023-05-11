from flask import Flask, request, render_template
from single_qa_agent import SingleQaAgent
import json
import prompts

app = Flask(__name__)


class InteractiveAgentSession():
    def __init__(self):
        self.agent = SingleQaAgent("./data/dev_david/db_cs_with_sources.pkl",
                                   model_name="gpt-3.5-turbo",
                                   temperature=0.2,
                                   vectorstore_k=8,
                                   prompt=prompts.TURBO_PROMPT)
        #   passages_path="./data/dev_david/cs_data.pkl",
        #   tfidf_k=8)

    def ask_agent(self, req):
        # Adds data from python client request
        try:
            question = req.get_json().get('question')
            response = self.agent.ask(question)
            return json.dumps({'status': 200, 'success': response.get('output_text')})
        except:
            print("Unable to get client data.")
            return json.dumps({'status': 500, 'success': "Internal Server Error"})


session = InteractiveAgentSession()


@app.route('/agent', methods=['POST'])
def api_agent_ask():
    return session.ask_agent(request)
