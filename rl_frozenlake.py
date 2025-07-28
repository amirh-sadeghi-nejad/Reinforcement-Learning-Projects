
import gym
print(gym.__version__)

import gym

env = gym.make("FrozenLake-v1", render_mode="human")

for i in range(20):
  env.reset()
  print(f"time step:{i}")
  print("Next state:", next_state)
  print("Reward:", reward)
  print("Done:", done)
  print("Info:", info)
  while True:

    action = env.action_space.sample()
    next_state, reward, done, info = env.step(action)

    env.render()
    if done:
      break
print("Next state:", next_state)
print("Reward:", reward)
print("Done:", done)
print("Info:", info)

env.close()