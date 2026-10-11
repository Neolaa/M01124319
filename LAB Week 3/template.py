"""
RECORD CHECK  -  my version
===========================

Name  : Anashe Neola Kabaya
Lane  :  AI 
Date  : 09/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1.

def check(value, limit):
    """Calculates and returns the difference and the percentage"""
    difference = value - limit
    percent = (value/limit) * 100
    return difference, percent 

def status_of(percent):
    """Returns the status of the percentage"""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else: return "OK"

def print_report(label, value, limit, difference, percent, status):
    """Prints all the information"""
    print(f"label       : {label}")
    print(f"value       : {value}")
    print(f"limit       : {limit}")
    print(f"difference  : {difference:.2f}")
    print(f"percent     : {percent:.2f}%")
    print(f"status      : {status}")


# ==================================================================== INPUT
# 2. 

label = input("enter label: ")
count = 0  #initializing count for the number of times the percentage is "Over Limit"

while label != "quit": #loop for user to check as many records as they want
    
    value = float(input("enter value: "))    
    limit = float(input("enter limit: ")) 


# ================================================================== PROCESS
# 3.
    difference, percent = check(value, limit) #calculating difference
    status = status_of(percent) #getting status using the function "status_of"        


# =================================================================== OUTPUT
# 4. 

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print_report(label, value, limit, difference, percent, status)
    print("=" * 34)
    if status == "OVER LIMIT":
        count += 1

    label = input("enter label: ")

print(f"Number of times percentage has been over limit: {count}")


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
