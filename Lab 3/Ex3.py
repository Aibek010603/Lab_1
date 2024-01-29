def solve(numheads, numlegs):
    # Solving for r (rabbits)
    r = (numlegs - 2 * numheads) / 2
    
    # Solving for c (chickens) 
    c = numheads - r
    
    if r.is_integer() and c.is_integer() and r >= 0 and c >= 0:
        return int(c), int(r)
    else:
        return "No solution"

numheads = 35
numlegs = 94
chickens, rabbits = solve(numheads, numlegs)
print(f"Chickens: {chickens}, Rabbits: {rabbits}")
