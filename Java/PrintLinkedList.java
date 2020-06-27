import java.util.*;

class Node {
    int val;
    Node next;
    
    Node(int val) {
        this.val = val;
        this.next = null;
    }
}

public class PrintLinkedList {
    // public static void main(String[] args) {
    //     List<Integer> list = new LinkedList<>();
    //     list.add(1);
    //     list.add(2);
    //     list.add(3);
    //     list.add(4);
    //     list.add(5);
    //     System.out.println(list);
    // }

    public static void printLinkedList(Node head) {
        while (head != null) {
            System.out.println(head.val);
            head = head.next;
        }
    }

    public static void main(String[] args) {
        // make Linked List of size 5 from 1 - 5
        Node head = new Node(1);
        Node temp = head;
        for (int i = 1; i < 5; i++) {
            Node addNode = new Node(i + 1);
            temp.next = addNode;
            temp = temp.next;
        }

        // now print that bitch
        printLinkedList(head);
    }
}