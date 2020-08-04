import re

from sunrise.actions import Action, Calculator


# Importing the text entered by the user and checking if does it match to the calculation pattern or not.
def parse(usertext):
    calculator_regex = r'[+-]? \s* \(? \s* [0-9]+ ([.][0-9]+)? \s* \)? \s* [\+ - \* \/] \s* \(? \s* [+-]? \s* [0-9]+ ([.][0-9]+)? \s* \)?'
    list_of_action_patterns = [
            [calculator_regex, Calculator]
            ]
    classification = None       
    regex = ''
    output = None
# Classifying the output of the function, if the input matched with the corresponding pattern.
    for i in range(len(list_of_action_patterns)): 
        regex = list_of_action_patterns[i][0]
        classification = list_of_action_patterns[i][1]
        matched_or_not = re.search(regex, usertext)
        if (bool(matched_or_not)):
            output = classification
    return output


