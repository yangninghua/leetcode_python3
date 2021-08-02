'''

在一条水平的公路上建有n个小屋，两个小屋间的距离是它们的横坐标之差的绝对值。保证小屋的横坐标是整数，以及没有两个小屋建立在同一位置。现在需要建立m所加油站(m<=n)，加油站只能建立在小屋所在的位置。
现在需要你写个程序，给定了所有小屋的位置和加油站的数目，计算出每个小屋离最近的加油站的距离总和的最小值。

输入：
第一行包括两个整数n和m: 1 <= n <= 300, 1 <= m <= 30, m <= n. 第二行包括n个整数，代表小屋的位置，以升序的形式列出。对于每一个整数x，1 <= X <= 10000.


输出：
输出距离总和的最小值。


样本输入
10 5
1 2 4 6 7 10 11 25 44 70

样本输出
11
'''

# '''
# https://www.acwing.com/problem/content/description/106/
# '''
# #N = raw_input() python2
# #N = input() python3
# N = input()
# N_1_N = list(map(int,input().split()))
# N_1_N.sort(reverse=False)

# result = 0
# mid = 0
# num = len(N_1_N)
# #oushu
# if num % 2 == 0:
#     mid = N_1_N[num//2]
#     for i in range(num):
#         result += abs(N_1_N[i] - mid)
# else:
#     mid = N_1_N[num//2]
#     for i in range(num):
#         result += abs(N_1_N[i] - mid)
# print(result)

'''
https://www.acwing.com/problem/content/338/
10 5
1 2 3 6 7 9 11 22 44 50
0	0	0	0	0	0	0	0	0	0	0	
0	0	1	2	6	10	16	21	37	74	117	
0	0	0	1	4	8	11	16	31	68	109	
0	0	0	0	3	4	7	11	26	61	102	
0	0	0	0	0	1	3	7	20	55	94	
0	0	0	0	0	0	2	4	17	50	89	
0	0	0	0	0	0	0	2	13	46	74	
0	0	0	0	0	0	0	0	11	33	61	
0	0	0	0	0	0	0	0	0	22	28	
0	0	0	0	0	0	0	0	0	0	6	
0	0	0	0	0	0	0	0	0	0	0	
1061109567	1061109567	1061109567	1061109567	1061109567	1061109567	
1061109567	0	1061109567	1061109567	1061109567	1061109567	
1061109567	1	0	1061109567	1061109567	1061109567	
1061109567	2	1	0	1061109567	1061109567	
1061109567	6	2	1	0	1061109567	
1061109567	10	3	2	1	0	
1061109567	16	5	3	2	1	
1061109567	21	9	5	3	2	
1061109567	37	21	9	5	3	
1061109567	74	37	21	9	5	
1061109567	117	43	27	15	9	
9
'''
N, P = 10,5
N_1_n = [1,2,3,6,7,9,11,22,44,50]
N_1_n.sort(reverse=False)

# N, P = map(int, input().split())
# N_1_n = list(map(int, input().split()))
# N_1_n.sort(reverse=False)
'''
1.dist[i][j]第i个村庄到第j个村庄之间建1个邮局的最小距离和
2.dist[i][j] = dist[i][j-1] + abs(a-b)
3.初始化[0][j] [i][0]=0
[i][j] [j][i]是对称的，可对称初始化
4.遍历从上到下，从左到右
'''
dist = [[200000000000]*(N+1) for _ in range(N+1)]
for i in range(1, N+1, 1):
    dist[i][i] = 0

for i in range(1, N+1-1, 1):
    dist[i][i] = 0
    for j in range(i+1, N+1-0, 1):
        a = N_1_n[j-1]
        b = N_1_n[(i-1+j-1)//2]
        dist[i][j] = dist[i][j-1]+ abs(a-b)
        dist[j][i] = dist[i][j]
#dp[i][j] 前i个村庄建j个邮局的最小距离和
dp = [[100000000000]*(P+1) for _ in range(N+1)]
for temp in range(N+1):
    dp[temp][1] = dist[1][temp]
for j in range(2, P+1, 1):
    #建立j个邮局
    for i in range(j, N+1, 1):
        #1-i个村庄建立j邮局
        for k in range(j-1, i, 1):
        #for k in range(1, (i-1)+1, 1):
        #1-k个村庄建立j-1个邮局
        # =min(
        #     [前1个村庄建j-1个邮局的最小距离和 + 第2到第i个村庄建1个邮局的最小距离和]
        #     [前2个村庄建j-1个邮局的最小距离和 + 第3到第i个村庄建1个邮局的最小距离和]
        #     [前3个村庄建j-1个邮局的最小距离和 + 第4到第i个村庄建1个邮局的最小距离和]
        #     [前4个村庄建j-1个邮局的最小距离和 + 第5到第i个村庄建1个邮局的最小距离和]
        #     [前i-1个村庄建j-1个邮局的最小距离和 + 第i到第i个村庄建1个邮局的最小距离和]
            dp[i][j] = min(dp[i][j], dp[k][j-1]+dist[k+1][i])
            # if j==P and i==N:
            #     print("dist[k+1][i]", dist[k+1][i], k+1, i)‘
# for i in range(1, N+1, 1):
#     for j in range(2, P+1, 1):
#         for k in range(1, (i-1)+1, 1):
#             dp[i][j] = min(dp[i][j], dp[k][j-1]+dist[k+1][i])
#             print(i,j, ":", k,j-1)
import pprint
pprint.pprint(dp)
print(dp[N][P])

'''
1.dp[i][j] 前i个村庄建P个邮局的最小距离和
2.dp[i][j] = dp[i][j-1] + min()
3.初始化
dp[0][0]=100000
dp[0][j]=100000
dp[i][0]=100000
dp[i][1] = dist[1][i]

4.由于已知dp[i][1] 未知的是dp[i][2] dp[i][3]
dp遍历，已知前i个村庄建1个邮局的最小距离和
'''