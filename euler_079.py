import networkx as nx


def create_graph():
  graph = nx.DiGraph()

  for i in xrange(10):
    graph.add_node(str(i))

  return graph


if __name__ == '__main__':
  with open('res/p079_keylog.txt', 'r') as f:
    graph = create_graph()

    for line in f:
      numbers = line.strip()

      for i in xrange(len(numbers) - 1):
        if numbers[i + 1] not in graph[numbers[i]]:
          graph.add_edge(numbers[i], numbers[i + 1])

    top_sort = nx.algorithms.topological_sort(graph)

    # remove disconnected nodes
    print ''.join([x for x in top_sort if len(graph.in_edges(x)) != 0 or len(graph.out_edges(x)) != 0])