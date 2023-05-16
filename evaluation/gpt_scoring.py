from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
import os 
from dotenv import load_dotenv
import json


LLM_ANSWERS_FILEPATH = "./results/dev_answers_turbo.json"
OUT_FILEPATH = "./results/dev_answers_turbo_with_gpt_scores.json"

# Set up API key
load_dotenv()
API_KEY = os.getenv('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = API_KEY

evaluator_template = """You are an evaluator grading an answer generated by a large language model in response to a question.
You are given a gold-standard reference answer in order to score the model's answer.
You must assign the language model's answer a score of either 0, 1, or 0.5.
A score of 1 means the model's answer completely and correctly answers the question, a score of 0.5 means the model's answer\
    is not incorrect but is not as specific or complete as it could be, and a score of 0 means the model's answer is incorrect,\
    missing essential information, or did not answer the question. Respond with only the score, no explanation.

Question: {question}

Reference Answer: {reference_answer}

Large language model's answer: {llm_answer}

Score (0, 1, or 0.5):
"""

llm = ChatOpenAI(temperature=0)
llm_chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template(evaluator_template)
)

# response = llm_chain.run(
#     question="What is the full title of CSCI 537?",
#     reference_answer="There is no CSCI 537.",
#     llm_answer="The full title of CSCI 537 is not provided.")

res = []
with open(LLM_ANSWERS_FILEPATH, "r") as llm_answers:
    llm_answers = json.load(llm_answers)

    for qa_object in llm_answers:
        response = llm_chain.run(
            question=qa_object["question"],
            reference_answer=qa_object["answer"],
            llm_answer=qa_object["ragdoll_answer"])

        if response not in ["0", "0.5", "1"]:
            print(f"Invalid response for question {qa_object['question']}: {response}")
            continue
        
        print(f"Question: {qa_object['question']}")
        print(f"Score: {response}\n")
        
        qa_object["gpt_score"] = response
        res.append(qa_object)
    
with open(OUT_FILEPATH, "w") as out:
    json.dump(res, out)


