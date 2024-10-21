from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def design(request):
    return render(request, 'grid/design.html')

class Nodes_in_astar:
    def __init__(self, pose, parent=None):       #pose= position of the node.
        self.pose = pose
        self.parent = parent
        self.g = 0  
        self.h = 0  
        self.f = 0 

def heuristic_value(a, b):                       #a= (x1,y2) , b= (x2,y2)
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar_algorithm(start, end, grid):
    open_list = []                               #open_list contains the nodes that needs to be explored
    closed_list = []                             #closed_list contains the nodes that are fully/completedly explored
    explored_nodes = []                          #explored_list contains the nodes position that is for the visualization purpose

    start_node = Nodes_in_astar(start)
    end_node = Nodes_in_astar(end)

    open_list.append(start_node)

    while open_list:
        current_node = min(open_list, key=lambda o: o.f)   #storing the minimum f valued node in the current_node

        if current_node.pose == end_node.pose:
            path = []
            while current_node:
                path.append(current_node.pose)
                current_node = current_node.parent
            return path[::-1], explored_nodes  

        open_list.remove(current_node)
        closed_list.append(current_node)
        explored_nodes.append(current_node.pose)

        x, y = current_node.pose

        neighbors = [
            (x-1, y), (x+1, y), (x, y-1), (x+1, y), 
            (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)] 
        
        for next_node in neighbors:
            if next_node[0] < 0 or next_node[0] >= len(grid) or next_node[1] < 0 or next_node[1] >= len(grid[0]):
                continue 
            if grid[next_node[0]][next_node[1]] == '1': 
                continue

            neighbor_node = Nodes_in_astar(next_node, current_node)

            if neighbor_node in closed_list:
                continue

            move_cost = 1 if (x == next_node[0] or y == next_node[1]) else 2  
            neighbor_node.g = current_node.g + move_cost
            neighbor_node.h = heuristic_value(neighbor_node.pose, end_node.pose)
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            if add_nodes(open_list, neighbor_node):
                open_list.append(neighbor_node)

    return None, explored_nodes  

def add_nodes(open_list, neighbor):
    for node in open_list:
        if neighbor.pose == node.pose and neighbor.g >= node.g:
            return False
    return True

@csrf_exempt
def my_path(request):
    if request.method == 'POST':
        data = json.loads(request.body)             #the json.loads is converting the raw data to dictionary data for easyness
        start = tuple(data['start'])                #data and json loads are python libraraies.
        end = tuple(data['end'])
        grid = data['grid']  

        path, explored = astar_algorithm(start, end, grid)

        
        if path:
            path = [p for p in path if p != start and p != end]  #the starting and ending are excluded from the visualization of explored nodes

        return JsonResponse({'path': path, 'explored': explored})

    return JsonResponse({'error': 'Invalid request'}, status=400)
