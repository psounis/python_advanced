from graphlib import TopologicalSorter

graph = {
    "v1": {},
    "v2": {"v1"},
    "v3": {"v1", "v2"},
    "v4": {"v3"},
    "v5": {"v3"},
    "v6": {"v2", "v4", "v5"},
    "v7": {"v5", "v6"}
}

sorter = TopologicalSorter(graph)
order = sorter.static_order()
print(list(order))


