# Parallel Concepts Examples

This directory contains practical code examples demonstrating parallel computing concepts covered in the theory section.

## Examples Overview

### 1. Data Parallelism
**File**: `data_parallel_demo.py`

Demonstrates data parallelism where the same operation is applied to different data elements simultaneously.

**Key Concepts**:
- Same operation on different data
- Data partitioning strategies
- Strong vs weak scaling
- Performance measurement (speedup, efficiency)

**Run the example**:
```bash
python data_parallel_demo.py
```

**Learning Objectives**:
- Understand data parallelism pattern
- Learn to partition data for parallel processing
- Measure and analyze parallel performance
- Compare sequential vs parallel execution

### 2. Task Parallelism  
**File**: `task_parallel_demo.py`

Demonstrates task parallelism where different operations are executed concurrently on the same or different data.

**Key Concepts**:
- Different operations executed concurrently
- Task queue and worker pool pattern
- Load balancing challenges
- Comparison with data parallelism

**Run the example**:
```bash
python task_parallel_demo.py
```

**Learning Objectives**:
- Understand task parallelism pattern
- Implement worker pool with task queues
- Analyze load balancing in heterogeneous tasks
- Compare task vs data parallelism approaches

## How to Use These Examples

### Prerequisites
- Python 3.7 or higher
- Basic understanding of Python programming
- Familiarity with command line interface

### Running Examples
1. Navigate to this directory:
   ```bash
   cd modules/01-fundamentals/01-parallel-concepts/examples
   ```

2. Run any example:
   ```bash
   python data_parallel_demo.py
   python task_parallel_demo.py
   ```

### Experimenting with Code
Each example includes suggestions for modifications to deepen understanding:

1. **Change parameters**:
   - Modify data sizes
   - Change number of workers
   - Adjust computation complexity

2. **Implement variations**:
   - Try different parallelization strategies
   - Compare with threading instead of multiprocessing
   - Add error handling and logging

3. **Performance analysis**:
   - Measure speedup with different core counts
   - Analyze scaling behavior
   - Identify bottlenecks

## Key Learning Points

### From Data Parallelism Example
1. **Partitioning Strategies**:
   - Equal-sized chunks for regular data
   - Dynamic partitioning for irregular workloads
   - Considerations for data dependencies

2. **Performance Metrics**:
   - Speedup = Sequential time / Parallel time
   - Efficiency = Speedup / Number of processors
   - Strong scaling vs weak scaling

3. **Implementation Patterns**:
   - Map-reduce pattern
   - Fork-join parallelism
   - Data decomposition techniques

### From Task Parallelism Example
1. **Task Management**:
   - Task queue design
   - Worker pool implementation
   - Load balancing strategies

2. **Coordination Patterns**:
   - Master-worker pattern
   - Work stealing for dynamic load balancing
   - Task dependency management

3. **Real-world Applications**:
   - Web servers and request handling
   - Scientific workflow management
   - Microservices architecture

## Common Patterns Demonstrated

### 1. Embarrassingly Parallel
- No communication between tasks
- Perfect for data parallelism
- Maximum scalability potential

### 2. Master-Worker
- Central coordinator distributes work
- Workers process tasks independently
- Results collected by master

### 3. Pipeline
- Data flows through processing stages
- Each stage can be parallelized
- Overlap computation and communication

## Performance Considerations

### Communication Overhead
- Minimal in data parallelism (partition once, combine once)
- Variable in task parallelism (task distribution, result collection)

### Load Balancing
- Easy for data parallelism (equal-sized chunks)
- Challenging for task parallelism (uneven task times)

### Memory Usage
- Data parallelism may require data duplication
- Task parallelism needs task queue management

## Extending the Examples

### Adding New Examples
1. **Pipeline Parallelism**: Implement a multi-stage processing pipeline
2. **Hybrid Parallelism**: Combine data and task parallelism
3. **Real Applications**: Implement parallel versions of common algorithms

### Integration with Other Modules
These examples provide foundation for:
- MPI programming (module 02)
- OpenMP basics (module 03)  
- Performance measurement (module 04)

## Troubleshooting

### Common Issues
1. **Memory errors**: Reduce data size or increase chunk size
2. **Slow performance**: Check CPU utilization, adjust worker count
3. **Hanging processes**: Ensure proper termination conditions

### Debugging Tips
1. Start with small data sizes
2. Add logging to track execution flow
3. Use Python's `time` module for profiling
4. Test with single worker before scaling up

## Next Steps

After understanding these examples, proceed to:
1. **Module 02**: MPI Hello World - Learn distributed memory programming
2. **Module 03**: OpenMP Basics - Learn shared memory programming
3. **Module 04**: Performance Measurement - Learn profiling and optimization

## Contributing

Found a bug or have an improvement? 
1. Create an issue describing the problem or enhancement
2. Submit a pull request with your changes
3. Follow the project's coding standards and conventions

## License

These examples are part of the HPC Learning project. See the main project README for license information.