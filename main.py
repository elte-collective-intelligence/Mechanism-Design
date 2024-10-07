# Create a weighted graph

from logging import Logger
from Enviroment.yard import CustomEnvironment
from MetaLearning.maml import MAMLMetaLearningSystem
from RLAgent.random_agent import RandomAgent

num_agents = 2
agent_money = 10.0
env = CustomEnvironment(num_agents, agent_money)
observation_space = env.observation_space()
action_space = env.action_space()
policy = RandomAgent()
logger = Logger()
maml_system = MAMLMetaLearningSystem(policy, logger=logger)

meta_train_tasks = [CustomEnvironment(num_agents, agent_money) for _ in range(10)]
meta_test_tasks = [CustomEnvironment(num_agents, agent_money) for _ in range(5)]

maml_system.meta_train(meta_train_tasks)
maml_system.meta_evaluate(meta_test_tasks)

maml_system.save_meta_model('maml_policy.pth')