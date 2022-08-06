import random


def check_ans():
    answer = "789054"
    print(answer)
    guess = "123456"
    temp_key = ""
    for x in range(6):
        if answer.count(guess[x]) == 0:
            print(f"{guess[x]} not in string")
            temp_key += "W"
            continue
        elif answer[x] == guess[x]:
            print(f"{guess[x]} in correct spot in string")
            temp_key += "C"
            continue
        print(f"{guess[x]} wrong spot in string")
        temp_key += "P"
        
    print(temp_key)
    
check_ans()

