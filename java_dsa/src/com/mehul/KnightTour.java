// Not solved yet

package com.mehul;

import java.util.ArrayList;

public class KnightTour {
    public static void main(String[] args) {
        boolean[][] board = createBoard(8);
        int paths = tour(4,board,0,0,0,new ArrayList<ArrayList<Integer>>());
        System.out.println(paths);
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

    public static int tour(int n, boolean[][] board, int jump, int r, int c, ArrayList<ArrayList<Integer>> paths){
        board[r][c] = false;
        if(jump == n*n-1){
            ArrayList<Integer> destination = new ArrayList<>();
            destination.add(0,r);
            destination.add(1,c);
            paths.add(jump,destination);
            return 1;
        }

        ArrayList<ArrayList<Integer>> nextJump = nextJumps(board,r,c);
        if(nextJump.isEmpty()){
            return 0;
        }
        for(ArrayList<Integer> square : nextJump){
            tour(n,board,jump+1,square.get(0),square.get(1),paths);
        }
        board[r][c] = true;
        return 0;
    }

    private static ArrayList<ArrayList<Integer>> nextJumps(boolean[][] board, int r, int c) {
        ArrayList<ArrayList<Integer>> jumps = new ArrayList<ArrayList<Integer>>();
        if(r+2 < board.length){
            if(c+1 < board.length){
                ArrayList<Integer> square = new ArrayList<>();
                square.add(0,r+2);
                square.add(1,c+1);
                jumps.add(square);
            }
            if(c-1 >= 0){
                ArrayList<Integer> square = new ArrayList<>();
                square.add(0,r+2);
                square.add(1,c-1);
                jumps.add(square);
            }
        }
        if(r-2 >= 0){
            if(c+1 < board.length){
                ArrayList<Integer> square = new ArrayList<>();
                square.add(0,r-2);
                square.add(1,c+1);
                jumps.add(square);
            }
            if(c-1 >= 0){
                ArrayList<Integer> square = new ArrayList<>();
                square.add(0,r-2);
                square.add(1,c-1);
                jumps.add(square);
            }
        }
        if(c+2 < board.length){
            if(r+1 < board.length){
                ArrayList<Integer> square = new ArrayList<>();
                square.add(0,r+1);
                square.add(1,c+2);
                jumps.add(square);
            }
            if(r-1 >= 0){
                ArrayList<Integer> square = new ArrayList<>();
                square.add(0,r-2);
                square.add(1,c+2);
                jumps.add(square);
            }
        }
        if(c-2 >= 0){
            if(r+1 < board.length){
                ArrayList<Integer> square = new ArrayList<>();
                square.add(0,r+1);
                square.add(1,c-2);
                jumps.add(square);
            }
            if(r-1 >= 0){
                ArrayList<Integer> square = new ArrayList<>();
                square.add(0,r-1);
                square.add(1,c-2);
                jumps.add(square);
            }
        }
    return jumps;
    }
}
