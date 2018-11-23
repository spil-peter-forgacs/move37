## Final Project (Multi Agent Research Project) (Week10)

### Task

_"Reproduce the Deep Deterministic Policy Gradients algorithm for a multi-agent particle environment._  
_The algorithm should learn how to get both agents to ‘tag’ each other."_

### Solution

This solution is based on:
* [https://github.com/rohan-sawhney/multi-agent-rl](https://github.com/rohan-sawhney/multi-agent-rl)

#### How to run
```
cd Homework_Assignment_Week10

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
