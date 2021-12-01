package com.mehul;

import java.util.Arrays;

public class SudokuSolver {
    public static void main(String[] args) {
        int [][] sudoku =
                { {3, 0, 6, 5, 0, 8, 4, 0, 0},
                {5, 2, 0, 0, 0, 0, 0, 0, 0},
                {0, 8, 7, 0, 0, 0, 0, 3, 1},
                {0, 0, 3, 0, 1, 0, 0, 8, 0},
                {9, 0, 0, 8, 6, 3, 0, 0, 5},
                {0, 5, 0, 0, 9, 0, 6, 0, 0},
                {1, 3, 0, 0, 0, 0, 2, 5, 0},
                {0, 0, 0, 0, 0, 0, 0, 7, 4},
                {0, 0, 5, 2, 0, 6, 3, 0, 0} };

        solve(sudoku,0,0);
    }


    public static void solve(int[][] board, int r, int c){
        if(r == board.length){
            displayBoard(board);
            return;
        }
        if(c == board.length){
            solve(board,r+1,0);
            return;
        }
        if(board[r][c] == 0){
            for(int i = 1; i <= board.length; i++){
                if(isSafe(board,i,r,c)){
                    board[r][c] = i;
                    solve(board,r,c+1);
                    board[r][c] = 0;
                }
            }
        }
        else{
            solve(board,r,c+1);
        }
    }

    private static void displayBoard(int[][] board) {
        for(int[] row : board){
            System.out.println(Arrays.toString(row));
        }
    }

    private static boolean isSafe(int[][] board, int i, int r, int c) {
        // Check row
        for(int num : board[r]){
            if(num == i){
                return false;
            }
        }
        // Check col
        for (int[] rows : board) {
            if (rows[c] == i) {
                return false;
            }
        }
        // Check 3x3 grid
        int rowStart = r - (r%3);
        int colStart = c - (c%3);

        for(int j=rowStart; j<rowStart+3; j++){
            for(int k=colStart; k<colStart+3; k++){
                if(board[j][k] == i){
                    return false;
                }
            }
        }
        return true;
    }
}
