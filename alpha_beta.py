def alphabeta(values, depth, i, isMax, alpha, beta):
    
    # Leaf node
    if depth == 0:
        return values[i]

    if isMax:   # MAX player
        best = -999
        for j in range(2):
            val = alphabeta(values, depth-1, i*2+j, False, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break   # prune

        return best

    else:       # MIN player
        best = 999
        for j in range(2):
            val = alphabeta(values, depth-1, i*2+j, True, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break   # prune

        return best


# 🔹 USER INPUT
n = int(input("Enter number of leaf nodes (power of 2): "))
values = list(map(int, input("Enter values: ").split()))

depth = 0
temp = n
while temp > 1:
    temp //= 2
    depth += 1

result = alphabeta(values, depth, 0, True, -999, 999)
print("Optimal Value:", result)