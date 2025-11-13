import employee_info as EMPINFO
from employee_info import employee_data as EMPDATA


def test_GetEmployeesByAge():
    expected = [EMPDATA[0], EMPDATA[1], EMPDATA[2], EMPDATA[4]]
    answer = EMPINFO.get_employees_by_age_range(22,34)
    assert(answer == expected)


def test_CalculateAverageSalary():
    expected = 60166.67
    answer = EMPINFO.calculate_average_salary()
    assert (answer == expected)


def test_GetEmployeesByDept():
    expected = [EMPDATA[0], EMPDATA[-1]]
    answer = EMPINFO.get_employees_by_dept("Sales")
    assert (answer == expected)


def test_GetEmployeesByDept_modify_data():
    expected = [EMPDATA[0], EMPDATA[3], EMPDATA[-1]]
    EMPDATA[3]["department"] = "Sales"  # Modify the data
    answer = EMPINFO.get_employees_by_dept("Sales")
    assert (answer == expected)
    EMPDATA[3]["department"] = "Engineering"  # Restore the data

