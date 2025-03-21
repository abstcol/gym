from argparse import Namespace

args = Namespace(
    # 环境相关参数
    env_name="Acrobot-v1",  # Gymnasium 环境名称 (默认: MountainCar-v0)
    terminate_reward=100,  # 环境终止奖励阈值
    asynchronous=True,    #是否并行化训练
    vec_num=6,          #并行环境数量

    # 训练相关参数
    episodes=500,  # 训练的总回合数 (默认: 1000)
    max_episode_steps=0,  # 单回合最大步数 (默认: 0，表示使用环境默认值)

    # 算法选择
    algo_name="AC_onpolicy",  # 训练算法名称 (默认: D3QN)

    # 经验回放相关参数
    batch_size=64,  # 每次训练从经验回放池中采样的样本数 (默认: 64)
    MAX_EXPERIENCE=2**17,  # 经验回放池的最大容量 (默认: 2^17)

    # DQN 学习相关参数
    gamma=0.99,  # 未来奖励折扣因子 (默认: 0.9)
    tau=1e-2,  # 目标网络软更新率 (默认: 1e-2)
    alpha=0.6,  # 经验回放中的优先级采样系数 (默认: 0.6)
    initial_beta=0.4,  # 经验回放中的重要性采样初始值 (默认: 0.4)
    increase_beta=1.0,  # 重要性采样的增长速率 (默认: 1.0)
    lr=0.0002,  # DQN 优化器的学习率 (默认: 0.001)
    use_entropy=False ,   #是否使用熵作为loss
    entro_coe=0.5,      #熵损失系数
    # 探索策略相关参数
    initial_epsilon=0.1,  # ε-贪心策略的初始值 (默认: 0.1)
    decay_epsilon=0.99,  # ε的衰减率，每个回合后乘以该值 (默认: 0.99)
    final_epsilon=0.01,  # ε的最小值 (默认: 0.01)
    prioepsilon=1e-6,  # 经验回放中优先级采样的 epsilon 值 (默认: 1e-6)
    stop_prio=False,  # 是否关闭优先级采样 (默认: False，使用优先级采样)

    # 神经网络结构相关参数
    hidden_sizes=[64, 32],  # DQN 隐藏层大小 (默认: [64, 32])

    # 训练输出与存储相关参数
    produce_gif=False,  # 是否生成训练过程的 GIF (默认: False)
    no_human_sample=False,  # 是否不使用人类样本 (默认: False)

    # wandb 权重名称
    checkpoint_name='abstcold-none/RL-Training/Acrobot-v1_D3QN_20250307-194002:v1'
    # 在 wandb 中的 checkpoint 名称
)

