from Task_one.selection_one import selection_subtask_1


def select():
    tasks = [
        '1: Git and Basic tools'
    ]
    print("Please select task for work:")
    for item in tasks:
        print(f'{item}')
    answer = str(input())
    if answer == "1":
        selection_subtask_1()


if __name__ == '__main__':
    select()
