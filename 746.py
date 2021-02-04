def minCostClimbingStairs( cost) -> int:
    # fare=zeros(len(cost))
    length = len(cost)+1
    fare = [0 for i in range(length)]
    for i in range(2, length):
        fare[i] = min(fare[i - 1] + cost[i - 1], fare[i - 2] + cost[i - 2])
    return fare[length]

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
minCostClimbingStairs(cost)