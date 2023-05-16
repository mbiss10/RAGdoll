from flask import Flask, request, render_template
from single_qa_agent import SingleQaAgent
from langchain.chat_models import ChatOpenAI
import json
import prompts

app = Flask(__name__)


class InteractiveAgentSession():
    def __init__(self):
        llm = ChatOpenAI(temperature=0)
        self.agent = SingleQaAgent(llm,
                          "./data/dev/db_cs_with_sources.pkl",
                          prompt=prompts.TURBO_PROMPT,
                          vectorstore_k=8,
                          vectorstore_sim_score_threshold=0.7,
                          passages_path="./data/dev/cs_data.pkl",
                          tfidf_k=8)
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
