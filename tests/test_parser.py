from sunrise.actions import find, Action, Calculator


def test_parser():
    action_add, params_add = find('1 + 4')
    action_sub, params_sub = find('7 - 5')
    action_mul, params_mul = find('2 * 3')
    assert issubclass(action_add, Action)
    assert issubclass(action_add, Calculator)
    assert issubclass(action_sub, Action)
    assert issubclass(action_sub, Calculator)
    assert issubclass(action_mul, Action)
    assert issubclass(action_mul, Calculator)
    assert params_add == {
        'a': '1',
        'operator': '+',
        'b': '4'
    }
    assert params_sub == {
        'a': '7',
        'operator': '-',
        'b': '5'
    }
    assert params_mul == {
        'a': '2',
        'operator': '*',
        'b': '3'
    }
