"""
Fix my phone, minion!
=====================

"She escaped? This can't be happening! Get me the security team!"

Professor Boolean, a notorious mad scientist, just found out his precious rabbit specimen has escaped! He rushes to call his security minions on the lab phone. However, the rabbit escapee hacked the phone to speed her escape! She left a sign with the following clues: Each digit that is dialed has to be a number that can be reached by a knight chess piece from the last digit dialed - that is, you must move precisely 2 spaces in one direction, and then 1 space in a perpendicular direction to dial the next correct number. You can dial any number you want to start with, but subsequent numbers must obey the knight's move rule. 

The lab phone has the numbers arranged in the following way: 1, 2, 3 in the first row; 4, 5, 6 in the second row; 7, 8, 9 in the third row; and blank, 0, blank in the fourth row. 

123
456
789
0 

For example, if you just dialed a 1, the next number you dial has to be either a 6 or an 8. If you just dialed a 6, the next number must be a 0, 1 or 7.

Professor Boolean wants you to find out how many different phone numbers he can dial under these conditions. Write a function called answer(x, y, z) that computes the number of phone numbers one can dial that start with the digit x, end in the digit y, and consist of z digits in total. Output this number as a string representing the number in base-10.

x and y will be digits from 0 to 9. z will be between 1 and 100, inclusive.


Test cases
==========

Inputs:
    (int) x = 6
    (int) y = 2
    (int) z = 5
Output:
    (string) "6"

Inputs:
    (int) x = 1
    (int) y = 5
    (int) z = 100
Output:
    (string) "0"

Inputs:
    (int) x = 3
    (int) y = 7
    (int) z = 1
Output:
    (string) "0"

"""
def answer(x, y, z):
    #       0      1       2     3        4     5     6         7     8       9
    d = [ [6, 4], [6,8], [9,7], [8,4], [3,9, 0],[], [1,7, 0], [2,6], [1,3], [4,2]]
    graph = {}
    c = 0
    for eachList in d:
        graph.setdefault(c,set())
        for eachNumber in eachList:
            graph[c].add(eachNumber)
        c+=1
    #print graph
    #{0: set([4, 6]), 1: set([8, 6]), 2: set([9, 7]), 3: set([8, 4]), 4: set([0, 9, 3]), 5: set([]), 6: set([0, 1, 7]), 7: set([2, 6]), 8: set([1, 3]), 9: set([2, 4])}

    def findPhoneNumbers(graph, begin, end, number=[]):
        number = number + [begin]
        if len(number) == z:
            if begin == end:
                return [number]
            else:
                return []
        numbers = []
        for nextNum in graph[begin]:
            newNumbers = findPhoneNumbers(graph, nextNum, end, number)
            for newNumber in newNumbers:
                numbers.append(newNumber)
        return numbers

    #Begin
    count = 0
    if not graph.has_key(x):
        return 0
    if len(graph[x]) == 0:
        return 0
    if len(graph[y]) == 0:
        return 0
    if z < 1 or z > 100:
        return 0

    for numbers in  findPhoneNumbers(graph, x, y):
        print list(numbers)
        count+=1
    return count

if __name__ == "__main__":
    print answer(6,2,5)
    print answer(3,7,1)
    print answer(1,5,100)
