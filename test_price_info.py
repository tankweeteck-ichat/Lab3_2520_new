import price_info as PRINFO

def test_CostOfFruits():
    expected = 14.0  # Orange = $1.40. So, cost = 1.40 x 10 = 14.0
    answer = PRINFO.cost_of_fruits("orange", 10)
    assert (answer == expected)



def test_total_cost_shopping():
    expected = 46.75
    answer = PRINFO.total_cost_shopping()
    assert (answer == expected)





