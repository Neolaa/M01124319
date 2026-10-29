"""
RECORD CHECK  -  my version
===========================

Name  : Anashe Neola Kabaya
Lane  :  AI      
Date  : 01/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.

label  = input("enter label: ")
used = float(input("enter used amount: "))
total = float(input("enter total amount: "))

# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
difference = total - used # calculating difference
percent = (used/total) * 100 # calculating percentage


# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"{'Used':<10}:{used:>10.2f}")
print(f"{'Total':<10}:{total:>10.2f}")
print(f"{'Free':<10}:{difference:>+10.2f}")
print(f"{'Percent':<10}:{percent:>10.2f} %")

print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
