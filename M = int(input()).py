M, N = map(int, input().split())
n = N - M
def calculate_ti(a):
    if a == 1:
        return 1
    elif a == 2:
        return 2
    else:
        tem_number = 1
        result = 2
        for idx in range(3, a + 1):
            result, tem_number= tem_number + result, result
        return result
print(calculate_ti(n))