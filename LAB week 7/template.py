"""
RECORD CHECK  -  my version
===========================

Name  : Anashe Neola Kabaya
Lane  :  AI 
Date  : 05/11/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

def parse_line(raw_line):
    """Turns one messy raw status line into a clean dictionary"""
    line = raw_line.strip()
    label_part, rest = line.split(",", 1) # spliting the text into label and the rest of it
    label = label_part.strip().lower()

    fields = {} # creating an empty dictionary
    for piece in rest.split(","):
        key, value = piece.split("=") # spliting the rest of the text into keys and values
        fields[key.strip().lower()] = float(value.strip()) # adding the keys and values to the dictionary

    return {"label": label, "rating": fields["rating"], "age": fields["age"]}

def status_of(record):
    """Determining the status of the record"""
    if record["rating"] < 5:
        return "FLAGGED"
    else:
        return "OK"


# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

raw_records = ["  Survey_2021 , rating=4 , age=23  ",
               "     SurVey_2022 , rating=7 , age=15  ",
               "  survey_2023   , RATING=8 , age=17    ",
               "Survey_2024 ,  rating=3 ,  age=28  ",
               "  Survey_2025 , Rating=6 , Age=20  ",]   

with open("my_file.txt", "w") as f:
    for line in raw_records:
        f.write(f"{line}\n")


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

count = 0 # initializing count for the number of flagged records
for raw_record in raw_records:
    parsed = parse_line(raw_record) # calling parse_line on each record
    print(parsed)
    status = status_of(parsed) # checking the status of the cleaned up record
    if status == "FLAGGED":
        count += 1
    print(f"{parsed["label"]} {status}")
    print()

print(f"{count} out of {len(raw_records)} records are flagged")

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
