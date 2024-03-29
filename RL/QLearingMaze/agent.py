# -*- coding:utf-8 -*-
import numpy as np

# Q 矩阵初始化为0
q = np.matrix(np.zeros([6, 6]))
print(q)
# Reward 矩阵为提前定义好的。 类似与HMM的生成矩阵。-1表示无相连接的边
r = np.matrix([[-1, -1, -1, -1,  0,  -1],
               [-1, -1, -1,  0, -1, 100],
               [-1, -1, -1,  0, -1,  -1],
               [-1,  0,  0, -1,  0,  -1],
               [ 0, -1, -1,  0, -1, 100],
               [-1,  0, -1, -1,  0, 100]])

#折扣因子
gamma = 0.8

a = 0.2
#是否选择最后策略的概率
epsilon = 0.4
# the main training loop
for episode in range(10000001):
    # random initial state
    state = np.random.randint(0, 6)
    print("random initial state:",state)
    # 如果不是最终转态
    while (True):
        # 选择可能的动作
        # Even in random case, we cannot choose actions whose r[state, action] = -1.
        possible_actions = []
        possible_q = []
        for action in range(6):
            if r[state, action] >= 0:
                possible_actions.append(action)
                possible_q.append(q[state, action])

        # Step next state, here we use epsilon-greedy algorithm.
        action = -1
        if np.random.random() < epsilon:
            # choose random action
            action = possible_actions[np.random.randint(0, len(possible_actions))]
        else:
            # greedy
            action = possible_actions[np.argmax(possible_q)]

        # Update Q value
        #q[state, action] = r[state, action] + gamma * [q[action].max() ]
        q[state, action] = q[state, action] + a * (r[state, action] + gamma * q[action].max() - q[state, action])

        # Go to the next state
        state = action

        if (state == 5):
            break

        # Display training progress
    if episode % 10 == 0:
        print("------------------------------------------------")
        print("Training episode: %d" % episode)
        print(q/5)