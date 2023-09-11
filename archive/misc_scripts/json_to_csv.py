import json
import csv

with open("./results/test/test_answers_turbo_with_gpt_scores.json", "r") as f:
    # write the contents of the json file to a csv file
    data = json.load(f)
    with open("./results/test/test_answers_turbo_with_gpt_scores.csv", "w") as out:
        writer = csv.writer(out)
        writer.writerow(["question", "reference_answer", "ragdoll_answer", "gpt_score"])
        for qa_object in data:
            writer.writerow([qa_object["question"], qa_object["answer"], qa_object["ragdoll_answer"], qa_object["gpt_score"]])