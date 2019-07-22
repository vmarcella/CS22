import argparse

from graphs.graph import fill_graph
from graphs.utils.file_reader import read_graph_file


def process_args():
    """
        Process the arguments for challenge 2
    """
    parser = argparse.ArgumentParser(
        description="Find the shortest path between two verticies"
    )
    parser.add_argument(
        "filename", help="The name of the graph file to parse", type=str
    )
    parser.add_argument("from_vert", help="The vertex you'd like to start at", type=int)
    parser.add_argument("to_vert", help="The vertex you'd like to end up at", type=int)

    return parser.parse_args()


def main(args: argparse.Namespace):
    """
        The main functionality of challenge 2. Handles input errors, creates the graph with
        the specified properties, and then finds the shortest path from two edges.
    """

    # Input checks
    if not args.filename:
        raise ValueError("There was no graph file path specified!")

    if not args.from_vert:
        raise ValueError("You didn't specify a from vertex to start at!")

    if not args.to_vert:
        raise ValueError("You didn't specify a to vertex to start at!")

    # Obtain the graph properties and then fill out the graph.
    graph, vertex, edges = read_graph_file(args.filename)
    fill_graph(graph, vertex, edges)

    # Obtain the path and edges to get from one vertex to another
    path, edges = graph.find_shortest_path(args.from_vertex, args.to_vertex)


if __name__ == "__main__":
    ARGS = process_args()
    main(ARGS)
