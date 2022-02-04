package com.mehul.graphs;

import java.util.*;

public class Graph {

    static class Edge {
        int to, from, cost;
        public Edge(int to, int from, int cost){
            this.to = to;
            this.from = from;
            this.cost = cost;
        }
    }

    private static void addEdge(Map<Integer,List<Edge>> graph,int to, int from, int cost){
        List<Edge> list = graph.get(from);
        if (list == null){
            list = new ArrayList<Edge>();
            graph.put(from,list);
        }
        list.add(new Edge(to,from,cost));
    }

    public static void main(String[] args) {
        int numNodes = 6;
        Map<Integer,List<Edge>> graph = new HashMap<>();
        addEdge(graph,1,0,2);
        addEdge(graph,2,0,4);
        addEdge(graph,3,1,1);
        addEdge(graph,4,2,3);
        addEdge(graph,5,2,2);
        addEdge(graph,2,1,4);

        int nodeCount = dfs(graph,0,numNodes);
        System.out.println(nodeCount);

    }

    static int dfs(Map<Integer,List<Edge>> graph,int start, int n){
        int count = 0;
        boolean[] visited = new boolean[n];
        Stack<Integer> stack = new Stack<>();

        stack.push(start);
        visited[start] = true;

        while (!stack.isEmpty()){
            int node = stack.pop();
            count++;
            List<Edge> adjEdges = graph.get(node);

            if(adjEdges != null){
                for(Edge edge : adjEdges){
                    if(!visited[edge.to]){
                        stack.push(edge.to);
                        visited[edge.to] = true;
                    }
                }
            }
        }
        return count;
    }


}



