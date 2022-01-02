package com.mehul;

class Node {
    int data;
    Node next;
    Node child;

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
        if (head.child != null){
            System.out.print('[');
            printOriginalList(head.child);
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

    }
}
