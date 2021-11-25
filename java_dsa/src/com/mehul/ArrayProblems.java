package com.mehul;

import java.util.ArrayList;
import java.util.Arrays;

/*
Given two arrays of integers nums and index. Your task is to create target array under the following rules:
Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.
*/

public class ArrayProblems{
    public static void main(String[] args){
        int[] nums = {2,2,7,5,7};
        int[] index = {0,1,1,0,4};
        int[] target = generateInOrder(nums, index);
        int[] target2 = generateInOrder2(nums, index);
        System.out.println(Arrays.toString(target));
        System.out.println(Arrays.toString(target2));
    }

    // method to generate new array in required order using ArrayList.
    public static int[] generateInOrder(int[] nums, int[] index){
        ArrayList<Integer> target = new ArrayList<>();
        int[] a = new int[nums.length];
        for(int i=0; i<nums.length; i++){
            target.add(index[i],nums[i]);
        }
        for(int i=0; i<nums.length; i++){
            a[i] = target.get(i);
        }

        return a;
    }

    // same function of method as above but without using ArrayList, just using primitive int array.
    public static int[] generateInOrder2(int[] nums, int[] index){
        int[] target = new int[nums.length];
        if(nums.length==1) return nums;
        for(int i = 0; i<nums.length; i++){
            int temp = target[index[i]];
            target[index[i]] = nums[i];
            for(int j =nums.length-1; j>index[i];j--){
                target[j] = target[j-1];
            }
            if(index[i]<nums.length-1) target[index[i]+1] = temp;
        }
        return target;
    }
}