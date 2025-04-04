import java.lang.reflect.Array;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;

// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}


class Solution {
    public Node cloneGraph(Node node) {
        return BFS_MODIFIED(node);
    }


    // Pseudocode:
    // 1. Initialization: Enqueue the given source vertex into a queue and mark it as visited.
    // 2. Exploration: While the queue is not empty:
    //      - Dequeue a node from the queue and visit it (e.g., print its value).
    //      - For each unvisited neighbor of the dequeued node:
    //      - Enqueue the neighbor into the queue.
    //      -  Mark the neighbor as visited.
    // 3.  Termination: Repeat step 2 until the queue is empty.

    // Source: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/ (GeekforGeeks)

    // In context of this Leetcode question, the pseudocode is:
    //    To solve this problem we need two things:
    //    1. BFS to traverse the graph
    //    2. A hash map to keep track of already visited and already cloned nodes
    //    We push a node in the queue and make sure that the node is already cloned. Then we process
    //    neighbors. If a neighbor is already cloned and visited, we just append it to the current
    //    clone neighbors list, otherwise, we clone it first and append it to the queue to make sure
    //    that we can visit it in the next tick.
    private Node BFS_MODIFIED(Node s) {
        if (s == null) {
            return null;
        }

        Map<Integer, Node> graph = new HashMap<>();

        Node clonedGraph = new Node(1);

        graph.put(clonedGraph.val, clonedGraph);

        // Create an array to store the traversal
        ArrayList<Node> res = new ArrayList<Node>();

        // Create a queue for BFS
        Queue<Node> queue = new ArrayDeque<Node>();

        // Initially mark all vertices as not visited
        Set<Integer> visited = new HashSet<>();

        // Mark source node as visited an enqueue it
        visited.add(s.val);
        queue.add(s);

        // Iterate over queue
        while (!queue.isEmpty()) {

            // Dequeue a vertex from queue and store it
            Node dequeuedNode = queue.poll();
            res.add(dequeuedNode);
            Node clonedNode = graph.get(dequeuedNode.val);

            // Get all adjacent vertices of the dequeued vertex. If an adjacent has not been
            // visited, mark it visited an enqueue it.
            for (Node n : dequeuedNode.neighbors) {
                // Clone neighbor if not already done
                if (!graph.containsKey(n.val)) {
                    graph.put(n.val, new Node(n.val));
                }

                // Add the cloned neighbor to the current cloned node
                clonedNode.neighbors.add(graph.get(n.val));

                // Only queue up unvisited neighbors
                if (!visited.contains(n.val)) {
                    visited.add(n.val);
                    queue.add(n);
                }
            }
        }
        return clonedGraph;
    }
}


class TestSolution {
    public static void main (String args[]){
        Node node1 = new Node(1);
        Node node2 = new Node(2);
        Node node3 = new Node(3);
        Node node4 = new Node(4);

        node1.neighbors.add(node2);
        node1.neighbors.add(node4);

        node2.neighbors.add(node1);
        node2.neighbors.add(node3);

        node3.neighbors.add(node2);
        node3.neighbors.add(node4);

        node4.neighbors.add(node1);
        node4.neighbors.add(node3);

        Solution solution = new Solution();
        Node clonedGraph = solution.cloneGraph(node1);
        System.out.println(clonedGraph);
        printGraph(clonedGraph);
    }

    private static void printGraph(Node node) {
        Set<Integer> visited = new HashSet<>();
        Queue<Node> queue = new LinkedList<>();

        queue.add(node);
        visited.add(node.val);

        while (!queue.isEmpty()) {
            Node current = queue.poll();
            System.out.print("Node " + current.val + " → [");

            for (Node neighbor : current.neighbors) {
                System.out.print(neighbor.val + " ");
                if (!visited.contains(neighbor.val)) {
                    visited.add(neighbor.val);
                    queue.add(neighbor);
                }
            }
            System.out.println("]");
        }
    }
}