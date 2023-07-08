q1>def isPowerOfTwo(n):
    if n <= 0:
        return False
    return n & (n - 1) == 0

q2>def sumOfFirstNNumbers(n):
    return (n * (n + 1)) // 2

q3>def factorial(N):
    result = 1
    for i in range(1, N+1):
        result *= i
    return result

q4>def exponent(N, P):
    result = N ** P
    return result

q5>def findMax(arr):
    # Base case: if the array contains only one element, return that element
    if len(arr) == 1:
        return arr[0]

    # Recursive case:
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Find the maximum elements in each half recursively
    left_max = findMax(left_half)
    right_max = findMax(right_half)

    # Compare the maximum elements of the two halves and return the larger one
    return max(left_max, right_max)

q6>def findNthTerm(a, d, N):
    nth_term = a + (N - 1) * d
    return nth_term

q7>def permute(s, l, r):
    if l == r:
        print("".join(s))
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]  # Swap the characters
            permute(s, l + 1, r)  # Recursively generate permutations for the remaining characters
            s[l], s[i] = s[i], s[l]  # Undo the swap to backtrack

def printPermutations(S):
    s = list(S)  # Convert the string to a list of characters
    n = len(s)
    permute(s, 0, n - 1)

q8>def productOfArrayElements(arr):
    product = 1
    for num in arr:
        product *= num
    return product
