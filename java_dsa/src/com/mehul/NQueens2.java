package com.mehul;

public class NQueens2 {
    public static void main(String[] args) {
        boolean[][] board = createBoard(4);
        int configs = configs(board,0);
        System.out.println(configs);
    }

    public static void printQueens(boolean[][]board){
        for(boolean[]row : board){
            for(boolean b : row){
                if(b){
                    System.out.print('X');
                }else{
                    System.out.print('Q');
                }
            }
            System.out.println();
        }
    }

    // Using this function will make rows refer to same value and changes in one row will cause changes in others as well.
//    public static boolean[][] createBoard(int n){
//        boolean[][] board = new boolean[n][n];
//        boolean[] a = new boolean[n];
//        for(int j=0;j<n;j++){
//            a[j] = true;
//        }
//        for(int i=0;i<n;i++){
//            board[i] = a;
//        }
//        return board;
//    }

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

    public static int configs(boolean[][] board, int r){
        if(r == board.length){
            printQueens(board);
            System.out.println();
            return 1;
        }
        int count = 0;
        for(int c=0;c<board.length;c++){
            if(isSafe(board,r,c)) {
                board[r][c] = false;
                count += configs(board, r+1);
                board[r][c] = true;
            }
        }
        return count;
    }

    private static boolean isSafe(boolean[][] board, int r, int c) {
        for(int i=1;i <= r;i++){
            if(!board[r-i][c]){
                return false;
            }
        }
        for(int i=1;i<=(Math.min(r,c));i++){
            if(!board[r-i][c-i]){
                return false;
            }
        }
        for(int i=1; i<=(Math.min(r,board.length-c-1));i++){
            if(!board[r-i][c+i]){
                return false;
            }
        }
        return true;
    }
}
// Successful after hours of debugging because of that commented createBoard function.