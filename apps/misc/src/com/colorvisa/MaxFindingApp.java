package com.colorvisa;

import java.util.Random;
import java.util.concurrent.ForkJoinPool;

public class MaxFindingApp {
  public static void main(String[] args) {
    int[] nums = new int[100_000];

    Random rand = new Random();

    for (int i = 0; i < nums.length; i++) {
      nums[i] = rand.nextInt(100_000);
    }

    ForkJoinPool pool = new ForkJoinPool(Runtime.getRuntime().availableProcessors());
    MaxFinding maxFinding = new MaxFinding(nums, 0, nums.length - 1);

    int max = pool.invoke(maxFinding);

    System.out.println("Max result: " + max);
  }
}
