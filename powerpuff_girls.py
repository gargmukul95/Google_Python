# Read input from STDIN. Print your output to STDOUT
# Use input() to read input from STDIN and use print to write your output to STDOUT
# import sys

def main():
    number_of_ingridients = input()
    value_ingridients_girls = input()
    list_value_ingridients_girls = [x.strip() for x in value_ingridients_girls.split()]
    print(list_value_ingridients_girls)
    value_ingridients_lab = input()
    list_value_ingridients_lab = [x.strip() for x in value_ingridients_lab.split()]
    print(list_value_ingridients_lab)
    result = []
    if int(number_of_ingridients) == len(list_value_ingridients_girls) and int(number_of_ingridients) == len(list_value_ingridients_lab):
        for i in range(int(number_of_ingridients)):
            result.append(int(list_value_ingridients_lab[i]) // int(list_value_ingridients_girls[i]))
    number_of_girls = min(result)
    # print(result)
    print(number_of_girls)

main()
