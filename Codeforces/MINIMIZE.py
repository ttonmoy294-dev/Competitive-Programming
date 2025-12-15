# Codeforces Problem 2009A - Minimize!
# https://codeforces.com/contest/2009/problem/A
# Solved by トンモイ
t = int(input())  # Number of test cases
for _ in range(t):
    a, b = map(int, input().split())  # Read two integers
    c = abs(a - b)  # Calculate absolute difference
    print(c)  # Print the result
