#!/usr/bin/env python3
"""
Data Parallelism Demonstration

This example shows data parallelism by performing the same operation
on different data elements simultaneously.

Data parallelism: Same operation on different data
"""

import time
import multiprocessing as mp
import random
from typing import List, Tuple


def process_chunk(data_chunk: List[float], multiplier: float) -> List[float]:
    """
    Process a chunk of data by multiplying each element.
    
    This represents a data-parallel operation: same computation
    (multiplication) applied to different data elements.
    
    Args:
        data_chunk: List of numbers to process
        multiplier: Value to multiply each element by
        
    Returns:
        Processed chunk
    """
    return [x * multiplier for x in data_chunk]


def sequential_processing(data: List[float], multiplier: float) -> List[float]:
    """Process data sequentially (baseline for comparison)."""
    return process_chunk(data, multiplier)


def parallel_processing(data: List[float], multiplier: float, num_workers: int = 4) -> List[float]:
    """
    Process data in parallel using multiple processes.
    
    This demonstrates data parallelism by dividing the data into chunks
    and processing each chunk independently.
    """
    # Divide data into chunks for each worker
    chunk_size = len(data) // num_workers
    chunks = []
    for i in range(num_workers):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_workers - 1 else len(data)
        chunks.append(data[start:end])
    
    # Create pool of workers
    with mp.Pool(processes=num_workers) as pool:
        # Apply same function to each chunk (data parallelism)
        results = pool.starmap(process_chunk, [(chunk, multiplier) for chunk in chunks])
    
    # Combine results
    return [item for sublist in results for item in sublist]


def benchmark(data_size: int = 1000000, multiplier: float = 2.5) -> Tuple[float, float, float]:
    """
    Benchmark sequential vs parallel processing.
    
    Returns:
        Tuple of (sequential_time, parallel_time, speedup)
    """
    # Generate random data
    random.seed(42)  # For reproducibility
    data = [random.random() for _ in range(data_size)]
    
    # Sequential processing
    start = time.time()
    seq_result = sequential_processing(data, multiplier)
    seq_time = time.time() - start
    
    # Parallel processing (using all available cores)
    num_workers = mp.cpu_count()
    start = time.time()
    par_result = parallel_processing(data, multiplier, num_workers)
    par_time = time.time() - start
    
    # Verify results match
    assert seq_result == par_result, "Results don't match!"
    
    speedup = seq_time / par_time if par_time > 0 else 0
    
    return seq_time, par_time, speedup


def demonstrate_data_parallelism():
    """Demonstrate data parallelism concepts with examples."""
    print("=" * 60)
    print("DATA PARALLELISM DEMONSTRATION")
    print("=" * 60)
    
    print("\n1. Concept Explanation:")
    print("   Data parallelism means applying the SAME operation")
    print("   to DIFFERENT data elements simultaneously.")
    print("   Example: Multiplying each element in an array by 2")
    
    print("\n2. Simple Example:")
    data = [1, 2, 3, 4, 5, 6, 7, 8]
    print(f"   Original data: {data}")
    
    # Sequential
    seq_result = [x * 2 for x in data]
    print(f"   Sequential result (x * 2): {seq_result}")
    
    # Parallel concept (simulated)
    print("   Parallel concept: Process [1,2,3,4] and [5,6,7,8] simultaneously")
    
    print("\n3. Real-world Applications:")
    print("   - Image processing (apply filter to all pixels)")
    print("   - Matrix operations (multiply all elements)")
    print("   - Scientific simulations (update all particles)")
    print("   - Data transformation (apply function to all records)")
    
    print("\n4. Performance Benchmark:")
    print("   Testing with 1,000,000 elements...")
    seq_time, par_time, speedup = benchmark(1000000)
    print(f"   Sequential time: {seq_time:.3f} seconds")
    print(f"   Parallel time: {par_time:.3f} seconds")
    print(f"   Speedup: {speedup:.2f}x")
    print(f"   Efficiency: {(speedup / mp.cpu_count() * 100):.1f}%")
    
    print("\n5. Key Characteristics:")
    print("   - Same operation applied to all data")
    print("   - Minimal communication between workers")
    print("   - Easy to load balance (equal-sized chunks)")
    print("   - Highly scalable for large datasets")
    
    print("\n6. When to Use Data Parallelism:")
    print("   ✓ Large datasets with uniform operations")
    print("   ✓ Operations are computationally expensive")
    print("   ✓ Data can be easily partitioned")
    print("   ✓ Minimal data dependencies between elements")
    
    print("\n7. Challenges:")
    print("   - Data partitioning strategy")
    print("   - Load balancing for irregular data")
    print("   - Result aggregation")
    print("   - Memory usage with many copies")


def compare_scaling():
    """Demonstrate strong vs weak scaling."""
    print("\n" + "=" * 60)
    print("SCALING ANALYSIS")
    print("=" * 60)
    
    data_sizes = [100000, 500000, 1000000]
    workers_list = [1, 2, 4]
    
    print("\nStrong Scaling (fixed problem size = 1,000,000):")
    print("Workers | Time (s) | Speedup | Efficiency")
    print("-" * 40)
    
    random.seed(42)  # For reproducibility
    data = [random.random() for _ in range(1000000)]
    multiplier = 2.5
    
    for workers in workers_list:
        if workers <= mp.cpu_count():
            # Time parallel processing
            start = time.time()
            parallel_processing(data, multiplier, workers)
            par_time = time.time() - start
            
            # Time sequential (1 worker)
            if workers == 1:
                seq_time = par_time
                speedup = 1.0
            else:
                speedup = seq_time / par_time
            
            efficiency = (speedup / workers) * 100
            print(f"{workers:7d} | {par_time:8.3f} | {speedup:7.2f} | {efficiency:9.1f}%")
    
    print("\nWeak Scaling (problem size per worker = 250,000):")
    print("Workers | Total Size | Time (s) | Efficiency")
    print("-" * 45)
    
    base_size = 250000
    for workers in workers_list:
        if workers <= mp.cpu_count():
            total_size = base_size * workers
            random.seed(42 + workers)  # Different seed for each size
            data = [random.random() for _ in range(total_size)]
            
            start = time.time()
            parallel_processing(data, multiplier, workers)
            par_time = time.time() - start
            
            # Ideal: constant time as problem scales with workers
            ideal_time = par_time if workers == 1 else par_time
            efficiency = 100  # Simplified for demonstration
            
            print(f"{workers:7d} | {total_size:10d} | {par_time:8.3f} | {efficiency:9.1f}%")


if __name__ == "__main__":
    print(f"System has {mp.cpu_count()} CPU cores")
    
    demonstrate_data_parallelism()
    compare_scaling()
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print("Data parallelism is ideal for:")
    print("1. Uniform operations on large datasets")
    print("2. Problems that can be easily partitioned")
    print("3. Applications where communication is minimal")
    print("\nThis example demonstrates the basic pattern of:")
    print("1. Partition data into chunks")
    print("2. Process chunks independently")
    print("3. Combine results")
    
    print("\nTry modifying this code to:")
    print("1. Change the operation (e.g., square root, sine)")
    print("2. Use different data types (e.g., strings, images)")
    print("3. Implement with threads instead of processes")
    print("4. Add error handling for uneven partitions")