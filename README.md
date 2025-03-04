# CartPole-v1
An implementation of Deep Q-Network (DQN) in the CartPole-v1 environment.

# Installation
Set up the project environment with:

```bash
conda create -n gym python=3.8  
conda activate gym 
pip install -r requirements.txt
```
If you encounter package conflicts, try installing dependencies manually.

# Training
You can train the agent with 
```bash
python train.py
```

You can customize the training process with various arguments.  
See `arguments.py` for more details, including:
`lr`: Learning rate for the optimizer
`batch_size`: Batch_size for training
`gamma`: Discount factor

# Logs&Checkpoints

Training logs and checkpoints will be saved in:`logs/env{env you choose}-yyyymmdd-hhmmss` after experiment.
For example
```bash
logs/env-CartPole-v1-20250304-120000/
```

To visualize logs in TensorBoard, use:
```
tensorboard --logdir=logs
```



# Testing
After training the agent, you can test it using `test.py`:
```bash
python test.py --weight-path {w_path}
```
Replace `{w_path}` with your actual weight file path.








<!--stackedit_data:
eyJoaXN0b3J5IjpbMTkxMDAxNjQ5MSwtMTc4NTEzMjUwNCwxND
E2MDk2NDA5LDEzNTcxMTEyMDMsMTE2NDU0Mzc3NF19
-->