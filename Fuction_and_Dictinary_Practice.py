def view_all_test(task_details):
    ''' Will print the key and value pairs from a dictionary '''

    for key, value in task_details.items():
        print(f"{key} : {value}")

def test_dictionary():
    ''' Creates the to be read from. The result is then returned to the view_all_test function.
        Strings have been used for easy of the tests. Variable will be used as teh values in actual example. '''
    task_assigned = {"Task              ": "Croque-morts",
                     "Assigned For      ": "Neville Longbotoom Granger",
                     "Date Assigned     ": "11/11/2021",
                     "Date Due          ": "07/02/2024",  # Using the defined 'due_date' variable
                     "Task Complete     ": "NO",
                     "Task Description  ": "THIS IS A TEST TO SEE IF THE INFORMATION WILL PULL THROUGH CORRECTLY"
                     }
    view_all_test(task_assigned)
