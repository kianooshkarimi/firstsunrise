from sunrise import do


def test_parser():
    assert '6' == do('2 + 4')
    assert '6' == do('Add 2 by 4')
    assert '2' == do('subtract 2 from 4')
    assert '2' == do('4 - 2')
    assert '6' == do('2 * 3')
    assert '12' == do('Mul 4 by 3')
    assert '3' == do('Mul 3 with 1')
    assert '10' == do('Multiply 2 by 5')
    assert '14' == do('Multiply 7 with 2')
    assert '15' == do('Multiplication of 3 and 5')
    assert '21' == do('3 times 7')
