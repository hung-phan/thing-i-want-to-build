package com.colorvisa;

import java.util.concurrent.RecursiveTask;

public class SimpleRecursiveTask extends RecursiveTask<Integer> {
  private int simulatedWork;

  public SimpleRecursiveTask(int simulatedWork) {
    this.simulatedWork = simulatedWork;
  }

  @Override
  protected Integer compute() {
    if (simulatedWork > 100) {
      System.out.println("Parallel execution needed because of the huge task...");

      SimpleRecursiveTask task1 = new SimpleRecursiveTask(simulatedWork / 2);
      SimpleRecursiveTask task2 = new SimpleRecursiveTask(simulatedWork / 2);

      task1.fork();
      task2.fork();

      return task1.join() + task2.join();
    } else {
      System.out.println("No need for parallel execution...");

      return 2 * simulatedWork;
    }
  }
}
