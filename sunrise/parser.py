import re
# importing the text entered by the user and checking if does it match to the calculation pattern or not
# then classifying the output of the function, baz, as a Calculator action or just an action.

from sunrise.actions import Action, Calculator
def parse(usertext):

    calculator_RegEx ='[+-]?\\s*\\(?\\s*[0-9]+([.][0-9]+)?\\s*\\)?\\s*[\\+ - \\* \\/]\\s*\\(?\\s*[+-]?\\s*[0-9]+([.][0-9]+)?\\s*\\)?';
    
    list_of_action_patterns = [[calculator_RegEx, Calculator(usertext)]]
    clasfict = ''       
    RegEx = ''
    output = None
    
    for i in range(len(list_of_action_patterns)):

        RegEx = list_of_action_patterns[i][0]
        clasfictn = list_of_action_patterns[i][1]
        matched_or_not = re.search(RegEx, usertext)
        if (bool(matched_or_not)):
            output = clasfictn
    
    return output;


