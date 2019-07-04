
import math
#from helpers import Map, load_map, show_map
from my_helper import Map

def getN1toN2Heuristic(MAP,node1,node2):

    node1_xy = MAP.intersections[node1]
    node2_xy = MAP.intersections[node2]
    #debug
    #print('    == getN1toN2Heuristic ==')
    #print('      node1:',node1,' -> node2:',node2)
    #print('      node1_xy:',node1_xy,'node2_xy:',node2_xy)
    rst = math.sqrt(pow((node2_xy[1]-node1_xy[1]),2) + pow((node2_xy[0]-node1_xy[0]),2))
    #print('      dis-rst:',rst)
    return rst

def getfgh(Map,node_from,node_to,goalNodes,path_cost):
    g = getN1toN2Heuristic(Map,node_from,node_to) + path_cost[node_from][1]#[f,g,h]
    h = getN1toN2Heuristic(Map,node_to,goalNodes)
    f = g + h
    return f,g,h

def addToOpenlist(openlist,node):
    openlist.append([node])

def fNodeSort(ele,path_cost):
    #f = ele[1] + ele[2]
    f = path_cost[ele[0]][0]
    return f


def ExpandNeighbors(Map,curNode,openlist,goalNodes,path_cost):

    #handle all neighbor nodes
    for node in Map.roads[curNode[0]]:
        #print(node)
        f,g,h = getfgh(Map,curNode[0],node,goalNodes,path_cost)

        if node in path_cost:
            #print('new f,g,h:',f,g,h,', path_cost[',node,'] :',path_cost[node])
            # we have a better choice to reach this node.
            if f < path_cost[node][0]:#[f,g,h,parent_node]
                #update cost info
                path_cost[node] = [f,g,h,curNode[0]]
                print('    updated existed node',node,'cost')
                #print('updated path_cost[',node,']:',path_cost[node])

        elif node not in path_cost:
            # add the node to openlist and tracking the cost directly
            addToOpenlist(openlist,node)
            path_cost[node] = [f,g,h,curNode[0]]
            #print('    add new Nieghbor:',node,f,g,h)
            print('    add new Nieghbor:',node)

        else:
            print('    node ',node, 'visited before and no better f')


def rebuild_path(parent_node,goalNodes):

    par = goalNodes
    rst = []
    while par >=0:
        rst.append(par)
        par = parent_node[par]

    rst = rst[::-1]
    print('**** RESULT: ',rst)
    return rst

def Astar(Map,startNode,goalNodes):


    #initial section
    openlist = []#for tracking node candidate
    path_cost ={}#[f,g,h,parent_node], use map for quickly check
    parent_node_rstlist = {}#for showing result

    #add the startNode
    path_cost[startNode] = [-1,-1,-1,-1]#[f,g,h,parent_node]
    parent_node_rstlist[startNode] = -1
    f,g,h = getfgh(Map,startNode,startNode,goalNodes,path_cost)
    addToOpenlist(openlist,startNode)

    step = 0
    elenum = -1
    while len(openlist) > 0 :

        #openlist.sort(key=fNodeSort)
        #print('path_cost:',path_cost)
        #print('b s',openlist)
        openlist.sort(key=lambda ele: path_cost[ele[0]][0])
        #print('a s',openlist)

        curNode = openlist.pop(0)
        parent_node_rstlist[curNode[0]] = path_cost[curNode[0]][3]#[f,g,h,parent_node]
        print('========')
        print('curnode:',curNode[0])


        if curNode[0] == goalNodes:
            print('found it')
            #print('parent_node:',parent_node[curNode[0]])
            print('max reaching out nodes',elenum)
            return rebuild_path(parent_node_rstlist,goalNodes)

        ExpandNeighbors(Map,curNode,openlist,goalNodes,path_cost)


        #debug zone
        #print('path_cost:',path_cost)
        #print(parent_node)
        if len(openlist) > elenum:
            elenum = len(openlist)
        print('end this round, openlist len:',len(openlist))
        #print('end this round:',openlist)
        #print(f,g,h)
        step +=1
        if step == 50:
            break
    print('can\'t reach the goal')
    return None


def shortest_path(Map,startNode,goalNodes):
    return Astar(Map,startNode,goalNodes)





################
# main section
################
#map_10 = load_map('./map-10.pickle')
#map_40 = load_map('./map-40.pickle')
'''
MAP_40_ANSWERS = [
    (5, 34, [5, 16, 37, 12, 34]),
    (5, 5,  [5]),
    (8, 24, [8, 14, 16, 37, 12, 17, 10, 24])
]
'''
map_40 = Map()

sta = 8
end = 24#12

#sta = 5
#end = 34

path = shortest_path(map_40,sta,end)

print(path)
