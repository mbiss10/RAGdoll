# with open("./david_dev_scores.txt", "r") as f:
#     with open("./david_dev_scores_parsed.txt", "w") as out:
#         all_lines = f.readlines()
#         model_2, model_7, model_12 = all_lines[:
#                                                53], all_lines[54:107], all_lines[108:]

#         # print(all_lines[53] == "\n" and all_lines[107] == "\n")
#         for idx, (a, b, c) in enumerate(zip(model_2, model_7, model_12)):
#             out.write(f"Question {idx+1}\n")
#             out.write(a)
#             out.write(b)
#             out.write(c)
#             out.write("\n")

# exit(0)


# with open("../output/dev_answers_all_models.txt", "r") as answers:
#     with open("./temp.csv", "w") as out:
#         writer = csv.writer(out)
#         row = []
#         for idx, line in enumerate(answers):
#             if idx % 6 == 0:
#                 writer.writerow(row)
#                 row = []
#             if idx % 6 in [0, 1, 5]:
#                 continue
#             else:
#                 data = line[line.index("answer: ")+8:]
#                 row.append(data.strip())s


# with open("./david_dev_scores.txt", "r") as david:
#     with open("./mark_dev_scores.txt", "r") as mark:
#         with open("./human_dev_scores.csv", "w") as out:
#             writer = csv.writer(out)

#             david_lines = david.readlines()
#             mark_lines = mark.readlines()
#             row = []
#             for idx, (david_score, mark_score) in enumerate(zip(david_lines, mark_lines)):
#                 if idx % 5 == 0:
#                     writer.writerow(row)
#                     row = []
#                     row.append(mark_score.strip().replace("Question: ", ""))
#                 elif idx % 5 == 4:
#                     continue
#                 else:
#                     row.append(mark_score.strip())
#                     row.append(david_score.strip())


# exit(0)
