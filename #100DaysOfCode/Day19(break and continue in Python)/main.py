
def code1():
    for i in range(12):
        print("5 x", i+1,'=',5 * i+1)
        if (i == 10):
            break

    print("\n")



def code2():
    for i in range(12):
        print("5 x", i+1,'=',5 * i+1)
        if (i == 10):
            break

    print("Loop ko chodkar nikal gaya")
    print("\n")


def code3():
    for i in range(12):
        if (i == 10):
            break
        print("5 x", i+1,'=',5 * i+1)

    print("\n")


def code4():
    for i in range(12):
        if (i == 10):
            print("Skip the iteration")
            continue
        print("5 x", i+1,'=',5 * i+1)

    print("\n")


def code5():
    i = 0
    while True:
        print(i)
        i += 1
        if (i%100 == 0):
            break




code1()
code2()
code3()
code4()
code5()



"""
Output :
5 x 1 = 1
5 x 2 = 6
5 x 3 = 11
5 x 4 = 16
5 x 5 = 21
5 x 6 = 26
5 x 7 = 31
5 x 8 = 36
5 x 9 = 41
5 x 10 = 46
5 x 11 = 51


5 x 1 = 1
5 x 2 = 6
5 x 3 = 11
5 x 4 = 16
5 x 5 = 21
5 x 6 = 26
5 x 7 = 31
5 x 8 = 36
5 x 9 = 41
5 x 10 = 46
5 x 11 = 51
Loop ko chodkar nikal gaya


5 x 1 = 1
5 x 2 = 6
5 x 3 = 11
5 x 4 = 16
5 x 5 = 21
5 x 6 = 26
5 x 7 = 31
5 x 8 = 36
5 x 9 = 41
5 x 10 = 46


5 x 1 = 1
5 x 2 = 6
5 x 3 = 11
5 x 4 = 16
5 x 5 = 21
5 x 6 = 26
5 x 7 = 31
5 x 8 = 36
5 x 9 = 41
5 x 10 = 46
Skip the iteration
5 x 12 = 56


0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
"""