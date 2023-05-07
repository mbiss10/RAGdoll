from rouge_score import rouge_scorer
from nltk.tokenize import word_tokenize
import nltk
import numpy as np
import string
import csv


# NOTE: run using `python3 -W ignore evaluate.py` to suppress BLEU warnings

def tokenize_with_no_punctuation(s):
    tokens = word_tokenize(s)

    # Remove some punctuation marks that aren't needed.
    # Note: some punctuation is important for meaning, so we don't remove all punctuation
    # e.g. lowest acceptable grade for Discrete Math requirement is C-
    excluded = set(['(', ')', '[', ']', '{', '}', '<', '>', ',', '.'])
    tokens_no_punc = [''.join(ch for ch in t if ch not in excluded)
                      for t in tokens]

    return [token for token in tokens_no_punc if token]


reference_questions = None
reference_answers = None
with open("../dev_set_data/dev_qs_with_ref_answers.txt", "r") as reference_file:
    reference_lines = reference_file.readlines()
    reference_questions = [line.strip() for idx, line in enumerate(
        reference_lines) if idx % 3 == 0]
    reference_answers = [line.strip() for idx, line in enumerate(
        reference_lines) if idx % 3 == 1]


# 2D array where each row is a list of answers for a particular model (agent)
model_answers = []
output_filepaths = [
    "../output/dev_answers_2.txt",
    "../output/dev_answers_7.txt",
    "../output/dev_answers_12.txt"
]
for output_filepath in output_filepaths:
    with open(output_filepath, "r") as output_file:
        model_answers.append([line.strip() for idx, line in enumerate(
            output_file.readlines()) if idx % 4 == 1])


# 2D list where each entry is a list of: [question, reference_answer, *model_answers]
qa_matrix = list(zip(reference_questions, reference_answers, *model_answers))

scores_matrix = []
model_names = ["Model 2", "Model 7", "Model 12"]
roguescorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
for idx, (q, ref, *answers) in enumerate(qa_matrix):
    print(f"Question: {q}")
    print(f"Reference Answer: {ref}")

    # tokenize the reference answer once, since it's the same for all models
    tokenized_ref = tokenize_with_no_punctuation(ref)

    # create list of scores for this question
    scores_row = [idx+1]

    for i, answer in enumerate(answers):
        # compute ROUGE scores
        score = roguescorer.score(ref, answer)
        print(
            f"Model {model_names[i]} answer: {answer}\n ROUGE-1: {score['rouge1']} || ROUGE-L: {score['rougeL']}")

        for rouge_type in ['rouge1', 'rougeL']:
            scores_row.extend(
                [score[rouge_type].precision, score[rouge_type].recall, score[rouge_type].fmeasure])

        # compute BLEU score
        processed_ans_tokens = tokenize_with_no_punctuation(answer)
        BLEUscore = None
        if len(processed_ans_tokens) >= 4 and len(tokenized_ref) >= 4:
            BLEUscore = nltk.translate.bleu_score.sentence_bleu(
                [tokenize_with_no_punctuation(answer)], tokenized_ref)

            # many scores are neaROUGE-Ly 0, so round to 5 decimal places
            BLEUscore = round(BLEUscore, 5)

        scores_row.append(BLEUscore)
        print(f"BLEU: {BLEUscore}")

    scores_matrix.append(scores_row)


# write scores to csv file
with open('./automated_scores.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Question #',
                     'ROUGE-1 Precision (2 Doc)', 'ROUGE-1 Recall (2 Doc)', 'ROUGE-1 F1 (2 Doc)',
                     'ROUGE-L Precision (2 Doc)', 'ROUGE-L Recall (2 Doc)', 'ROUGE-L F1 (2 Doc)',
                     'BLEU (2 Doc)',
                     'ROUGE-1 Precision (7 Doc)', 'ROUGE-1 Recall (7 Doc)', 'ROUGE-1 F1 (7 Doc)',
                     'ROUGE-L Precision (7 Doc)', 'ROUGE-L Recall (7 Doc)', 'ROUGE-L F1 (7 Doc)',
                     'BLEU (7 Doc)',
                     'ROUGE-1 Precision (12 Doc)', 'ROUGE-1 Recall (12 Doc)', 'ROUGE-1 F1 (12 Doc)',
                     'ROUGE-L Precision (12 Doc)', 'ROUGE-L Recall (12 Doc)', 'ROUGE-L F1 (12 Doc)',
                     'BLEU (12 Doc)'])
    writer.writerows(scores_matrix)
