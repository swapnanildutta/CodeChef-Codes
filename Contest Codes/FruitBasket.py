'''
Teacher brought a fruit basket for three students. The basket contains only Apples, Mangoes and Oranges. Student A knows a value a, the total number of Apples and Mangoes in the Basket, B knows a value b, the total number of Mangoes and Oranges in the basket and Student C knows a value c, the total number of Oranges and Apples in the Basket. Since the teacher brought it he knows a value d

, the total number of fruits in the basket. You have to determine the exact number of Apples , Mangoes and Oranges in the basket separately.
Input:

    First line will contain T

, number of testcases. Then the testcases follow.
Each testcase contains of a single line of input, four integers a,b,c,d

    .

Output:

For each testcase, output in a single line the number of Apples , Mangoes and Oranges in this order.
Constraints

    1≤T≤100

0≤a≤1000
0≤b≤1000
0≤c≤1000
0≤d≤1000

-The Solution always exisits
Sample Input:

2

7 9 8 12
3 8 7 9
Sample Output:

3 4 5

1 2 6
'''
T=int(input())
out=list()
for i in range(T):
    vals=[int(i) for i in input().split()]
    a,o,m=vals[-1]-vals[1],vals[-1]-vals[0],vals[-1]-vals[2]
    out.append([a,m,o])
for each in out:
    print(each[0],each[1],each[2])