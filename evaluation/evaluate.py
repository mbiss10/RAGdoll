from rouge_score import rouge_scorer
from nltk.tokenize import word_tokenize
import nltk
import numpy as np
import csv
import json


# NOTE: run using `python3 -W ignore evaluate.py` to suppress BLEU warnings

LLM_ANSWERS_FILEPATH = "./results/dev_answers_turbo.json"
OUTPUT_FILEPATH = './evaluation/output/automated_scores_turbo.csv'


def tokenize_with_no_punctuation(s):
    tokens = word_tokenize(s)

    # Remove some punctuation marks that aren't needed.
    # Note: some punctuation is important for meaning, so we don't remove all punctuation
    # e.g. lowest acceptable grade for Discrete Math requirement is C-
    excluded = set(['(', ')', '[', ']', '{', '}', '<', '>', ',', '.'])
    tokens_no_punc = [''.join(ch for ch in t if ch not in excluded)
                      for t in tokens]

    return [token for token in tokens_no_punc if token]


output = []
with open(LLM_ANSWERS_FILEPATH, "r") as f:
    data = json.load(f)

    roguescorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    for qa_object in data:
        score_row = []
        
        q = qa_object['question']
        ref_answer = qa_object['answer']
        ragdoll_answer = qa_object['ragdoll_answer']

        score_row.append(q)

        r_score = roguescorer.score(ref_answer, ragdoll_answer)

        for rouge_type in ['rouge1', 'rougeL']:
            score_row.extend(
                [r_score[rouge_type].precision, r_score[rouge_type].recall, r_score[rouge_type].fmeasure])

        # compute BLEU score
        tokenized_ref = tokenize_with_no_punctuation(ref_answer)
        tokenized_ragdoll_answer = tokenize_with_no_punctuation(ragdoll_answer)
        BLEUscore = None
        if len(tokenized_ragdoll_answer) >= 4 and len(tokenized_ref) >= 4:
            BLEUscore = nltk.translate.bleu_score.sentence_bleu(
                [tokenized_ragdoll_answer], tokenized_ref)

            # many scores are neaROUGE-Ly 0, so round to 5 decimal places
            BLEUscore = round(BLEUscore, 5)

        score_row.append(BLEUscore)

        output.append(score_row)


# write scores to csv file
with open(OUTPUT_FILEPATH, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Question',
                     'ROUGE-1 Precision', 'ROUGE-1 Recall', 'ROUGE-1 F1',
                     'ROUGE-L Precision', 'ROUGE-L Recall', 'ROUGE-L F1',
                     'BLEU',
                     ])
    writer.writerows(output)
