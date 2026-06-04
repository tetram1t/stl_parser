def build_dependency_graph(ir):

    instructions = ir["instructions"]
    cfg = ir.get("cfg", [])
    def_use = ir.get("def_use", [])

    edges = []

    # control edges
    for e in cfg:
        edges.append({
            "from": e.get("from_block"),
            "to": e.get("to_block"),
            "type": "control"
        })

    # data edges
    for d in def_use:
        edges.append({
            "from": d["def"],
            "to": d["use"],
            "type": "data",
            "var": d["var"]
        })

    return {
        "nodes": instructions,
        "edges": edges
    }