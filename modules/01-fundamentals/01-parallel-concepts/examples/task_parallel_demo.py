#!/usr/bin/env python3
"""
Task Parallelism Demonstration

This example shows task parallelism by performing different operations
on the same or different data simultaneously.

Task parallelism: Different operations executed concurrently
"""

import time
import multiprocessing as mp
import threading
import queue
from typing import List, Dict, Any, Callable
from enum import Enum
import random


class TaskType(Enum):
    """Types of tasks for demonstration."""
    CALCULATE_SQUARE = "calculate_square"
    CALCULATE_CUBE = "calculate_cube"
    CALCULATE_FACTORIAL = "calculate_factorial"
    PROCESS_STRING = "process_string"
    FETCH_DATA = "fetch_data"


def calculate_square(x: int) -> int:
    """Calculate square of a number (simulate computation)."""
    time.sleep(0.1)  # Simulate computation time
    return x * x


def calculate_cube(x: int) -> int:
    """Calculate cube of a number (simulate computation)."""
    time.sleep(0.15)  # Simulate computation time
    return x * x * x


def calculate_factorial(x: int) -> int:
    """Calculate factorial (simulate heavy computation)."""
    time.sleep(0.2)  # Simulate computation time
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result


def process_string(s: str) -> str:
    """Process a string (simulate I/O or transformation)."""
    time.sleep(0.05)  # Simulate processing time
    return s.upper() + "!" * random.randint(1, 3)


def fetch_data(task_id: int) -> Dict[str, Any]:
    """Simulate fetching data from external source."""
    time.sleep(0.1 + random.random() * 0.2)  # Variable latency
    return {
        "task_id": task_id,
        "data": random.randint(1, 100),
        "timestamp": time.time()
    }


def sequential_task_processing(tasks: List[Dict]) -> List[Any]:
    """Process tasks sequentially."""
    results = []
    for task in tasks:
        task_type = task["type"]
        data = task["data"]
        
        if task_type == TaskType.CALCULATE_SQUARE:
            result = calculate_square(data)
        elif task_type == TaskType.CALCULATE_CUBE:
            result = calculate_cube(data)
        elif task_type == TaskType.CALCULATE_FACTORIAL:
            result = calculate_factorial(data)
        elif task_type == TaskType.PROCESS_STRING:
            result = process_string(data)
        elif task_type == TaskType.FETCH_DATA:
            result = fetch_data(data)
        else:
            result = None
        
        results.append({
            "task": task_type.value,
            "input": data,
            "output": result
        })
    
    return results


def worker(task_queue: mp.Queue, result_queue: mp.Queue):
    """Worker function for parallel task processing."""
    while True:
        try:
            task = task_queue.get(timeout=1)
            if task is None:  # Poison pill to stop worker
                break
                
            task_type = task["type"]
            data = task["data"]
            
            # Execute appropriate function based on task type
            if task_type == TaskType.CALCULATE_SQUARE:
                result = calculate_square(data)
            elif task_type == TaskType.CALCULATE_CUBE:
                result = calculate_cube(data)
            elif task_type == TaskType.CALCULATE_FACTORIAL:
                result = calculate_factorial(data)
            elif task_type == TaskType.PROCESS_STRING:
                result = process_string(data)
            elif task_type == TaskType.FETCH_DATA:
                result = fetch_data(data)
            else:
                result = None
            
            result_queue.put({
                "task": task_type.value,
                "input": data,
                "output": result,
                "worker": mp.current_process().name
            })
            
        except queue.Empty:
            break


def parallel_task_processing(tasks: List[Dict], num_workers: int = 4) -> List[Any]:
    """Process tasks in parallel using worker pool."""
    # Create queues
    task_queue = mp.Queue()
    result_queue = mp.Queue()
    
    # Add tasks to queue
    for task in tasks:
        task_queue.put(task)
    
    # Add poison pills to stop workers
    for _ in range(num_workers):
        task_queue.put(None)
    
    # Create and start workers
    workers = []
    for i in range(num_workers):
        w = mp.Process(target=worker, args=(task_queue, result_queue))
        w.start()
        workers.append(w)
    
    # Collect results
    results = []
    for _ in range(len(tasks)):
        result = result_queue.get()
        results.append(result)
    
    # Wait for workers to finish
    for w in workers:
        w.join()
    
    return results


def demonstrate_task_parallelism():
    """Demonstrate task parallelism concepts."""
    print("=" * 60)
    print("TASK PARALLELISM DEMONSTRATION")
    print("=" * 60)
    
    print("\n1. Concept Explanation:")
    print("   Task parallelism means executing DIFFERENT operations")
    print("   on the SAME or DIFFERENT data simultaneously.")
    print("   Example: Web server handling multiple client requests")
    
    print("\n2. Example Tasks:")
    tasks = [
        {"type": TaskType.CALCULATE_SQUARE, "data": 5},
        {"type": TaskType.CALCULATE_CUBE, "data": 3},
        {"type": TaskType.CALCULATE_FACTORIAL, "data": 6},
        {"type": TaskType.PROCESS_STRING, "data": "hello"},
        {"type": TaskType.FETCH_DATA, "data": 1},
        {"type": TaskType.CALCULATE_SQUARE, "data": 7},
        {"type": TaskType.CALCULATE_CUBE, "data": 4},
        {"type": TaskType.FETCH_DATA, "data": 2},
    ]
    
    print("   Task list:")
    for i, task in enumerate(tasks):
        print(f"   {i+1}. {task['type'].value}({task['data']})")
    
    print("\n3. Sequential Processing:")
    start = time.time()
    seq_results = sequential_task_processing(tasks)
    seq_time = time.time() - start
    
    print(f"   Time: {seq_time:.3f} seconds")
    print(f"   Results: {len(seq_results)} tasks completed")
    
    print("\n4. Parallel Processing:")
    num_workers = min(4, mp.cpu_count())
    start = time.time()
    par_results = parallel_task_processing(tasks, num_workers)
    par_time = time.time() - start
    
    print(f"   Workers: {num_workers}")
    print(f"   Time: {par_time:.3f} seconds")
    print(f"   Speedup: {seq_time / par_time:.2f}x")
    
    print("\n5. Worker Distribution:")
    worker_counts = {}
    for result in par_results:
        worker_name = result.get('worker', 'unknown')
        worker_counts[worker_name] = worker_counts.get(worker_name, 0) + 1
    
    for worker_name, count in worker_counts.items():
        print(f"   {worker_name}: {count} tasks")
    
    print("\n6. Real-world Applications:")
    print("   - Web servers (different requests)")
    print("   - Compilers (lexical analysis, parsing, code gen)")
    print("   - Scientific workflows (different simulations)")
    print("   - Microservices architecture")
    
    print("\n7. Key Characteristics:")
    print("   - Different operations/tasks")
    print("   - Tasks may have dependencies")
    print("   - Load balancing can be challenging")
    print("   - Communication patterns vary")
    
    print("\n8. When to Use Task Parallelism:")
    print("   ✓ Heterogeneous tasks with different operations")
    print("   ✓ Tasks with varying execution times")
    print("   ✓ Independent or loosely coupled tasks")
    print("   ✓ Dynamic task generation")
    
    print("\n9. Challenges:")
    print("   - Task dependency management")
    print("   - Load balancing for uneven tasks")
    print("   - Resource contention")
    print("   - Synchronization and coordination")


def compare_with_data_parallelism():
    """Compare task parallelism with data parallelism."""
    print("\n" + "=" * 60)
    print("TASK vs DATA PARALLELISM COMPARISON")
    print("=" * 60)
    
    print("\nData Parallelism:")
    print("  Pattern: Same operation, different data")
    print("  Example: Multiply all elements in array by 2")
    print("  Communication: Minimal (partition data, combine results)")
    print("  Load Balancing: Easy (equal-sized chunks)")
    print("  Scalability: Excellent for regular problems")
    
    print("\nTask Parallelism:")
    print("  Pattern: Different operations, same/different data")
    print("  Example: Web server handling various requests")
    print("  Communication: Variable (task dependencies)")
    print("  Load Balancing: Challenging (uneven task times)")
    print("  Scalability: Good for independent tasks")
    
    print("\nHybrid Approach:")
    print("  Many real applications use both:")
    print("  - Data parallelism within tasks")
    print("  - Task parallelism between different operations")
    print("  Example: Video processing pipeline:")
    print("    • Task 1: Decode frames (data parallel per frame)")
    print("    • Task 2: Apply filters (data parallel per pixel)")
    print("    • Task 3: Encode frames (data parallel per frame)")


def demonstrate_dynamic_task_generation():
    """Show dynamic task generation and load balancing."""
    print("\n" + "=" * 60)
    print("DYNAMIC TASK GENERATION & LOAD BALANCING")
    print("=" * 60)
    
    print("\n1. Work Stealing Pattern:")
    print("   - Each worker has its own task queue")
    print("   - Idle workers steal tasks from busy workers")
    print("   - Dynamic load balancing for uneven workloads")
    
    print("\n2. Task Dependencies:")
    print("   - Some tasks depend on others' results")
    print("   - Represented as directed acyclic graph (DAG)")
    print("   - Execute when dependencies are satisfied")
    
    print("\n3. Example: Image Processing Pipeline")
    print("   Tasks with dependencies:")
    print("   1. Load image → 2. Resize → 3. Filter → 4. Save")
    print("   Can execute different images in parallel")
    print("   Each stage can use data parallelism")
    
    print("\n4. Implementation Strategies:")
    print("   - Thread pools with work queues")
    print("   - Actor model (message passing)")
    print("   - Task-based parallel libraries")
    print("   - Workflow engines")


if __name__ == "__main__":
    print(f"System has {mp.cpu_count()} CPU cores")
    
    demonstrate_task_parallelism()
    compare_with_data_parallelism()
    demonstrate_dynamic_task_generation()
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print("Task parallelism is ideal for:")
    print("1. Heterogeneous workloads with different operations")
    print("2. Applications with independent or loosely coupled tasks")
    print("3. Dynamic workloads where tasks are generated at runtime")
    
    print("\nCommon patterns:")
    print("1. Master-Worker: Central coordinator distributes tasks")
    print("2. Work Stealing: Idle workers take tasks from busy ones")
    print("3. Pipeline: Tasks flow through processing stages")
    print("4. Fork-Join: Split work, process independently, combine")
    
    print("\nTry modifying this code to:")
    print("1. Add new task types with different computations")
    print("2. Implement work stealing for better load balancing")
    print("3. Add task dependencies (DAG execution)")
    print("4. Compare with threading instead of multiprocessing")
    print("5. Measure overhead of task queue management")