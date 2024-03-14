# # import spacy

# # # Load the English language model
# # nlp = spacy.load("en_core_web_sm")

# # # Sample extracted text data
# # extracted_data = """
# # Scott Moonen

# # Senior Software Engineer &
# # Global Technical Ambassador,
# # IBM Pure Application System

 

# # 3039 Cornwallis Rd.
# # Research Triangle Park, NC 27709

# # Tel +1 919 254 1388
# # smoonen@us.ibm.com
# # 
# # """

# # # Process the text with spaCy
# # doc = nlp(extracted_data)

# # # Extract entities and infer job positions
# # job_positions = set()
# # for ent in doc.ents:
# #     if ent.label_ == "ORG":  # Assuming the organization's name is identified as a named entity
# #         # Check if the preceding token is indicative of a job title
# #         if ent.start > 1 and doc[ent.start - 1].pos_ == "ADJ":  # Check for adjective preceding the organization
# #             job_positions.add(doc[ent.start - 1].text)

# # # Print the inferred job positions
# # print("Testing the extraction",job_positions)


# import spacy

# # Load the English language model
# nlp = spacy.load("en_core_web_sm")

# # Sample extracted text data
# extracted_data = """
# Scott Moonen

# Senior Software Engineer &
# Global Technical Ambassador,
# IBM Pure Application System

# 3039 Cornwallis Rd.
# Research Triangle Park, NC 27709

# Tel +1 919 254 1388
# smoonen@us.ibm.com
# """

# # Process the text with spaCy
# doc = nlp(extracted_data)

# # Print named entities and part-of-speech tags
# for token in doc:
#     print(f"Token: {token.text}, Entity Type: {token.ent_type_}, POS Tag: {token.pos_}")
import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Sample extracted text data
extracted_data = """
Scott Moonen

Senior Software Engineer &
Global Technical Ambassador,
IBM Pure Application System

 

3039 Cornwallis Rd.
Research Triangle Park, NC 27709

Tel +1 919 254 1388
smoonen@us.ibm.com
"""

# Process the text with spaCy
doc = nlp(extracted_data)

# Keywords indicating job positions
job_keywords = ["Engineer", "Manager", "Analyst", "Ambassador"]

# Extract job positions based on keywords
job_positions = set()
for token in doc:
    if token.text in job_keywords:
        # Check if the token is preceded by an adjective
        if token.i > 0 and doc[token.i - 1].pos_ == "ADJ":
            job_positions.add(doc[token.i - 1].text + " " + token.text)

# Print the inferred job positions
print("Inferred Job Positions:", job_positions)
