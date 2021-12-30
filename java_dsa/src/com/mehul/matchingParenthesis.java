package com.mehul;

import java.util.Stack;

public class matchingParenthesis {
    public static void main(String[] args) {
        String s = "({})";
        System.out.println(isParenthesisMatching(s));
    }

    static boolean isMatching(char a, char b){
        return (a=='(' && b==')') ||
                (a=='[' && b==']') ||
                (a=='{' && b=='}');
    }

    static boolean isOpening(char a){
        return (a == '(') || (a == '[') || (a == '{');
    }

    static boolean isParenthesisMatching(String str){
        Stack<Character> stack = new Stack<>();
        for( int i = 0; i < str.length(); i++){
            char cur = str.charAt(i);
            if (isOpening(cur)){
                stack.push(cur);
            }else{
                if(stack.isEmpty()){
                    return false;
                }else{
                    if(!isMatching(stack.peek(),cur)){
                        return false;
                    }else{
                        stack.pop();
                    }
                }
            }
        }
        return stack.isEmpty();
    }
}
