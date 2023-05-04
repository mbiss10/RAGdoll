import sys
import pickle
from qa_agent import SingleQaAgent
from prompts import CONCISE_PROMPT

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run_dev_set.py <num_questions>")
        sys.exit(1)

    num_questions = int(sys.argv[1])

    agent = SingleQaAgent("./db_cs_with_sources.pkl",
                          temperature=0, num_docs_to_retrieve=12, prompt=CONCISE_PROMPT)

    # Ask questions from the dev set and save the results in txt format
    with open("./dev_set_data/dev_qs_with_ref_answers.txt", "r") as questions:
        with open("./dev_answers_12.txt", "w") as f:
            for idx, line in enumerate(questions):
                if idx % 3 != 0:
                    continue

                q_num = idx // 3 + 1
                if q_num > num_questions:
                    break

                f.write(line)
                res = agent.ask(line.strip(), return_only_outputs=False)
                f.write(res['output_text'] + "\n\n")

    # Save pickled version of QA history
    with open("./dev_history_12.pkl", "wb") as f:
        pickle.dump(agent.history, f)

    # with open("./dev_history_1.pkl", "rb") as f:
    #     history = pickle.load(f)
    #     print(history)
