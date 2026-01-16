# Performance Analysis and Laws

## Overview
Understanding and analyzing parallel performance is crucial for developing efficient parallel programs. This section covers the fundamental laws, metrics, and techniques for evaluating parallel performance.

## Key Performance Metrics

### 1. Execution Time
- **Wall-clock Time**: Total time from start to finish (real time)
- **CPU Time**: Total processor time used (sum across all processors)
- **Parallel Time**: Time taken by parallel version
- **Sequential Time**: Time taken by best sequential version

### 2. Speedup
```
Speedup(S) = T_seq / T_par
```
Where:
- `T_seq`: Execution time of sequential algorithm
- `T_par`: Execution time of parallel algorithm with P processors

#### Types of Speedup:
- **Linear Speedup**: S = P (ideal case)
- **Sublinear Speedup**: S < P (common due to overhead)
- **Superlinear Speedup**: S > P (rare, usually due to cache effects)

### 3. Efficiency
```
Efficiency(E) = Speedup / P = T_seq / (P × T_par)
```
- Range: 0 to 1 (0% to 100%)
- 100% efficiency means perfect parallelization
- Typically decreases as P increases

### 4. Scalability
- **Strong Scaling**: Fixed problem size, increase processors
- **Weak Scaling**: Increase problem size with processors
- **Iso-efficiency**: How problem size must grow with P to maintain efficiency

## Fundamental Laws

### 1. Amdahl's Law (1967)
Predicts maximum speedup given parallel portion of code.

```
Speedup ≤ 1 / (f + (1 - f)/P)
```
Where:
- `f`: Fraction of program that must be executed sequentially (0 ≤ f ≤ 1)
- `P`: Number of processors

#### Implications:
- Even small sequential portions limit speedup
- Maximum speedup = 1/f (as P → ∞)
- Example: If 10% sequential (f=0.1), max speedup = 10× regardless of P

### 2. Gustafson's Law (1988)
Accounts for problem scaling with available processors.

```
Speedup = P + (1 - P) × f
```
Where:
- `f`: Sequential fraction of scaled problem
- `P`: Number of processors

#### Implications:
- With larger problems, parallel portion dominates
- Speedup can scale linearly with P for large problems
- More optimistic than Amdahl's Law for scalable problems

### 3. Karp-Flatt Metric
Measures experimental parallel overhead.

```
e = (1/S - 1/P) / (1 - 1/P)
```
Where:
- `S`: Measured speedup
- `P`: Number of processors
- `e`: Experimentally determined sequential fraction

#### Use:
- Diagnose scalability problems
- Distinguish between algorithmic and implementation issues

## Performance Bottlenecks

### 1. Communication Overhead
- Time spent sending/receiving messages
- Includes latency and bandwidth limitations
- Can dominate execution time for fine-grained parallelism

### 2. Load Imbalance
- Uneven distribution of work among processors
- Some processors idle while others work
- Particularly problematic for irregular problems

### 3. Synchronization Overhead
- Time spent waiting at barriers or locks
- Can create serialization points
- Reduces effective parallelism

### 4. Memory Hierarchy Effects
- **Cache Misses**: Data not in cache, must fetch from memory
- **False Sharing**: Different processors modifying same cache line
- **NUMA Effects**: Non-uniform memory access times

### 5. Resource Contention
- Competition for shared resources (memory bandwidth, I/O, network)
- Can create bottlenecks even with good algorithm design

## Performance Measurement Techniques

### 1. Profiling
- **Instrumentation**: Insert timing calls in code
- **Sampling**: Periodically check program counter
- **Hardware Counters**: Use CPU performance monitoring units

### Common Profiling Tools:
- **gprof**: Statistical profiler for C/C++
- **perf**: Linux performance analysis tool
- **Intel VTune**: Advanced performance profiling
- **NVIDIA Nsight**: GPU performance analysis
- **TAU**: Portable profiling toolkit for parallel programs

### 2. Tracing
- Record detailed timeline of events
- Useful for understanding communication patterns
- Tools: Score-P, Extrae, Vampir

### 3. Benchmarking
- Standardized tests to compare systems/algorithms
- **Microbenchmarks**: Measure specific operations
- **Kernel Benchmarks**: Measure computational kernels
- **Application Benchmarks**: Full application performance

## Performance Optimization Strategies

### 1. Algorithm Selection
- Choose algorithm with better parallel characteristics
- Consider communication patterns and data dependencies
- Balance between algorithmic efficiency and parallelizability

### 2. Data Decomposition
- **Domain Decomposition**: Partition data space among processors
- **Functional Decomposition**: Partition by computational tasks
- **Hybrid Approaches**: Combine domain and functional decomposition

### 3. Communication Optimization
- **Message Aggregation**: Combine small messages
- **Communication-Computation Overlap**: Hide latency with computation
- **Topology-Aware Mapping**: Match communication pattern to network

### 4. Load Balancing
- **Static**: Pre-determined work distribution
- **Dynamic**: Work assigned during execution
- **Adaptive**: Adjust based on runtime measurements

### 5. Memory Optimization
- **Data Locality**: Keep related data together
- **Cache Blocking**: Organize computations to fit in cache
- **Prefetching**: Load data before it's needed

## Performance Modeling

### 1. Analytical Models
- Mathematical formulas predicting performance
- Based on algorithm characteristics and hardware parameters
- Useful for algorithm design and system selection

### 2. Empirical Models
- Based on measurements from actual runs
- Can capture complex interactions not in analytical models
- Requires representative workloads

### 3. Simulation
- Detailed simulation of hardware and software
- High accuracy but computationally expensive
- Tools: gem5, SST, SimGrid

## Case Studies

### 1. Matrix Multiplication
- **Algorithm**: Cannon's algorithm, SUMMA
- **Bottlenecks**: Communication for matrix distribution
- **Optimizations**: Blocking for cache, communication-computation overlap

### 2. N-body Simulation
- **Algorithm**: Barnes-Hut, Fast Multipole Method
- **Bottlenecks**: Load imbalance, communication for force calculation
- **Optimizations**: Spatial decomposition, tree-based algorithms

### 3. Computational Fluid Dynamics
- **Algorithm**: Finite difference/volume/element methods
- **Bottlenecks**: Neighbor communication, solver convergence
- **Optimizations**: Domain decomposition, multigrid methods

## Practical Performance Analysis Workflow

### Step 1: Establish Baseline
- Measure sequential performance
- Identify computational hotspots
- Understand algorithm complexity

### Step 2: Parallelize
- Start with simplest parallel version
- Measure speedup and efficiency
- Identify major bottlenecks

### Step 3: Optimize
- Address identified bottlenecks
- Iterate with measurement
- Balance optimization effort vs performance gain

### Step 4: Scale
- Test weak and strong scaling
- Identify scaling limits
- Understand resource requirements

## Common Pitfalls

### 1. Over-optimization
- Spending too much time on minor optimizations
- Ignoring algorithmic improvements
- Optimizing before measuring

### 2. Wrong Metrics
- Focusing on wrong performance metric
- Ignoring energy efficiency or memory usage
- Not considering total cost of ownership

### 3. Platform-Specific Optimizations
- Over-optimizing for specific hardware
- Reducing portability
- Creating maintenance burden

### 4. Ignoring Variability
- Not accounting for system noise
- Single measurement instead of statistical analysis
- Ignoring worst-case performance

## Future Trends

### 1. Energy Efficiency
- Performance per watt becoming critical
- Dynamic voltage and frequency scaling
- Heterogeneous computing for energy efficiency

### 2. Machine Learning for Optimization
- Auto-tuning of parameters
- Performance prediction models
- Intelligent runtime systems

### 3. Cross-layer Optimization
- Coordinated optimization across hardware, system software, and applications
- Domain-specific architectures
- Hardware/software co-design

### 4. Quantum-Classical Hybrid
- Performance analysis of quantum algorithms
- Integration with classical HPC
- New performance metrics for quantum advantage

## Summary

Performance analysis is an iterative process of measurement, analysis, and optimization. The key principles are:
1. **Measure first**: Use profiling to identify bottlenecks
2. **Understand limits**: Apply Amdahl's and Gustafson's laws
3. **Optimize systematically**: Address biggest bottlenecks first
4. **Consider scalability**: Test both strong and weak scaling
5. **Balance trade-offs**: Performance vs development time, portability, maintainability

Effective parallel programming requires not just making code run in parallel, but making it run efficiently in parallel. This requires understanding both the algorithmic aspects and the hardware characteristics.

---

**Next**: [Practical Exercises and Applications](exercises/)