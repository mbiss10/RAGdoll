from qa_agent import SingleQaAgent

if __name__ == "__main__":
    agent = SingleQaAgent("./db_cs_with_sources.pkl",
                          temperature=0.5, num_docs_to_retrieve=6)

    with open("./dev_questions.txt", "r") as f:
        for line in f:
            print(f"Asking: {line.strip()}")

            # agent.ask(line.strip(), return_only_outputs=False)
