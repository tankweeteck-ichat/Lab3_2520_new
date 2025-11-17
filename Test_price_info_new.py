import price_info as PRINFO


def test_cost_of_fruits():
    expected = 8.10   #  Pineapple x 3 = (2.70*3)
    result = PRINFO.cost_of_fruits('pineapple', 3)
    assert(result == expected)



def test_total_cost():
    expected = 46.75
    result = PRINFO.total_cost_shopping()
    assert(result == expected)



