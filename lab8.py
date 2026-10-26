N = int(input())
a = list(map(int, input().split()))

if len(a) != N:
    print("Ошибка: неверное количество элементов")
else:
    total = sum(a)
    left_sum = 0
    min_diff = float('inf')
    best_index = 0

    for i in range(N):
        right_sum = total - left_sum - a[i]
        diff = abs(left_sum - right_sum)

        if diff < min_diff:
            min_diff = diff
            best_index = i

        left_sum += a[i]
        
    print(best_index + 1)
    print(min_diff)