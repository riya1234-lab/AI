# Simple English to FOPL converter

sentence = input("Enter a simple sentence: ")

# Convert to lowercase for easy checking
s = sentence.lower()

# Rules for conversion
if "all" in s and "are" in s:
    words = s.split()
    print("FOPL: ∀x (" + words[1] + "(x) → " + words[-1] + "(x))")

elif "is a" in s:
    words = s.split()
    print("FOPL:", words[0].capitalize() + "(" + words[-1] + ")")

elif "loves" in s:
    words = s.split()
    print("FOPL: Loves(" + words[0] + "," + words[2] + ")")

elif "some" in s:
    words = s.split()
    print("FOPL: ∃x (" + words[1] + "(x))")

else:
    print("Sorry, sentence not supported")