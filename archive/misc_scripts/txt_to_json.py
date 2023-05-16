import json

with open("./data/dev/questions_with_ref_answers.txt", "r") as f:
    lines = f.readlines()
    questions = [line.strip() for idx, line in enumerate(
        lines) if idx % 3 == 0]
    answers = [line.strip() for idx, line in enumerate(
        lines) if idx % 3 == 1]
    
    qa = list(zip(questions, answers))
    qa = [{"question": q, "answer": a} for q, a in qa]

    with open("./data/dev/questions_with_ref_answers.json", "w") as out:
        json.dump(qa, out)


data = None    
with open("./data/dev/questions_with_ref_answers.json", "r") as f:
    data = json.load(f)
    for idx, qa in enumerate(data):
        qa["q_num"] = idx + 1

with open("./data/dev/questions_with_ref_answers.json", "w") as out:
    json.dump(data, out)