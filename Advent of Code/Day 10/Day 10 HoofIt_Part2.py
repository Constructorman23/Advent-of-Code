def count_trail(grid,pos,current_height,memo):
    i, j = pos
    
    if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
        return 0
    if grid[i][j] != current_height:
        return 0
    if grid[i][j] == 9:
        return 1
    
    if (i,j,current_height) in memo:
        return memo[(i, j, current_height)]
    
    total_trails = 0
    for di, dj in [(-1,0),(0,1),(1,0),(0,-1)]:
        total_trails += count_trail(grid,(i+di,j+dj),current_height+1,memo)
        
    memo[(i, j, current_height)] = total_trails
        
    return total_trails

with open('Day 10/input.txt', 'r') as file:
    grid = file.read().splitlines()

grid= list(grid)
for i in range(len(grid)):
    grid[i] = list(map(int,grid[i]))

trailheads_pos= set()
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 0:
            pos = (i,j)
            trailheads_pos.add(pos)
total = 0           
for trailhead in trailheads_pos:
    trailscore = 0
    memo = {}
    trails = count_trail(grid,trailhead,0,memo)
    total+= trails
    
print(total)