import networkx as nx
import matplotlib.pyplot as plt

# Course prereqs from the file
course_prereq = {
    "CS 1411": [],
    "MATH 1451": [],
    "ENGL 1301": [],
    "CS 1412": ["CS 1411"],
    "MATH 1452": ["MATH 1451"],
    "PHYS 1408": ["MATH 1451"],
    "ENGL 1302": ["ENGL 1301"],
    "CS 2413": ["CS 1412"],
    "CS 1382": ["CS 1411"],
    "ECE 2372": ["MATH 1451"],
    "MATH 2450": ["MATH 1452"],
    "PHYS 2401": ["PHYS 1408"],
    "CS 2350": ["CS 1412", "ECE 2372"],
    "CS 2365": ["CS 2413"],
    "ENGR 2392": [],
    "POLS 1301": [],
    "MATH 2360": ["MATH 1452"],
    "ENGL 2311": ["ENGL 1301", "ENGL 1302"],
    "CS 3361": ["CS 2413"],
    "CS 3364": ["CS 2413", "CS 1382", "MATH 2360"],
    "MATH 3342": ["MATH 2450"],
    "POLS 2306": [],
    "CS 3365": ["CS 2365", "CS 2413", "MATH 3342"],
    "CS 3375": ["CS 2350"],
    "CS 3383": ["CS 1382"],
    "CS 4365": ["CS 3365"],
    "CS 4352": ["CS 3364", "CS 3375"],
    "CS 4354": ["CS 3364"],
    "CS 4366": ["CS 4365"]
}

# This is the code need to create a directed graph
G = nx.DiGraph()

# funtion used to add those courses above to the graph
G.add_nodes_from(course_prereq.keys())

# this will add the prereq of the courses to the graph so basically sort them so that it matches up with topological ordering
for course, prerequisites in course_prereq.items():
    for prereq in prerequisites:
        G.add_edge(prereq, course)

# This will be the code used to preform the topological sorting method needed with DFS (Depth first Search)
topological_order = list(nx.topological_sort(G))

# shows all of the post-visiting numbers starting from 1 going up to 29
post_visit = {course: idx + 1 for idx, course in enumerate(topological_order)}

# As well as displaying it in the graph the code will also print the topological ordering of the graph into the console.
print("Topological Order of the courses with PVM (Post-Visiting Numbers:")
for course in topological_order:
    print(f"{course} - PVM: {post_visit[course]}")

# Just changes to the layout of the graph and spacing
pos = nx.spring_layout(G, k=1.0, iterations=1)

# Draws the graph up then proceeds to label nodes with post-visiting numbers
plt.figure(figsize=(10, 10))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='yellow', font_size=8, font_color='black', font_weight='bold')

# Adds the PVM as labels to nodes
labels = {course: f"{post_visit[course]}" for course in topological_order}
nx.draw_networkx_labels(G, pos, labels, font_size=25, verticalalignment='top', horizontalalignment='center')


plt.title("ADT GRAPH")
plt.show()
