import random


def state_change(state, transitions: dict)-> str:
    states = list(transitions[state].keys())
    probs = list(transitions[state].values())
    return random.choices(population=states,weights= probs)[0]


def sim_markov(init_state: str, transitions: dict, steps: int):
    state = init_state
    record = [state]

    for _ in range(steps):
        state = state_change(state, transitions)
        record.append(state)

    return record
