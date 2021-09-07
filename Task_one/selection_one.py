from Task_one.validation import validation


def selection_subtask_1():
    valid = validation("kawabanga!")
    subtask = [
        "1: Validation Password",
        "2: Addition and multiplication"
    ]
    print("Please select subtask for work:\n *type \"exit\" if you want to exit \n")
    answer = input()
    if answer == "exit":
        print("Goodbye , Samurai (っ˘̩╭╮˘̩)っ")
    elif answer == 1:
        valid.run()
    elif answer == 2:
        pass
    else:
        print("unknown request, please enter correct data")
        selection_subtask_1()
