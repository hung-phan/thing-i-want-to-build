package com.colorvisa;

import java.util.concurrent.RecursiveTask;
import java.util.stream.IntStream;

class MaxFinding extends RecursiveTask<Integer> {
  static final int THRESHOLD = 128;

  private int[] nums;
  private int low;
  private int high;

  public MaxFinding(int[] nums, int low, int high) {
    this.nums = nums;
    this.low = low;
    this.high = high;
  }

  public int sequential(int low, int high) {
    return IntStream.rangeClosed(low, high).map(index -> nums[index]).max().getAsInt();
  }

  public int parallel(int low, int high) {
    int mid = (low + high) / 2;

    MaxFinding left = new MaxFinding(nums, low, mid);
    MaxFinding right = new MaxFinding(nums, mid + 1, high);

    invokeAll(left, right);

    return Math.max(left.join(), right.join());
  }

  @Override
  protected Integer compute() {
    if (high - low < THRESHOLD) {
      return sequential(low, high);
    }

    return parallel(low, high);
  }
}
