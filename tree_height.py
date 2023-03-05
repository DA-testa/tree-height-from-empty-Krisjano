import threading
import sys

def compute_height(n, parents):
    max = 0
    temp = 0
    treeheight = [-1] * n

    def get_height(index):
        if treeheight[index] != -1:
            return treeheight[index]
        elif parents[index] == -1:
            treeheight[index] = 1
            return 1
        else:
            treeheight[index] = get_height(parents[index]) + 1
            return treeheight[index]

    for i in range(n):
        temp = get_height(i)
        if temp > max:
            max = temp


    return max


def main(): 
    word = input()
    if 'I' in word: 
        n = int(input())
        parents = list(map(int, input().split()))
    elif word[0] == "F":
        filename = input().strip()
        filepath = 'test/' + filename
        if filename.endswith("a"):
            return
        else:
            with open(filepath, 'r') as fn:
                n = int(fn.readline())
                parents = list(map(int, fn.readline().split()))
    print (compute_height(n, parents))

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
