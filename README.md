# 2048-api
A 2048 game api for training supervised learning (imitation learning) or reinforcement learning agents

# Code structure
* [`game2048/`](game2048/): the main package.
    * [`game.py`](game2048/game.py): the core 2048 `Game` class.
    * [`agents.py`](game2048/agents.py): the `Agent` class with instances.
    * [`displays.py`](game2048/displays.py): the `Display` class with instances, to show the `Game` state.
    * [`expectimax/`](game2048/expectimax): a powerful ExpectiMax agent by [here](https://github.com/nneonneo/2048-ai).
* [`explore.ipynb`](explore.ipynb): introduce how to use the `Agent`, `Display` and `Game`.
* [`static/`](static/): frontend assets (based on Vue.js) for web app.
* [`webapp.py`](webapp.py): run the web app (backend) demo.
* [`evaluate.py`](evaluate.py): evaluate your self-defined agent.

# To define your own agents
我在Agents模块中加入了一个新的类MyAgent，它继承了ExpectiMaxAgent，这样可以非常方便地调用ExpectiMaxAgent中的step()函数去获得当前棋盘的决策（高级AI模型给出的）。同时我也定义了my_step()作为我的Agent模型给出的决策。

# To train my model
在Main文件中运行相应程序即可训练模型

# To run the web app
```bash
python webapp.py
```

# LICENSE
The code is under Apache-2.0 License.
