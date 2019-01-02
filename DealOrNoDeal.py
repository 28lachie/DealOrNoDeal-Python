"""
==============================================
               Deal or No Deal v1.0
                By Lachlan Evans
==============================================
    Libraries
"""
import random
import sys

'''
    Core Game Variables
        availableCases: Array of numeric (dollar) values of the cases
        selectedCases: An array storing the list of selected cases (integer value)
        availableCasesCount: The amount of cases to pick from.
'''
allCaseValues = [
    .50, 1, 2, 5, 10, 20, 50, 100, 150, 200, 250, 500, 750,
    1000, 2000, 3000, 4000, 5000, 10000, 15000, 20000,
    50000, 75000, 100000, 20000
]

displayValues = [
    .50, 1, 2, 5, 10, 20, 50, 100, 150, 200, 250, 500, 750,
    1000, 2000, 3000, 4000, 5000, 10000, 15000, 20000,
    50000, 75000, 100000, 20000
]

selectedCases = []
yourCaseValue = None
available_cases_count = len(allCaseValues)
'''
    Main Program
'''


def main():
    global yourCaseValue
    global available_cases_count

    random.shuffle(allCaseValues)

    '''
        Case Selection
    '''
    while yourCaseValue is None:
        try:
            user_case_number = int(input(
                "Hello and welcome to deal or no deal, please choose a case between 1, %s: " % available_cases_count))

            if 1 <= user_case_number <= available_cases_count:
                print("Case %s selected." % user_case_number)
                yourCaseValue = allCaseValues[user_case_number - 1]
                allCaseValues.remove(yourCaseValue)

                selectedCases.append(user_case_number)
            else:
                print("Please enter a valid case number.")
        except ValueError:
            print("Please enter a valid case number.")

    '''
        Iteration until no more cases can be opened
    '''
    case_open_count = 0
    while len(allCaseValues) > 0:
        if len(allCaseValues) > 1:
            try:
                print("")
                print("Available Cases: %s " % get_available_cases())
                selected_case_number = int(input("Please select a case to open: "))

                print("")

                if 1 <= selected_case_number <= available_cases_count:
                    if selected_case_number in selectedCases:
                        print("This case has already been selected.")
                    else:
                        selectedCases.append(selected_case_number)
                        selected_case_value = allCaseValues.pop(0)
                        displayValues.remove(selected_case_value)

                        print(
                            "You have selected case %s, it contains $%s" % (selected_case_number, selected_case_value))

                        case_open_count += 1

                        if case_open_count >= 3:
                            execute_banker()
                            case_open_count = 0
                else:
                    print("This case is not valid.")
            except ValueError:
                print("Please enter a valid case number")
        else:
            print(sorted(displayValues))
            stay_switch = False
            while not stay_switch:

                prompt_result = str(input("Would you like to switch or stay?").lower())

                if prompt_result == 'stay':
                    print("You have won $%s" % yourCaseValue)
                    stay_switch = True
                elif prompt_result == 'switch':
                    print("You have won $%s" % str(allCaseValues[0]))
                    stay_switch = True
                else:
                    print("Please enter switch or stay only!")
            sys.exit(0)


'''
    Returns a list of possible cases
'''


def get_available_cases():
    available_cases = []
    for caseNumber in range(1, available_cases_count + 1):
        if caseNumber not in selectedCases:
            available_cases.append(caseNumber)

    return available_cases


'''
    Executes the banker function
'''


def execute_banker():
    print("[===== BANKER CALLS =====]")

    available_cases = get_available_cases()

    offer = round(sum(allCaseValues) / len(available_cases))

    print(sorted(displayValues))
    print("The banker has offered $%s" % offer)
    response = str(input("Deal Or No Deal?").lower())
    if response == 'deal':
        print("You would have one: $%s" % yourCaseValue)
        print("You have won $%s" % offer)
        sys.exit(0)


main()

