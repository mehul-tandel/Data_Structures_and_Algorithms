//The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
//
//Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
//
//Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

package com.mehul;

import java.util.ArrayList;

public class NQueens {
    public static void main(String[] args) {
        System.out.println(allConfigurations(4));
    }
    public static ArrayList<ArrayList<StringBuilder>> allConfigurations(int n){
        ArrayList<ArrayList<StringBuilder>> configurations = new ArrayList<ArrayList<StringBuilder>>();
        for(int i=0;i<n;i++){
            configurations.add(configure(n,0,i));
        }
        return configurations;
    }

    public static ArrayList<StringBuilder> configure(int n,int r, int c){
        ArrayList<StringBuilder> configuration = new ArrayList<>();
        for(int i=0;i<n;i++){
            configuration.add(new StringBuilder());
        }
        boolean[][] board = createBoard(n);

        //solve problem
        placeQueens(n,board,r,c);

        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if (board[i][j]){
                    configuration.get(i).append(".");
                }else{
                    configuration.get(i).append("Q");
                }
            }
        }
        return configuration;
    }
    public static boolean[][] createBoard(int n){
        boolean[][] board = new boolean[n][n];
        for (int i=0;i<n;i++){
            boolean[] a = new boolean[n];
            for(int j=0;j<n;j++){
                a[j] = true;
            }
            board[i] = a;
        }
        return board;
    }
    public static boolean checkVertical(int r, int c,boolean[][] board){
        if(board[r][c]){
            if(r==0) {
                return true;
            }
            return checkVertical(--r,c,board);
        }
        return false;
    }
    public static boolean checkDiagLeft(int r, int c, boolean[][] board){
        if(board[r][c]){
            if(r==0 || c==0) {
                return true;
            }
            return checkDiagLeft(--r,--c,board);
        }
        return false;
    }
    public static boolean checkDiagRight(int r, int c,int n, boolean[][]board){
        if(board[r][c]){
            if(r==0 || c==n-1) {
                return true;
            }
            return checkDiagRight(--r,++c,n,board);
        }
        return false;
    }
    public static boolean check(int n,int r, int c, boolean[][] board){
        boolean vertical = checkVertical(r,c,board);
        if(!vertical){
            return false;
        }
        boolean diagLeft = checkDiagLeft(r,c,board);
        if(!diagLeft){
            return false;
        }
        boolean diagRight = checkDiagRight(r,c,n,board);
        if(!diagRight){
            return false;
        }
        return true;
    }

    public static boolean placeQueens(int n,boolean[][]board, int r, int c){
        if(c==n){
            return false;
        }
        if(r==n){
            return true;
        }
        boolean placeQueen = check(n,r,c,board);
        if(placeQueen){
            board[r][c] = false;
            placeQueens(n,board,++r,0);
        }
        else{
            placeQueens(n,board,r,++c);
        }
        return true;
    }

}
// Partially correct