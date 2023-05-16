import csv
import json

# open the json file "./results/dev_answers_turbo.json" and write it out to a csv file "./results/dev_answers_turbo.csv":
with open("./results/dev_answers_turbo.json", "r") as f:
    data = json.load(f)
    with open("./results/dev_answers_turbo.csv", "w") as out:
        writer = csv.writer(out)
        writer.writerow(["question", "reference_answer", "ragdoll_answer"])
        for qa in data:
            writer.writerow([qa["question"], qa["answer"], qa["ragdoll_answer"]])

