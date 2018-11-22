## Homework_Assignment_Week10

### Final Project (Multi Agent Research Project)

This solution is based on:
* [https://github.com/rohan-sawhney/multi-agent-rl](https://github.com/rohan-sawhney/multi-agent-rl)

#### How to run
```
cd Homework_Assignment_Week10

python3 ddpg_tag.py --env simple_tag_guided --experiment_prefix ./results/ddpg_1v1/

python3 ddpg_tag.py --env simple_tag_guided_1v2 --experiment_prefix ./results/ddpg_1v2/

python3 ddpg_tag.py --env simple_tag_guided_2v1 --experiment_prefix ./results/ddpg_2v1/

python3 ddpg_tag.py --env simple_tag_guided_2v2 --experiment_prefix ./results/ddpg_2v2/
```

Use ` --render` parameter for rendering the process.
