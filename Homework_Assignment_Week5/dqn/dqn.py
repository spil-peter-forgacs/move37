'''

Make a Bipedal Robot Walk in a Simulation.

It uses:
* OpenAI Gym for the environment.
* DQN Agent with Keras

This solution is based on:
* https://keon.io/deep-q-learning/
* https://github.com/keon/deep-q-learning/blob/master/dqn.py

How to run:
python dqn.py

'''

import random
import gym
import numpy as np
from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

EPISODES = 1000

'''
The DQN Agent
'''
class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size

        # Previous experiences and observations to re-train the model.
        self.memory = deque(maxlen=2000)

        # Discount rate.
        self.gamma = 0.95
        # Exploration rate.
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.999
        self.learning_rate = 0.001

        self.model = self._build_model()

    '''
    Building Neural Net for Deep-Q learning Model.
    @return model
    '''
    def _build_model(self):
        # Using sequential model.
        model = Sequential()
        # First layer with observation space size.
        model.add(Dense(48, input_dim=self.state_size, activation='relu'))
        # Hidden layers.
        model.add(Dense(36, activation='relu'))
        model.add(Dense(24, activation='relu'))
        # Last layer with action space size.
        model.add(Dense(self.action_size, activation='linear'))
        # Loss is Mean Square Error and optimizer is Adam.
        model.compile(loss='mse',
                      optimizer=Adam(lr=self.learning_rate))
        return model

    '''
    Remember
    '''
    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    '''
    Choose an action.
    @param state - Current state
    @return action
    '''
    def act(self, state):
        # Exploration.
        if np.random.rand() <= self.epsilon:
            return np.random.randn(self.action_size)
        # Exploitation.
        act_values = self.model.predict(state)
        return act_values[0]

    '''
    Replay
    '''
    def replay(self, batch_size):
        # Sample some experiences.
        minibatch = random.sample(self.memory, batch_size)

        # Extract information from the experience.
        for state, action, reward, next_state, done in minibatch:

            # At the end the target is the reward.
            target = reward

            if not done:
                # Our target is the expected future discounted reward.
                target = (reward + self.gamma *
                          np.amax(self.model.predict(next_state)[0]))

            # Predicted future reward.
            target_f = self.model.predict(state)
            target_f[0] = action * target

            # Train the network.
            self.model.fit(state, target_f, epochs=1, verbose=0)

        # Lower the exploration rate.
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    '''
    Load trained model
    '''
    def load(self, name):
        self.model.load_weights(name)

    '''
    Save trained model
    '''
    def save(self, name):
        self.model.save_weights(name)


if __name__ == "__main__":
    # OpenAI Gym Bipedal Walker
    # https://github.com/openai/gym/wiki/BipedalWalker-v2
    env = gym.make('BipedalWalker-v2')

    state_size = env.observation_space.shape[0]

    action_size = env.action_space.shape[0]

    agent = DQNAgent(state_size, action_size)

    # Optional: Load the model.
    # agent.load("./save/BipedalWalker-dqn.h5")

    done = False
    batch_size = 32

    for e in range(EPISODES):

        # New episode: reset the environment.
        state = env.reset()
        state = np.reshape(state, [1, state_size])

        for time in range(500):
            # Optional: Rendering the scene.
            # env.render()

            # Choose action.
            action = agent.act(state)

            # Interaction with the environment.
            next_state, reward, done, _ = env.step(action)

            reward = reward if not done else -10

            next_state = np.reshape(next_state, [1, state_size])

            agent.remember(state, action, reward, next_state, done)

            state = next_state

            # User feedback on the end of all episodes.
            if done:
                print("episode: {}/{}, score: {}, e: {:.2}"
                      .format(e, EPISODES, time, agent.epsilon))
                break

            if len(agent.memory) > batch_size:
                agent.replay(batch_size)

        # Optional: Save the model.
        # if e % 10 == 0:
        #     agent.save("./save/BipedalWalker-dqn.h5")
