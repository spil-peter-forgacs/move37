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
Here are additional MADDPG solutions for particle environment written in Tensorflow and Pytorch.

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
