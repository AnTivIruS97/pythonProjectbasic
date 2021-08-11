working_hours = [('sam',100),('tom', 300)]
def emp_max(working_hours):
    cur_maxhrs = 0
    emp_name = ''
    for emp, hours in working_hours:
        if hours > cur_maxhrs:
            cur_maxhrs = hours
            emp_name = emp
    return emp_name, cur_maxhrs
    print(emp_max(working_hours))