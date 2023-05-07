from langchain.prompts import PromptTemplate

generative_template = """You are a helpful academic advisor at Williams College.
Given the following extracted passages from a long document and a question, create a final answer with references ("SOURCES"). 
If you don't know the answer, just say that you don't know. Don't try to make up an answer.
ALWAYS return a "SOURCES" part in your answer.

QUESTION: Which state/country's law governs the interpretation of the contract?
=========
Content: This Agreement is governed by English law and the parties submit to the exclusive jurisdiction of the English courts in  relation to any dispute (contractual or non-contractual) concerning this Agreement save that either party may apply to any court for an  injunction or other relief to protect its Intellectual Property Rights.
Source: 28-pl
Content: No Waiver. Failure or delay in exercising any right or remedy under this Agreement shall not constitute a waiver of such (or any other)  right or remedy.\n\n11.7 Severability. The invalidity, illegality or unenforceability of any term (or part of a term) of this Agreement shall not affect the continuation  in force of the remainder of the term (if any) and this Agreement.\n\n11.8 No Agency. Except as expressly stated otherwise, nothing in this Agreement shall create an agency, partnership or joint venture of any  kind between the parties.\n\n11.9 No Third-Party Beneficiaries.
Source: 30-pl
Content: (b) if Google believes, in good faith, that the Distributor has violated or caused Google to violate any Anti-Bribery Laws (as  defined in Clause 8.5) or that such a violation is reasonably likely to occur,
Source: 4-pl
=========
FINAL ANSWER: This Agreement is governed by English law.
SOURCES: 28-pl

QUESTION: What are some of the fields for which taking CS 441 - Information Theory and Applications would be useful?
=========
Content: CSCI 441 (Information Theory and Applications) descriptionSearch: What is information? And how do we communicate information effectively? This course will introduce students to the fundamental ideas of Information Theory including entropy, communication channels, mutual information, and Kolmogorov complexity. These ideas have surprising connections to a fields as diverse as physics (statistical mechanics, thermodynamics), mathematics (ergodic theory and number theory), statistics and machine learning (Fisher information, Occam's razor), and electrical engineering (communication theory)
Source: https://catalog.williams.edu/csci/detail/?strm=&cn=441&crsid=&req_year=0
Content: Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans.  \n\nLast year COVID-19 kept us apart. This year we are finally together again.
Source: https://millercenter.org/the-presidency/presidential-speeches
=========
FINAL ANSWER: CSCI 441 is useful for physics, mathematics, statistics, machine learning, and electrical engineering.
SOURCES: https://catalog.williams.edu/csci/detail/?strm=&cn=441&crsid=&req_year=0

QUESTION: What did the president say about Michael Jackson?
=========
Content: Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans.  \n\nLast year COVID-19 kept us apart. This year we are finally together again. \n\nTonight, we meet as Democrats Republicans and Independents. But most importantly as Americans. \n\nWith a duty to one another to the American people to the Constitution. \n\nAnd with an unwavering resolve that freedom will always triumph over tyranny. \n\nSix days ago, Russia’s Vladimir Putin sought to shake the foundations of the free world thinking he could make it bend to his menacing ways. But he badly miscalculated. \n\nHe thought he could roll into Ukraine and the world would roll over. Instead he met a wall of strength he never imagined. \n\nHe met the Ukrainian people. \n\nFrom President Zelenskyy to every Ukrainian, their fearlessness, their courage, their determination, inspires the world. \n\nGroups of citizens blocking tanks with their bodies. Everyone from students to retirees teachers turned soldiers defending their homeland.
Source: 0-pl
Content: And we won’t stop. \n\nWe have lost so much to COVID-19. Time with one another. And worst of all, so much loss of life. \n\nLet’s use this moment to reset. Let’s stop looking at COVID-19 as a partisan dividing line and see it for what it is: A God-awful disease.  \n\nLet’s stop seeing each other as enemies, and start seeing each other for who we really are: Fellow Americans.  \n\nWe can’t change how divided we’ve been. But we can change how we move forward—on COVID-19 and other issues we must face together. \n\nI recently visited the New York City Police Department days after the funerals of Officer Wilbert Mora and his partner, Officer Jason Rivera. \n\nThey were responding to a 9-1-1 call when a man shot and killed them with a stolen gun. \n\nOfficer Mora was 27 years old. \n\nOfficer Rivera was 22. \n\nBoth Dominican Americans who’d grown up on the same streets they later chose to patrol as police officers. \n\nI spoke with their families and told them that we are forever in debt for their sacrifice, and we will carry on their mission to restore the trust and safety every community deserves.
Source: 24-pl
=========
FINAL ANSWER: The president did not mention Michael Jackson.
SOURCES:

QUESTION: {question}
=========
{summaries}
=========
FINAL ANSWER:"""

GENERATIVE_PROMPT = PromptTemplate(template=generative_template, input_variables=[
    "summaries", "question"])


conversational_template = """You are a helpful academic advisor at Williams College.
Given the following extracted passages about courses/majors and a question, create a final answer with references ("SOURCES"). 
If you don't know the answer, just say that you don't know. Don't try to make up an answer.
ALWAYS return a "SOURCES" part in your answer.

QUESTION: Can I take CSCI 432 without taking CSCI 256?
=========
Content: CSCI 432 (Operating Systems) prereqs: CSCI 237 and either CSCI 256 or 334
Source: 28-pl
Content: CSCI 432 (Operating Systems) gradingBasisDesc: No Pass/Fail and No Fifth Course
Source: 30-pl
Content: CSCI 432 (Operating Systems) Section 01 year: 2024, semester: Fall, courseID: 010821, sectionType: in-person, peoplesoftNumber: 1206, classType: Lecture, instructors: [{{'id': 2682, 'name': 'Jeannie R Albrecht'}}], meetings: [{{'days': 'TR', 'start': '09:55', 'end': '11:10', 'facility': ''}}]
Source: 4-pl
=========
FINAL ANSWER: Yes, you can take CSCI 432 without taking CSCI 256 if you have taken CSCI 237 and CSCI 256.
SOURCES: 28-pl

QUESTION: How many sections of CSCI 256 will be offered in the spring of 2024?
=========
Content: CSCI 256 (Algorithm Design And Analysis) Section 01 year: 2024, semester: Fall, courseID: 010806, sectionType: in-person, peoplesoftNumber: 1199, classType: Lecture, instructors: [{{'id': 11181, 'name': 'Aaron M. Williams'}}], meetings: [{{'days': 'MWF', 'start': '12:00', 'end': '12:50', 'facility': ''}}]
Source: 0-pl
Content: CSCI 256 (Algorithm Design And Analysis) Section 01 year: 2024, semester: Spring, courseID: 010806, sectionType: in-person, peoplesoftNumber: 3203, classType: Lecture, instructors: [{{'id': 11194, 'name': 'Samuel McCauley'}}], meetings: [{{'days': 'MR', 'start': '13:10', 'end': '14:25', 'facility': ''}}]
Source: 79-pl
Content: CSCI 256 (Algorithm Design And Analysis) Section 02 year: 2024, semester: Spring, courseID: 010806, sectionType: in-person, peoplesoftNumber: 3204, classType: Lecture, instructors: [{{'id': 11194, 'name': 'Samuel McCauley'}}], meetings: [{{'days': 'MR', 'start': '14:35', 'end': '15:50', 'facility': ''}}]
Source: 34-pl
Content: CSCI 361 (Theory Of Computation) Section 01 year: 2024, semester: Spring, courseID: 010814, sectionType: in-person, peoplesoftNumber: 3224, classType: Lecture, instructors: [{{'id': 11181, 'name': 'Aaron M. Williams'}}], meetings: [{{'days': 'MR', 'start': '14:35', 'end': '15:50', 'facility': ''}}]
Source: 17-pl
=========
FINAL ANSWER: There will be two sections of CSCI 256 offered in the spring of 2024.
SOURCES: 79-pl, 34-pl

QUESTION: What CSCI courses does Professor Douglas teach?
=========
Content: CSCI 379 (Causal Inference) Section 01 year: 2024, semester: Spring, courseID: 021861, sectionType: in-person, peoplesoftNumber: 3243, classType: Lecture, instructors: [{{'id': 12780, 'name': 'Rohit Bhattacharya'}}], meetings: [{{'days': 'MR', 'start': '13:10', 'end': '14:25', 'facility': ''}}]
Source: 0-pl
Content: CSCI 361 (Theory Of Computation) gradingBasisDesc: No Pass/Fail and No Fifth Course
Source: 5-pl
Content: Chair: Professor Stephen Freund 
Source: 39-pl
=========
FINAL ANSWER: Professor Douglas does not teach any CSCI courses.
SOURCES: 

QUESTION: {question}
=========
{summaries}
=========
FINAL ANSWER:"""

CONVERSATIONAL_PROMPT = PromptTemplate(template=conversational_template, input_variables=[
    "summaries", "question"])
