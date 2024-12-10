def explore_trail(grid,pos,visited,current_height):
    i, j = pos
    
    if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
        return set()
    if pos in visited or grid[i][j] != current_height:
        return set()
    if grid[i][j] == 9:
        return {pos}
    
    results = set()
    
    for di, dj in [(-1,0),(0,1),(1,0),(0,-1)]:
        results.update(explore_trail(grid,(i+di,j+dj),visited,current_height+1))
    
    visited.add(pos)
    
    return results

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
    visited = set()
    trails = explore_trail(grid,trailhead,visited,0)
    total+=len(trails)
    
print(total)