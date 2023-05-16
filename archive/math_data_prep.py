
from unstructured_inference.inference.layout import DocumentLayout
from unstructured.partition.pdf import partition_pdf
PDF_PATH = "../data/math.pdf"

# Inference using high-res strategy

# Returns a List[Element] present in the pages of the parsed pdf document
elements = partition_pdf(PDF_PATH)

for element in elements[:100]:
    print(element, "\n\n")


# Explore layout
layout = DocumentLayout.from_file(PDF_PATH)

layout.pages[0].elements[0]

for page in layout.pages:
    for el in page.elements:
        print(el.type)
        print(el.text)
        print("____\n")

# Try fast strategy
# elements_fast = partition_pdf(PDF_PATH, strategy="fast")

# for element in elements_fast:
#     #     print(type(element))
#     print(element, "")
