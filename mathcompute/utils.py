import math

from mathcompute import decorators

REF_POWER = 15
MAX_NUMBER = 10**REF_POWER


def nth_fibonacci(n):
    """Computes the fibonacci number in the iterative way."""
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


def string_addition(num1, num2):
    """Adds two numbers in format."""
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
    """Computes the fibonacci number using string."""
    if n <= 2:
        return "1"

    first = "1"
    second = "1"
    third = first + second

    for counter in xrange(3, n + 1):
        third = string_addition_new(first, second)
        first = second
        second = third

    return third


def string_addition_new_final(num1, num2):
    """
    Adds two numbers in string format.
    Handles positive numbers only.
    """
    length1 = len(num1)
    length2 = len(num2)
    length = max(length1, length2)

    if num1 == "0" and num2 == "0":
        return "0"

    ans = []
    r1 = num1[::-1]
    r2 = num2[::-1]
    for i in xrange(0, length, REF_POWER):
        first = r1[i:i + REF_POWER][::-1]
        second = r2[i:i + REF_POWER][::-1]
        try:
            first = int(first)
        except ValueError as e:
            first = 0

        try:
            second = int(second)
        except ValueError as e:
            second = 0

        a = first + second
        ans.append(a)

    ans.append(0)
    for k, v in enumerate(ans):
        if v >= MAX_NUMBER:
            ans[k + 1] += 1

        ans[k] = str(v + MAX_NUMBER)[1:]

    return ''.join(ans[::-1]).lstrip("0")


def nth_fibonacci_string(n):
    if n <= 2:
        return "1"

    first = "1"
    second = "1"
    third = first + second

    for counter in xrange(3, n + 1):
        third = string_addition_new_final(first, second)
        first = second
        second = third

    return third


timed_nth_fibonacci_string = decorators.time_calc(nth_fibonacci_string)
timed_nth_fibonacci_string_new = decorators.time_calc(nth_fibonacci_string)
