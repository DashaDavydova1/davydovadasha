def get_sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
n=int(input())               
if n<= 0:
    print(0)
else:
    print(f"Введите {n} чисел по одному:")    
    prev_num = int(input())
    prev_sign = get_sign(prev_num)

    max_len = 1
    current_len = 1
    for _ in range(n-1):
        num = int(input())
        current_sign = get_sign(num)
        if current_sign==prev_sign:
            current_len += 1
    else:
        current_len = 1
        prev_sign = current_sign
    if current_len > max_len:
        max_len = current_len
    print(max_len)       