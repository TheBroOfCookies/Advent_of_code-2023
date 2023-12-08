class Node: #solution: 19199
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right
    
    def __str__(self):
        return f"Node: {self.name} ({self.left},{self.right})"

def find_zzz(filename):
    nodes = []
    directions = ""
    current_node = 0
    with open(filename) as file:
        lines = file.readlines()
        directions = lines[0].strip()
        for line in lines[2:]:
            name, rest = line.strip().split("=")
            left, right = rest.replace("(", "").replace(")", "").split(",")
            node = Node(name.strip(), left.strip(), right.strip())
            nodes.append(node)
            if node.name == "AAA":
                current_node = node
    print(directions)
    steps = 0
    while True:
        for d in directions:
            next_node = ""
            if d == "L":
                next_node  = current_node.left
            else: 
                next_node  = current_node.right
            steps += 1
            if next_node == "ZZZ":
                return steps
            
            for n in nodes:
                if n.name == next_node:
                    current_node = n
                    break
                
            
 
print(find_zzz("input.txt"))
#print(find_zzz("example.txt"))