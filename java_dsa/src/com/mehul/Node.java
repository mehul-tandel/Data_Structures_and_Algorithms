package com.mehul;

import java.util.ArrayDeque;

class Node {
    int data;
    Node next;
    Node down;

    Node(int data){
        this.data = data;
    }
}

class MultilevelLl {
    public static void printOriginalList (Node head){
        if (head == null){
            return;
        }
        System.out.print(' ' + head.data + ' ');
        if (head.down != null){
            System.out.print('[');
            printOriginalList(head.down);
            System.out.print(']');
        }
        printOriginalList(head.next);
    }

    public static void printList(Node head){
        while (head != null){
            System.out.print(head.data + "->");
            head = head.next;
        }
        System.out.println("null");
    }

    public static Node flattenList(Node head){
        if(head == null){
            return null;
        }
        Node curr = head;
        Node tail = head;
        ArrayDeque<Node> queue = new ArrayDeque<>();
        while (tail.next != null || !queue.isEmpty()){
            if(tail.next == null){
                tail.next = queue.poll();
            }
            while(tail.next != null){
                tail = tail.next;
            }
            while(curr.down == null){
                curr = curr.next;
            }
            queue.add(curr.down);
            curr = curr.next;
        }
        return head;
    }
}
