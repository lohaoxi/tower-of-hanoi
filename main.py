from TowerOfHanoi import *
from PDB import *
import time

# astar h1 
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
print("a* search h1")
for i in range(1, 9):
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Number of discs:", i)
    start_time = time.time()
    initial = tuple([0] * i)
    goal = tuple([3] * i)
    example_problem = TowerOfHanoi(i, initial, goal)
    solution_node = astar_search(example_problem, example_problem.h, display = True);
    solution_path = solution_node.path();
    print("Running time:", time.time() - start_time)
    print("Solution states:", solution_path);
    print("Solution actions:", solution_node.solution())
    print("Plan length:", len(solution_node.solution()))

# astar h2
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
print("a* search h2")
for i in range(1, 9):
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Number of discs:", i)
    start_time = time.time()
    initial = tuple([0] * i)
    goal = tuple([3] * i)
    example_problem = TowerOfHanoi(i, initial, goal)
    solution_node = astar_search(example_problem, example_problem.h2, display = True);
    solution_path = solution_node.path();
    print("Running time:", time.time() - start_time)
    print("Solution states:", solution_path);
    print("Solution actions:", solution_node.solution())
    print("Plan length:", len(solution_node.solution()))
    
# astar h3 (suboptimal)
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
print("a* search h3 (suboptimal)")
for i in range(1, 9):
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Number of discs:", i)
    start_time = time.time()
    initial = tuple([0] * i)
    goal = tuple([3] * i)
    example_problem = TowerOfHanoi(i, initial, goal)
    solution_node = astar_search(example_problem, example_problem.h3, display = True);
    solution_path = solution_node.path();
    print("Running time:", time.time() - start_time)
    print("Solution states:", solution_path);
    print("Solution actions:", solution_node.solution())
    print("Plan length:", len(solution_node.solution()))

# depth first search
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
print("depth first search")
for i in range(1, 9):
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Number of discs:", i)
    start_time = time.time()
    initial = tuple([0] * i)
    goal = tuple([3] * i)
    example_problem = TowerOfHanoi(i, initial, goal)
    solution_node = depth_first_graph_search(example_problem)
    solution_path = solution_node.path();
    print("Running time:", time.time() - start_time)
    print("Plan length:", len(solution_node.solution()))

# PDB
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
m = 5
PDB = construct_PDB(m)
print("a* search with PDB")
for i in range(m + 1, 9):
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Number of discs:", i)
    start_time = time.time()
    initial = tuple([0] * i)
    goal = tuple([3] * i)
    example_problem = TowerOfHanoiPDB(i, initial, goal)
    solution_node = astar_search_PDB(example_problem, example_problem.hPDB, PDB, m, display = True);
    solution_path = solution_node.path();
    print("Running time:", time.time() - start_time)
    print("Solution states:", solution_path);
    print("Solution actions:", solution_node.solution())
    print("Plan length:", len(solution_node.solution()))


