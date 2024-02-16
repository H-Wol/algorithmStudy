from sys import stdin


def max_daily_sales(N, X, sales):
    max_sales = current_sales = sum(sales[:X])
    max_count = 1

    for i in range(1, N - X + 1):
        current_sales = current_sales - sales[i - 1] + sales[i + X - 1]

        if current_sales > max_sales:
            max_sales = current_sales
            max_count = 1
        elif current_sales == max_sales:
            max_count += 1

    return max_sales, max_count


input = stdin.readline

N, X = map(int, input().split())
sales = list(map(int, input().split()))

max_sales, max_count = max_daily_sales(N, X, sales)

if max_sales == 0:
    print("SAD")
else:
    print(max_sales)
    print(max_count)
