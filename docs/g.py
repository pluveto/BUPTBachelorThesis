import networkx as nx
import matplotlib.pyplot as plt

# 创建空的有向图
G = nx.DiGraph()

# 添加节点
G.add_node("数据处理")
G.add_node("训练")
G.add_node("预测")
G.add_node("收集")
G.add_node("存储")
G.add_node("更新副本数")
G.add_node("伸缩")
G.add_node("Pods")
G.add_node("HPA")

# 添加边
G.add_edge("数据处理", "训练")
G.add_edge("训练", "预测")
G.add_edge("存储", "数据处理")
G.add_edge("收集", "存储")
G.add_edge("预测", "更新副本数")
G.add_edge("更新副本数", "伸缩")
G.add_edge("伸缩", "HPA")
G.add_edge("HPA", "Pods")
G.add_edge("Pods", "收集")

# 创建四个子图
algorithm_module = nx.subgraph(G, ["数据处理", "训练", "预测"])
monitoring_module = nx.subgraph(G, ["收集", "存储"])
control_module = nx.subgraph(G, ["更新副本数", "伸缩"])
kubernetes = nx.subgraph(G, ["Pods", "HPA"])

# 设置图形布局
pos = {
    "数据处理": (0, 1),
    "训练": (1, 1),
    "预测": (2, 1),
    "收集": (0, 0),
    "存储": (1, 0),
    "更新副本数": (0, -1),
    "伸缩": (1, -1),
    "Pods": (2, -1),
    "HPA": (3, -1),
}

# 绘制子图
plt.figure(figsize=(8, 4))

plt.subplot(2, 4, 1)
nx.draw(algorithm_module, pos, with_labels=True)
plt.title("算法模块")

plt.subplot(2, 4, 2)
nx.draw(monitoring_module, pos, with_labels=True)
plt.title("监控模块")

plt.subplot(2, 4, 3)
nx.draw(control_module, pos, with_labels=True)
plt.title("控制模块")

plt.subplot(2, 4, 4)
nx.draw(kubernetes, pos, with_labels=True)
plt.title("Kubernetes")

# 隐藏坐标轴
plt.axis('off')

# 显示图形
plt.tight_layout()
plt.show()
