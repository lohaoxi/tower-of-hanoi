from TowerOfHanoi import *
from itertools import product
import pandas as pd
import time


def all_states(m):
    """ Produce all state for the m discs"""
    pegs = range(4)
    return list(product(pegs, repeat = m))

def convert_index(state):
    """ Convert the state tuples as indices"""
    state = list(state)
    n = len(state)
    output = [0] * n
    for i in range(n):
        output[i] = state[i] * (10 ** (n - i - 1))
        
    return sum(output)
        

def construct_PDB(m):
    """ Convert the PDB"""
    start_time = time.time()
    print("Constructing PDB...")
    states = all_states(m)
    PDB = [0] * (4 ** m)
    index = [0] * (4 ** m)
    for i in range(len(states)):
        temp = TowerOfHanoi(m, initial = states[i], goal = tuple([3] * m))
        solution_node = breadth_first_graph_search(temp)
        PDB[i] = int(len(solution_node.solution()))
        index[i] = convert_index(states[i])
        df = pd.DataFrame({'index' : index, 'h' : PDB})
        df = df.set_index('index')
    print("Running time:", time.time() - start_time)
    return df

class TowerOfHanoiPDB(TowerOfHanoi):
    """This is a subclass of the TowerOfHanoi class uniquely for the PDB heuristic"""
    
    def hPDB(self, node, PDB, m):
        h = PDB.at[convert_index(node.state[-m:]), 'h']
        return h
    
    pass



def astar_search_PDB(problem, h, PDB, m, display=False):
    """This is a A* search uniquely for the PDB heuristic"""
    return best_first_graph_search(problem, lambda n: n.path_cost + h(n, PDB, m), display)


    
    


