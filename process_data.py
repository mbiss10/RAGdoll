import pickle
import json
import os

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = API_KEY

DEV_SET_PATH = "./data/dev"
TEST_SET_PATH = "./data/test"

##########################################
# Extract Math/CS courses (JSON objects
# loaded as dicts) from courses.json file
##########################################
cs_courses = None
math_courses = None
with open("./data/courses.json", "r") as f:
    course_dict = json.load(f)
    courses = course_dict["courses"]

    cs_courses = [
        course for course in courses if course["department"] == "CSCI"]

    math_courses = [
        course for course in courses if course["department"] == "MATH"]

    print(f"Found {len(cs_courses)} CSCI courses.")
    print(f"Found {len(math_courses)} MATH courses.")


##########################################
# Create list of tuples of the form (passage, source)
# where passage is some text about a course or section
# and source is a URL.
##########################################
course_header_groups = [
    ["descriptionSearch"],
    ["gradingBasisDesc"],
    # ["titleLong", "titleShort"],
    ["classFormat", "extraInfo", "crossListing", "components", "departmentNotes"],
    ["courseAttributes"],
    ["classReqEval"],
    ["prereqs"],
    ["enrolmentPreferences"]
]

section_headers = ["year", "semester", "courseID", "sectionType",
                   "peoplesoftNumber", "classType", "instructors", "meetings"]


# list of tuples of the form (passage, source)
cs_data = []
math_data = []
for data, course_list, dept_name in [(cs_data, cs_courses, "csci"), (math_data, math_courses, "math")]:
    # log courses we've processed so we don't repeat course data across multiple sections
    courses_processed = set()

    for section in course_list:
        section_name = f"{section['department']} {section['number']} ({section['titleLong']}) Section {section['section']}"
        course_name = f"{section['department']} {section['number']} ({section['titleLong']})"

        # create source URL for this course using the course catalog
        course_num = section['number']
        course_id = section['courseID']
        course_url = f"https://catalog.williams.edu/{dept_name}/detail/?strm=&cn={course_num}&crsid={course_id}&req_year=0"

        # add info about this course if we haven't already
        if course_name not in courses_processed:
            for header_group in course_header_groups:
                course_line = f"{course_name} "
                course_line += ", ".join(
                    [f"{header}: {section[header]}" for header in header_group])
                course_line += "\n"
                data.append((course_line, course_url))
                courses_processed.add(course_name)

        # add info about this section of the course
        section_line = f"{section_name} "
        section_line += ", ".join(
            [f"{segment}: {section[segment]}" for segment in section_headers])
        section_line += "\n"
        data.append((section_line, course_url))


##########################################
# Add passages from the CS major requirements and
# department info PDF. This was manually extracted
# and cleaned up from the PDF. Cite the PDF as the
# source for these passages.
##########################################
with open(f"{DEV_SET_PATH}/cs_pdf_gold.txt", "r") as f:
    for line in f:
        cs_data.append((line, "https://catalog.williams.edu/pdf/csci.pdf"))

# Do the same for math
with open(f"{TEST_SET_PATH}/math_pdf_gold.txt", "r") as f:
    for line in f:
        math_data.append((line, "https://catalog.williams.edu/pdf/math.pdf"))


print("Data parsing complete.")
print(f"Total CSCI passages created: {len(cs_data)}")
print(f"Total MATH passages created: {len(math_data)}")


##########################################
# Save data to a file for easy viewing
##########################################
with open(f"{DEV_SET_PATH}/cs_with_sources.txt", "w") as f:
    for passage, source in cs_data:
        f.write(f"{passage} [Source: {source}]\n\n")

with open(f"{TEST_SET_PATH}/math_with_sources.txt", "w") as f:
    for passage, source in math_data:
        f.write(f"{passage} [Source: {source}]\n\n")


##########################################
# Create a vectorstore from the data.
# Replace *data with either *cs_data or *math_data
##########################################
# texts, sources = list(zip(*data))

# 🔴 Uncomment the lines below to write the new vectorestore db   🔴
# 🔴 This may cause the model's behavior to change since it will  🔴
# 🔴 create a new knowledge store. It also costs API credits.     🔴

# embeddings = OpenAIEmbeddings()
# db = FAISS.from_texts(texts, embeddings, metadatas=[
#                       {"source": source} for source in sources])


##########################################
# Serialize and store our vectorstores.
# Replace file path for CS versus MATH db
##########################################
# with open("./data/test/db_math_with_sources.pkl", "wb") as f:
#     pickle.dump(db, f)
