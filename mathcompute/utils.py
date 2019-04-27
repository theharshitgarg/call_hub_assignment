from mathcompute import decorators


def nth_fibonacci(n):
    if n <= 2:
        return 1

    first = 1
    second = 1
    third = first + second

    for counter in xrange(3, n + 1):
        third = first + second
        first = second
        second = third

    return third


def fast_nth_fibonacci(n, ans):
    if n == 0:
        ans[0] = 1
        ans[1] = 1

        return ans

    fast_nth_fibonacci(n / 2, ans)
    a = ans[0]
    b = ans[1]
    c = 2 * b - a
    c = a * c
    d = a * a + b * b

    if n % 2 == 0:
        ans[0] = c
        ans[1] = d

    else:
        ans[0] = d
        ans[1] = c + d

    return ans


def string_addition(num1, num2):
    ans = ""
    length1 = len(num1)
    length2 = len(num2)
    r1 = num1[::-1]
    r2 = num2[::-1]

    carry = 0
    i = 0
    while i < length1 and i < length2:
        ans = ans + str((int(r1[i]) + int(r2[i]) + carry) % 10)
        carry = (int(r1[i]) + int(r2[i]) + carry) / 10
        i = i + 1

    while i < length1:
        ans = ans + str((int(r1[i]) + carry) % 10)
        carry = (int(r1[i]) + carry) / 10
        i = i + 1

    while i < length2:
        ans = ans + str((int(r2[i]) + carry) % 10)
        carry = (int(r2[i]) + carry) / 10
        i = i + 1

    if carry:
        ans = ans + str(carry)
    return ans[::-1]


def nth_fibonacci_string(n):
    if n <= 2:
        return "1"

    first = "1"
    second = "1"
    third = first + second

    for counter in xrange(3, n + 1):
        third = string_addition(first, second)
        first = second
        second = third

    return third


timed_nth_fibonacci_string = decorators.time_calc(nth_fibonacci_string)
