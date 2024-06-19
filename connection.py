# connection.py
from cassandra.cluster import Cluster

def get_connection():
    cluster = Cluster(['cassandra-node1', 'cassandra-node2', 'cassandra-node3', 'cassandra-node4'])
    session = cluster.connect('library')
    return session
