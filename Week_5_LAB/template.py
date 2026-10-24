"""
RECORD CHECK  -  my version
===========================

Name  : Anashe Neola Kabaya
Lane  :  AI 
Date  : 21/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

class Record:
    over_limit_count = 0
    def __init__(self, label, value, limit):
        """initialising class Record"""    
        self.label = label
        self.value = value
        self.limit = limit
        

    def status(self):
        """Calculates percentage and returns its status"""
        percent = (self.value/self.limit) * 100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.
   
r1 = Record("survey_2027", 1193, 1200)
r2 = Record("survey_2028", 1225, 1200)

print(r1.label, r1.status())
print(r2.label, r2.status())

with open("my_records_5.txt", "w") as f:
    f.write(f"{r1.label},{r1.value},{r1.limit}\n")
    f.write(f"{r2.label},{r2.value},{r2.limit}\n")
    
def load_records(path):
    """Loads objects from a file into a list and returns the list"""
    records = []
    with open(path, "r") as f:
        for line in f:
            label, value, limit = line.strip().split(",") 
            records.append(Record(label, float(value), float(limit)))
    return records


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

count = 1
records = load_records("my_records_5.txt")

for record in records:

    if record.status() == "OVER LIMIT":
        Record.over_limit_count += 1

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print(f"label   :   {record.label}")
    print(f"value   :   {float(record.value):.2f}")
    print(f"limit   :   {float(record.limit):.2f}")
    print(f"status  :   {record.status()}")

    print("=" * 34)

print(f"{Record.over_limit_count} of {len(records)} records are OVER LIMIT")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
