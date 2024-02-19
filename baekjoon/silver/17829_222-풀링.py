from sys import stdin

input = stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]


def reduce_array(arr):
    while len(arr) > 1:
        new_arr = []
        for i in range(0, len(arr)-1, 2):
            new_row = []
            for j in range(0, len(arr[0])-1, 2):
                sub_array = [arr[i][j], arr[i][j+1],
                             arr[i+1][j], arr[i+1][j+1]]
                sub_array.sort(reverse=True)
                new_row.append(sub_array[1])
            new_arr.append(new_row)
        arr = new_arr
    return arr[0][0]


result = reduce_array(matrix)
print(result)
