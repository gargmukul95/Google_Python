#!/usr/bin/env python3

import csv


def read_employees(path_to_file):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    data = []
    with open(path_to_file) as file:
        reader = csv.DictReader(file, dialect='empDialect')
        # data = []
        for i in reader:
            data.append(i)
    return data


Employee_list = read_employees('/home/student-00-f03e6d5cc72b/data/employees.csv')


# print(Employee_list)


def process_data(data):
    department_list = []
    for employee_data in data:
        department_list.append(employee_data['Department'])
    # print(department_list)
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = data.count(department_name)
    return department_data


# read_employees('/home/student-00-f03e6d5cc72b/data/employees.csv')
dictionary = process_data(Employee_list)
print(dictionary)


def write_report(dictionary, result):
    with open(result, 'w+') as f:
        for i in sorted(dictionary):
            f.write(str(i) + ':' + str(dictionary[i]) + '\n')


write_report(dictionary, '/home/student-00-f03e6d5cc72b/test_report.txt')

