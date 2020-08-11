import re

from sunrise.actions import Action, Calculator

calculator_regex = r'[+-]?\s*\(?\s*[0-9]+([.][0-9]+)?\s*\)?\s*[\+ - \* \/]\s*\(?\s*[+-]?\s*[0-9]+([.][0-9]+)?\s*\)?'
list_of_action_patterns = [
        [calculator_regex, Calculator]
        ]
clasfict = ''
regex = ''
output = None


# importing the text entered by the user and checking if does matchs to the calculation pattern or not
def parse(usertext):
    for i in range(len(list_of_action_patterns)):
        regex = list_of_action_patterns[i][0]
        #classifying the output of the function, as a Calculator (or any other action in future extentions)
        clasfictn = list_of_action_patterns[i][1]
        matched_or_not = re.search(regex, usertext)
        if bool(matched_or_not):
            output = clasfictn
    return output


