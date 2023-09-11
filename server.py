"""
A Flask server to handle requests from the fron-end client when running our demo.
"""

from flask import Flask, request, render_template
from single_qa_agent import SingleQaAgent
from langchain.chat_models import ChatOpenAI
import json
import prompts
import requests

app = Flask(__name__)


class InteractiveAgentSession():
    def __init__(self):
        llm = ChatOpenAI(temperature=0)
        self.agent = SingleQaAgent(llm,
                          "./data/dev_david/db_cs_with_sources.pkl",
                          prompt=prompts.TURBO_PROMPT,
                          vectorstore_k=8,
                          vectorstore_sim_score_threshold=0.7,
                          passages_path="./data/dev_david/cs_data.pkl",
                          tfidf_k=10)
        
    def make_request(self, user_input):
        url = 'https://chatgptspanish.org/wp-admin/admin-ajax.php'
        headers = {
            'Accept': '*/*',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryVTFT3tmNveC68dAT',
            'Origin': 'https://chatgptspanish.org',
            'Accept-Language': 'en-US,en;q=0.9',
            'Host': 'chatgptspanish.org',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15',
            'Referer': 'https://chatgptspanish.org/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        }

        post_request_data = f'''------WebKitFormBoundaryVTFT3tmNveC68dAT
Content-Disposition: form-data; name="_wpnonce"

bd435bd251
------WebKitFormBoundaryVTFT3tmNveC68dAT
Content-Disposition: form-data; name="post_id"

44
------WebKitFormBoundaryVTFT3tmNveC68dAT
Content-Disposition: form-data; name="url"

https://chatgptspanish.org
------WebKitFormBoundaryVTFT3tmNveC68dAT
Content-Disposition: form-data; name="action"

wpaicg_chat_shortcode_message
------WebKitFormBoundaryVTFT3tmNveC68dAT
Content-Disposition: form-data; name="message"

Speak english. {user_input}

------WebKitFormBoundaryVTFT3tmNveC68dAT
Content-Disposition: form-data; name="bot_id"

0
------WebKitFormBoundaryVTFT3tmNveC68dAT--
'''

        response = requests.post(url, headers=headers, data=post_request_data)
        
        return response.json()["data"]


    def ask_agent(self, req):
        # Adds data from python client request
        # try:
        #     question = req.get_json().get('question')
        #     response = self.agent.ask(question)
        #     return json.dumps({'status': 200, 'success': response.get('output_text')})
        # except:
        #     print("Unable to get client data.")
        #     return json.dumps({'status': 500, 'success': "Internal Server Error"})

        try:
            question = req.get_json().get('question')
            response = self.make_request(question)
            return json.dumps({'status' : 200, 'success': response})
        except:
            print("Unable to get client data.")
            return json.dumps({'status': 500, 'success': "Internal Server Error"})


session = InteractiveAgentSession()


@app.route('/agent', methods=['POST'])
def api_agent_ask():
    return session.ask_agent(request)
