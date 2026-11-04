from employee import employee_details

def test_employee_details_Vishal():
    result = employee_details ("Vishal" , 100,"IT" , 45000)

    expected_emp = (
        "Employee Name : Vishal\n"
        "Employee ID: 100\n"
        "Department: IT\n"
        "Salary: 45000"
    )

    assert result == expected_emp