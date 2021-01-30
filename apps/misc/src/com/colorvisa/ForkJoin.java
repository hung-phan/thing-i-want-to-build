package com.colorvisa;

import java.util.concurrent.ForkJoinPool;

public class ForkJoin {
  public static void main(String[] args) {
    ForkJoinPool pool = new ForkJoinPool(Runtime.getRuntime().availableProcessors());

    pool.invoke(new SimpleRecursiveAction(100000));
  }
}
