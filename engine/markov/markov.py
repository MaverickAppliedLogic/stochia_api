import random
import numpy as np


def build_transition_matrix(states, flat_probs):
    n = len(states)
    matrix = []

    for i in range(n):
        row = flat_probs[i*n : (i+1)*n]
        matrix.append(row)

    transitions = {
        states[i]: {
            states[j]: matrix[i][j]
            for j in range(n)
        }
        for i in range(n)
    }

    return transitions


def state_change(state, transitions: dict) -> str:
    states = list(transitions[state].keys())
    probs = list(transitions[state].values())
    return random.choices(population=states, weights=probs)[0]


def sim_markov(init_state: str, transitions: dict, steps: int) -> dict:
    state = init_state
    record = [state]

    for _ in range(steps):
        state = state_change(state, transitions)
        record.append(state)

    return record


def convergence_from_path(path, states):
    path_arr = np.array(path)
    total = len(path_arr)
    return [(path_arr == s).sum() / total for s in states]



def gen_sim_markov(states, probs, init_state, steps)->dict:
    transitions = build_transition_matrix(states, probs)
    path = sim_markov(init_state, transitions, steps)
    conv = convergence_from_path(path, states)

    return {
        "path": path,
        "probs": transitions,
        "conv": conv
    }


