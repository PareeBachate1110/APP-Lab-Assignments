def knapsack_bottom_up(values, weights, W):
    n = len(values)

    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]              #create DP Table

    for i in range(1, n + 1):
        for w in range(W + 1):

            if weights[i - 1] <= w:                                     #if weight of item is less than current capacity
                dp[i][w] = max(
                    dp[i - 1][w],                                       #exclude current item
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]       #include current item
                )
            else:
                dp[i][w] = dp[i - 1][w]         #exclude the item as it exceeds current weight

    return dp[n][W]             #return maximum obtainable value


def knapsack_top_down(values, weights, W):
    n = len(values)
    memo = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]           #creates a table filled with -1 meaning we havent calculated best value yet 

    def solve(i, w):
        if i == 0 or w == 0:                            #No items or no capacity
            return 0

        if memo[i][w] != -1:                            #checks if previously calculated
            return memo[i][w]

        if weights[i - 1] <= w:                         #Check if current item can fit
            memo[i][w] = max(
                solve(i - 1, w),
                solve(i - 1, w - weights[i - 1]) + values[i - 1]
            )
        else:
            memo[i][w] = solve(i - 1, w)        #skip if item too heavy

        return memo[i][w]                       # Start with all items and full capacity

    return solve(n, W)                         # Start with all items and full capacity


# Example Input
values = [60, 100, 120]
weights = [10, 20, 30]
W = 50

print("Bottom-Up Approach:", knapsack_bottom_up(values, weights, W))
print("Top-Down Approach:", knapsack_top_down(values, weights, W))
