import pickle

with open("./results/turbo_agent_history_on_dev_set.pkl", "rb") as f:
    with(open("./archive/turbo_agent_history_on_dev_set.txt", "w")) as out:
        history = pickle.load(f)
        for x in history:
            out.write(x[0] + "\n" + x[1]['output_text'] + "\n")
            for doc in x[1]["input_documents"]:
                out.write(doc.page_content + "\n")
            out.write("\n")