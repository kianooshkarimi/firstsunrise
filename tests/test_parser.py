from sunrise import parser
from sunrise.actions import Action, Calculator


def test_parser():
    action = parser.parse('2.3 *(- 43.825)')
    try:
        assert issubclass(action, Action)
    except:
        print('Cannot parse the entered text as an action')
        
    try:
        assert issubclass(action, Calculator)
    except:
        print('cannot parse the entered text as a calculation action')

