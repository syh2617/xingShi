import csv
import py2neo
from py2neo import Graph, Node, Relationship

# 连接到 Neo4j 数据库
graph = Graph("bolt://localhost:7687", auth=("neo4j", "123syh123"))

# 创建节点
person1 = Node("Person", name="Alice")
person2 = Node("Person", name="Bob")

# 创建关系
knows = Relationship(person1, "KNOWS", person2)

# 将节点和关系添加到图数据库中
graph.create(person1)
graph.create(person2)
graph.create(knows)

# 查询数据
query = "MATCH (p:Person)-[k:KNOWS]->(p2:Person) WHERE p.name = 'Alice' RETURN p, k, p2"
result = graph.run(query)

# 打印查询结果
for record in result:
    print(record)

# 执行 Cypher 查询删除所有节点和关系
graph.run("""MATCH (n) DETACH DELETE n""")