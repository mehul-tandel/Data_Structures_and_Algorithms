package com.mehul;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.Stack;

public class StackProblems {
    public static void main(String[] args) {
//       int[] a  = {4,3,6,5,76,23,56,8};
//        System.out.println(Arrays.toString(previousSmallerElement(a)));
//        System.out.println(Arrays.toString(nextSmallerElement(a)));
//        System.out.println(Arrays.toString(previousGreaterElement(a)));
    }

    static int[] previousSmallerElement(int[] arr){
        int[] ans = new int[arr.length];
        Stack<Integer> stack = new Stack<>();
        for(int i = 0; i < arr.length; i++){
            while(!stack.isEmpty() && stack.peek() >= arr[i]){
                stack.pop();
            }
            if(stack.isEmpty()){
                ans[i] = -1;
            }else{
                ans[i] = stack.peek();
            }
            stack.push(arr[i]);
        }
        return ans;
    }

    static int[] previousGreaterElement(int[] arr){
        int[] ans = new int[arr.length];
        Stack<Integer> stack = new Stack<>();
        for(int i = 0; i < arr.length; i++){
            while(!stack.isEmpty() && stack.peek() < arr[i]){
                stack.pop();
            }
            if(stack.isEmpty()){
                ans[i] = -1;
            }else{
                ans[i] = stack.peek();
            }
            stack.push(arr[i]);
        }
        return ans;
    }

    static int[] nextSmallerElement(int[] arr){
        int[] ans = new int[arr.length];
        Deque<Integer> stack = new ArrayDeque<>();
        for(int i = arr.length-1; i>=0; i--){
            while(!stack.isEmpty() && stack.peek()>=arr[i]){
                stack.pop();
            }
            if(stack.isEmpty()) {
                ans[i] = -1;
            }else{
                ans[i] = stack.peek();
            }
            stack.push(arr[i]);
        }
        return ans;
    }

}
