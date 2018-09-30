import gym
env = gym.make("CliffWalking-v0")

# The typical imports
import gym
import numpy as np
import matplotlib.pyplot as plt
from mc import FiniteMCModel as MC

eps = 1000000
S = 4*12
A = 4
m = MC(S, A, epsilon=1)
for i in range(1, eps+1):
    ep = []
    observation = env.reset()
    while True:
        # Choosing behavior policy
        action = m.choose_action(m.b, observation)

        # Run simulation
        next_observation, reward, done, _ = env.step(action)
        ep.append((observation, action, reward))
        observation = next_observation
        if done:
            break

    m.update_Q(ep)
    # Decaying epsilon, reach optimal policy
    m.epsilon = max((eps-i)/eps, 0.1)

print("Final expected returns : {}".format(m.score(env, m.pi, n_samples=10000)))
