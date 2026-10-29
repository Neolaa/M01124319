"""
RECORD CHECK  -  my version
===========================

Name  : Anashe Neola Kabaya
Lane  :  AI 
Date  : 15/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1.

def check_record(value, limit):
    """Calculates and returns the difference, percent and status"""
    difference = value - limit # calculating the difference between value and limit
    percent = (value/limit) * 100 # calculating the percentage 
    if value > limit: # checking whether value is over limit or not
        status = "OVER LIMIT"
    else: status = "OK"
    return difference, percent, status

def print_report(label, value, limit, difference, percent, status):
    """Prints all the information"""

    print("=" * 34)
    print(f"label       :   {label:>10}")
    print(f"value       :   {value:>10}")
    print(f"limit       :   {limit:>10}")
    print(f"difference  :   {difference:>10.2f}")
    print(f"percent     :   {percent:>10.2f}%")
    print(f"status      :   {status:>10}")
    print("=" * 34)


# ====================================================================== STORE
# 2. 

records = [] # creating an empty list 'records'  

with open("my_records.txt", "w") as f: # making data file
    f.write("survey_2027,1143,1200\n")
    f.write("survey_2028,1250,1200\n")
    f.write("survey_2029,1079,1200\n")
           

def load_records(path):
    """Loads records from a file into a list of dictionaries"""
    try:
        with open(path, "r") as f:
           
            for line in f: # going through each line in the file
                this_line = line.strip()
                label, value, limit = this_line.split(",")
                keys = ["label", "value", "limit"] # creating a list of keys
                values = [label, value, limit] # creating a list of values
                dictionary = dict(zip(keys, values)) # creating a dictionary by pairing up the list of keys with that of values
                records.append(dictionary)
            return records
    except FileNotFoundError:
        print(f"{path} not found")
        return []

records = load_records("my_records.txt") 

count = 0 # initialising count for the number of times value is over limit
with open("new_records.txt", "w") as f: # creating a new file
    for record in records: 
        label = record.get("label")
        value = int(record.get("value"))
        limit = int(record.get("limit"))
        difference, percent, status = check_record(value, limit)
        
        f.write(f"{label}, {status}\n") # writing to the new file
        print()
        print(f"{label}, {status}")

# =============================================================== PROCESS + OUTPUT
# 3.
        print_report(label, value, limit, difference, percent, status)

        if status == "OVER LIMIT":
            count += 1

print()
print(f"Number of times value was over limit: {count}")




# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
