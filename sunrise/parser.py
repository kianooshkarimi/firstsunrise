import re
# importing the text entered by the user and checking if does it match to the calculation pattern or not
# then classifying the output of the function, baz, as a Calculator action or just an action.

from sunrise.actions import Action, Calculator
def parse(usertext):
    
    matched_or_not = re.search('[+-]?\s*\(?\s*[0-9]+([.][0-9]+)?\s*\)?\s*(\+|-|\*|\/)\s*[(]?\s*[+-]?\s*[0-9]+([.][0-9]+)?\s*\)?', usertext) 
    if (bool(matched_or_not)):
        return Calculator(usertext)
    else:
        return None


