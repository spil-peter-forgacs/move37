# move37

This repository is related to:
* [https://www.theschool.ai/courses/move-37-course/](https://www.theschool.ai/courses/move-37-course/)
* [https://github.com/colinskow/move37](https://github.com/colinskow/move37)

## Homework_Assignment_Week2

This solution is based on:
* [https://github.com/aaksham/frozenlake](https://github.com/aaksham/frozenlake)

### How to run
```
cd Homework_Assignment_Week2
python DeterministicFrozenLake.py
```

## Homework_Assignment_Week3

This solution is based on:
* [https://oneraynyday.github.io/ml/2018/05/24/Reinforcement-Learning-Monte-Carlo/#example-cliff-walking](https://oneraynyday.github.io/ml/2018/05/24/Reinforcement-Learning-Monte-Carlo/#example-cliff-walking)

### How to run
```
cd Homework_Assignment_Week3
python blackjack.py

python CliffWalking.py
```

## Midterm Assignment: Make a Bipedal Robot Walk (Week5)

### Task

[https://www.theschool.ai/courses/move-37-course/lessons/midterm-assignment-make-a-bipedal-robot-walk/](https://www.theschool.ai/courses/move-37-course/lessons/midterm-assignment-make-a-bipedal-robot-walk/)

_"The midterm is to make a bipedal humanoid robot walk in a simulation._  
_You can use OpenAI Gym for the environment._  
_[https://github.com/search?q=bipedal+gym](https://github.com/search?q=bipedal+gym)_  
_This link shows some potential solutions that you can use to help you when you build your own._

_We’re looking for good documentation, readable code, and bonus points for using reinforcement learning in a novel way for this challenge."_

### Solution

This assigment has two solutions:
* DQN
* A2C

#### DQN

This solution is based on:
* [https://keon.io/deep-q-learning/](https://keon.io/deep-q-learning/)
* [https://github.com/keon/deep-q-learning/blob/master/dqn.py](https://github.com/keon/deep-q-learning/blob/master/dqn.py)

##### How to run
```
cd Homework_Assignment_Week5/dqn/
python dqn.py
```

#### A2C

This solution is based on:
* Deep Reinforcement Learning Hands-On by Maxim Lapan  
  [https://www.packtpub.com/big-data-and-business-intelligence/deep-reinforcement-learning-hands](https://www.packtpub.com/big-data-and-business-intelligence/deep-reinforcement-learning-hands)

Chapter 14 & Chapter 15:
* Continuous Action Space, The Actor-Critic (A2C) method
* Trust Regions – TRPO, PPO, and ACKTR

##### How to run
```
cd Homework_Assignment_Week5/a2c/
python 01_train_a2c.py --name bipedal --cuda
python 02_play.py --model saves/a2c-bipedal/<<your data file>>.dat --save 45
```

## Homework_Assignment_Week6

This solution is based on:
* [https://github.com/AndersonJo/dqn-pytorch](https://github.com/AndersonJo/dqn-pytorch)

## Homework_Assignment_Week7

This solution is based on:
* [https://github.com/ikergarcia1996/NeuroEvolution-Flappy-Bird](https://github.com/ikergarcia1996/NeuroEvolution-Flappy-Bird)  
  [https://github.com/ikergarcia1996/NeuroEvolution-Flappy-Bird/blob/master/Jupyter%20Notebook/Flappy.ipynb](https://github.com/ikergarcia1996/NeuroEvolution-Flappy-Bird/blob/master/Jupyter%20Notebook/Flappy.ipynb)
* [https://www.youtube.com/watch?v=h2Uhla6nLDU&feature=youtu.be](https://www.youtube.com/watch?v=h2Uhla6nLDU&feature=youtu.be)  
  [https://github.com/f-prime/FlappyBird/blob/master/flappybird.py](https://github.com/f-prime/FlappyBird/blob/master/flappybird.py)

### How to run
```
cd Homework_Assignment_Week7/FlappyBird/
python flappybird.py
```

### How to run
```
cd Homework_Assignment_Week7/NeuroEvolution-Flappy-Bird/
python flappy.py
```

## Homework_Assignment_Week8

### Solution 1: REINFORCE

This solution is based on:
* [https://github.com/simoninithomas/Deep_reinforcement_learning_Course/blob/master/Policy%20Gradients/Cartpole/Cartpole%20REINFORCE%20Monte%20Carlo%20Policy%20Gradients.ipynb](https://github.com/simoninithomas/Deep_reinforcement_learning_Course/blob/master/Policy%20Gradients/Cartpole/Cartpole%20REINFORCE%20Monte%20Carlo%20Policy%20Gradients.ipynb)

#### How to run
```
cd Homework_Assignment_Week8/Deep_reinforcement_learning_Course/
jupyter notebook Lunar\ Lander\ REINFORCE\ Monte\ Carlo\ Policy\ Gradients.ipynb
```

### Solution 2: REINFORCE

This solution is based on:
* [https://leimao.github.io/article/REINFORCE-Policy-Gradient/](https://leimao.github.io/article/REINFORCE-Policy-Gradient/)
* [https://github.com/leimao/OpenAI_Gym_AI/tree/master/LunarLander-v2/REINFORCE/2017-05-24-v1](https://github.com/leimao/OpenAI_Gym_AI/tree/master/LunarLander-v2/REINFORCE/2017-05-24-v1)

#### How to run
```
cd Homework_Assignment_Week8/OpenAI_Gym_AI
python OpenAI.py -m train
python OpenAI.py -m test
```

## Homework_Assignment_Week9

### Re-implement A2C but in Tensorflow

This solution is based on:
* [https://github.com/ikostrikov/pytorch-a3c](https://github.com/ikostrikov/pytorch-a3c)


## Final Project (Multi Agent Research Project) (Week10)

### Task

_"Reproduce the Deep Deterministic Policy Gradients algorithm for a multi-agent particle environment._  
_The algorithm should learn how to get both agents to ‘tag’ each other."_

### Suggested readings
* [Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments](https://arxiv.org/pdf/1706.02275.pdf)
* [Continuous control with deep reinforcement learning](https://arxiv.org/pdf/1509.02971.pdf)

### Solution - Tensorflow

This solution is based on:
* [https://github.com/rohan-sawhney/multi-agent-rl](https://github.com/rohan-sawhney/multi-agent-rl)
* [https://github.com/openai/multiagent-particle-envs](https://github.com/openai/multiagent-particle-envs)
* [https://github.com/camellyx/10707-deep-learning-project](https://github.com/camellyx/10707-deep-learning-project)

#### How to run

- To install, `cd Homework_Assignment_Week10/tensorflow1_multiagent` into the directory and type `pip install -e .`

- Known dependencies: Python (3.5.4), OpenAI gym (0.9.5), numpy (1.13.1)

- Additional installation instructions: [https://github.com/openai/multiagent-particle-envs](https://github.com/openai/multiagent-particle-envs)

```
cd Homework_Assignment_Week10/tensorflow1_multiagent

python3 ddpg_tag.py --env simple_tag_guided --experiment_prefix ./results/ddpg_1v1/

python3 ddpg_tag.py --env simple_tag_guided_1v2 --experiment_prefix ./results/ddpg_1v2/

python3 ddpg_tag.py --env simple_tag_guided_2v1 --experiment_prefix ./results/ddpg_2v1/

python3 ddpg_tag.py --env simple_tag_guided_2v2 --experiment_prefix ./results/ddpg_2v2/

python3 maddpg_tag.py --env simple_tag_guided --experiment_prefix ./results/maddpg_1v1/

python3 maddpg_tag.py --env simple_tag_guided_1v2 --experiment_prefix ./results/maddpg_1v2/

python3 maddpg_tag.py --env simple_tag_guided_2v1 --experiment_prefix ./results/maddpg_2v1/

python3 maddpg_tag.py --env simple_tag_guided_2v2 --experiment_prefix ./results/maddpg_2v2/
```

Use ` --render` parameter for rendering the process.

### Other solutions

**Please, use the solution above for testing.**  
Here are additional codes related written in Tensorflow and Pytorch.

#### Tensorflow 2
`cd Homework_Assignment_Week10/tensorflow2_maddpg`

This solution is based on:
* [https://github.com/openai/maddpg](https://github.com/openai/maddpg)
* [https://github.com/google/maddpg-replication](https://github.com/google/maddpg-replication)

#### PyTorch 1
`cd Homework_Assignment_Week10/pytorch1_maddpg`

This solution is based on:
* [https://github.com/xuehy/pytorch-maddpg](https://github.com/xuehy/pytorch-maddpg)
* [https://github.com/sisl/MADRL](https://github.com/sisl/MADRL)

#### PyTorch 2
`cd Homework_Assignment_Week10/pytorch2_maddpg`

This solution is based on:
* [https://github.com/shariqiqbal2810/maddpg-pytorch](https://github.com/shariqiqbal2810/maddpg-pytorch)

#### PyTorch 3
`cd Homework_Assignment_Week10/pytorch3_maddpg_mpe`

This solution is based on:
* [https://github.com/xuemei-ye/maddpg-mpe](https://github.com/xuemei-ye/maddpg-mpe)
