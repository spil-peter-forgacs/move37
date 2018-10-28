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
