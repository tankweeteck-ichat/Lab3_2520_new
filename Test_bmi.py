import lab2_2520.bmi as ABC

def test_CalcBMI_underweight():
    expected = -1
    result = ABC.calculate_bmi(1.73, 37)
    assert(result == expected)


def test_CalcBMI_normalweight():
    expected = 0
    result = ABC.calculate_bmi(1.73, 57)
    assert(result == expected)


def test_CalcBMI_overweight():
    expected = 1
    result = ABC.calculate_bmi(1.73, 87)
    assert(result == expected)




