package com.mehul;

import java.util.ArrayList;

public class BacktrackGrid {

    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        ArrayList<ArrayList<Integer>> mat;
        mat = matrix(3);
        System.out.println(AllPaths(3,0,0, "",list,mat));

    }
    // Function to form a 2d arraylist for flagging cells.
    public static ArrayList<ArrayList<Integer>> matrix(int n){
        ArrayList<ArrayList<Integer>> mat = new ArrayList<>();
        for(int i=0;i<n;i++){
            ArrayList<Integer> row = new ArrayList<>();
            for(int j=0;j<n;j++){
                row.add(1);
            }
            mat.add(row);
        }
        return mat;
    }
    // Function to find all possible paths from start(0,0) to end(n,n)
    public static ArrayList<String> AllPaths(int n, int r, int c, String path, ArrayList<String> paths,ArrayList<ArrayList<Integer>> notVisited){

        if(notVisited.get(r).get(c).equals(0)){
            return paths;
        }
        //Flagging once visited
        notVisited.get(r).set(c,0);

        if(r==n-1 && c==n-1){
            paths.add(path);
            System.out.println(path);
            notVisited.get(r).set(c,1); //reset destination point after finding one path
            return paths;
        }

        if(r<n-1){
            AllPaths(n,r+1,c,path+'D',paths,notVisited);
        }
        if(c<n-1){
            AllPaths(n,r,c+1,path+'R',paths,notVisited);
        }
        if(r>0){
            AllPaths(n,r-1,c,path+'U',paths,notVisited);
        }
        if(c>0){
            AllPaths(n,r,c-1,path+'L',paths,notVisited);
        }
        //Unflagging all flagged cells to reset for new path search (backtracking)
        notVisited.get(r).set(c,1);
        return paths;
    }
}
