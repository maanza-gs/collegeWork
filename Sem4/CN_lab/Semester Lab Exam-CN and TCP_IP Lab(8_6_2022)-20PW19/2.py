paths = [[1,1,0,0,0,1],
         [1,1,1,0,1,1],
         [0,1,1,1,1,0],
         [0,0,1,1,0,0],
         [0,1,1,0,1,1],
         [1,1,0,0,0,1]]

nodes = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5}
node = ['A','B','C','D','E','F']

distance = [[0,1,0,0,0,1],
            [1,0,1,0,3,3],
            [0,1,0,1,1,0],
            [0,0,1,0,0,0],
            [0,3,1,0,0,2],
            [1,3,0,0,2,0]]

visited = []

nextHop = [2,4,6,7,0]

start = 0
end = 0

def routeFind(paths, start, end):
    visited.append(start)
    for i in range(len(paths)):
        if len(visited)==0:
            i = nodes[start]
        else:
            i = nodes[visited[-1]]
        minD = max(distance[i])
        for j in range(0,6):
            if(paths[i][j]!=0):
                if(distance[i][j]<=minD and distance[i][j]!=0 and node[j] not in visited):
                    minD = max(distance[j])
                    for k in range(0,6):
                        if(paths[j][k]!=0):
                            if(distance[j][k]<=minD and distance[j][k]!=0 and node[k] not in visited):
                                visited.append(node[j])
                                break
                    break
        if (j == nodes[end]):
            break           
             
    if end not in visited:
        visited.append(end)   
        
    print(visited)
    
def routingTable(paths):

    for i in range(len(paths)):
        print(f"\n Node {node[i]}")
        print('Node  |\tCost  |\tNext Hop')
        print('------------------------')
        for j in range(0,6):
            if (distance[i][j]!=0 or i==j):
                print(node[j],distance[i][j],node[j],sep="\t\t  ")
            else:
                print(node[j],"*",'-',sep="\t\t  ")

    
#after A crashes
for j in range(1,6):
    paths[j][0] = 0
    distance[j][0] = 0
    distance[0][j] = 0
    paths[0][j] = 0
 

visited = []
print("Please type the node letters in capitals (A,B,C,D,E,F)")
print("After Network A crashes\nEnter Source Node: ")
start = input()
print("Enter Destination Node: ")
end = input()
routeFind(paths, start, end)
routingTable(paths)



