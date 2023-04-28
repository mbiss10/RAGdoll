PDF_PATH = "./data/csci.pdf"
import copy
import json

"""

# ### Inference using high-res strategy
from unstructured.partition.pdf import partition_pdf

# Returns a List[Element] present in the pages of the parsed pdf document
elements = partition_pdf(PDF_PATH)

for element in elements[:100]:
    print(element, "\n\n")

"""


"""
# ### Explore layout
from unstructured_inference.inference.layout import DocumentLayout
layout = DocumentLayout.from_file(PDF_PATH)

layout.pages[0].elements[0]

for page in layout.pages:
    for el in page.elements:
        print(el.type)
        print(el.text)
        print("____\n")
"""

"""
# ### Try fast strategy
elements_fast = partition_pdf(PDF_PATH, strategy="fast")

for element in elements_fast:
#     print(type(element))
    print(element, "")
"""


"""
# ### PDFMiner
from pdfminer.high_level import extract_text
from io import StringIO
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams

output_string = StringIO()
with open('samples/simple1.pdf', 'rb') as fin:
    extract_text_to_fp(fin, output_string, laparams=LAParams(),
    output_type='html', codec=None)
"""


###########
# courses.json => cs_courses list
###########

cs_courses = None
with open("./data/courses.json", "r") as f:
    print("Loading courses.json")
    course_dict = json.load(f)
    courses = course_dict["courses"]
    
    print(f"Found info on {len(courses)} courses")
    
    cs_courses = [course for course in courses if course["department"] == "CSCI"]


# for course in cs_courses:
#     print(len(str(course)))



###########
# cs_courses list => courses_prefixed_separated.txt
# (Each section is on a separate line with all info for that section as JSON)
# (Each course is also given its own line for the description)
###########
"""
# course_logistics = []
# for course in copy.deepcopy(cs_courses):
#     del course["descriptionSearch"]
#     course_name = f"{course['department']} {course['number']} Section {course['section']}"
#     course_json_linearized = str(course)
#     res = f"{{course: {course_name}, {course_json_linearized[1:]}"
#     course_logistics.append(res)

with open("./data/courses_prefixed_separated.txt", "w") as f:
    for course in copy.deepcopy(cs_courses):
        del course["descriptionSearch"]
        
        course_name = f"{course['department']} {course['number']} Section {course['section']}"
        f.write(f"{{course: {course_name}, ")
        
        remainder_str = ", ".join([f"{k}: {v}" for k,v in course.items()])
        f.write(f"{remainder_str}}}\n")

course_descriptions = dict()

for course in cs_courses:
    course_name = f"{course['department']} {course['number']}"
    if course_name not in course_descriptions:
        course_descriptions[course_name] = course['descriptionSearch']

        
with open("./data/courses_prefixed_separated.txt", "a") as f:
    for k, v in course_descriptions.items():
        f.write(f"{k}: {v}\n")

"""


###########
# Create courses_ultra_processed.txt
# Each SECTION of a course is given a single line with the following info as key/value pairs:
# - section name
# - year
# - semester
# - courseID
# - sectionType
# - peoplesoftNumber
# - classType
# - instructors (nested data)
# - meetings (nested data)
# 
# 
# Each COURSE is also given several lines including the following info as key/value pairs:
# - descriptionSearch
# - gradingBasisDesc
# 
# - classFormat 
# - extraInfo
# - crossListing
# - components
# 
# - titleLong
# - titleShort
# 
# - courseAttributes (nested data)
# 
# - classReqEval
# 
# - prereqs
# 
# - departmentNotes
# 
# - enrolmentPreferences
###########

course_segments = [
    ["descriptionSearch"],
    ["gradingBasisDesc"],
    ["titleLong", "titleShort"],
    ["classFormat", "extraInfo", "crossListing", "components"],
    ["courseAttributes"],
    ["classReqEval"],
    ["prereqs"],
    ["departmentNotes"],
    ["enrolmentPreferences"]
]

section_segments = ["year", "semester", "courseID", "sectionType", "peoplesoftNumber", "classType", "instructors", "meetings"]

courses_processed = set()
with open("./data/courses_ultra_processed.txt", "w") as f:
    for section in copy.deepcopy(cs_courses):
        section_name = f"{section['department']} {section['number']} Section {section['section']}"
        course_name = f"{section['department']} {section['number']}"
        
        if course_name not in courses_processed:
            for segment_list in course_segments:
                # add info about this course
                course_line = f"{course_name} "
                course_line += ", ".join([f"{segment}: {section[segment]}" for segment in segment_list])
                course_line += "\n"
                f.write(course_line)
                courses_processed.add(course_name)
        
        for section_segment in section_segments:
            section_line = f"{section_name} "
            section_line += ", ".join([f"{segment}: {section[segment]}" for segment in section_segments])
            section_line += "\n"
            f.write(section_line)


