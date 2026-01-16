# Exercise 1 Solutions: Basic Parallel Concepts

## Part A: Conceptual Questions

### Question 1: Types of Parallelism

1. **Web server handling multiple client requests**: Task parallelism (different requests are different tasks)
2. **Adding 100 to each element of array**: Data parallelism (same operation on different data elements)
3. **Compiler stages on different program parts**: Pipeline parallelism (different stages processing different parts) with some data parallelism within stages
4. **Video encoder processing different frames**: Primarily data parallelism (same encoding on different frames), possibly with pipeline parallelism if multiple encoding stages
5. **Scientific simulation with forces and positions**: Task parallelism (different calculations: forces vs positions) with data parallelism within each calculation

### Question 2: Architecture Matching

1. **Multicore CPU with shared memory** → B. OpenMP (shared memory programming model)
2. **Cluster of computers with distributed memory** → A. MPI (message passing for distributed memory)
3. **NVIDIA GPU with many simple cores** → C. CUDA (NVIDIA's GPU programming model)
4. **Hybrid system with CPU and GPU** → D. MPI + OpenMP + CUDA (hybrid model for heterogeneous systems)

### Question 3: Performance Metrics

Given: T_seq = 100s, T_par(4) = 30s, P = 4

1. **Speedup**: S = T_seq / T_par = 100 / 30 = 3.33
2. **Efficiency**: E = S / P = 3.33 / 4 = 0.8325 or 83.25%
3. **Linear speedup on 8 processors**: If linear speedup, S = P = 8, so T_par(8) = T_seq / 8 = 100 / 8 = 12.5s
4. **Sequential fraction using Amdahl's Law**: 
   From S = 1 / (f + (1-f)/P)
   3.33 = 1 / (f + (1-f)/4)
   Solving: f ≈ 0.1 or 10% sequential portion

## Part B: Problem Analysis

### Problem 1: Image Processing

1. **Data parallel operations**: All four operations can use data parallelism by processing different pixels or blocks of pixels independently.
2. **Pipeline parallelism**: Yes, could create a pipeline where:
   - Stage 1: RGB to grayscale
   - Stage 2: Gaussian blur  
   - Stage 3: Edge detection
   - Stage 4: Thresholding
   Different images or image regions flow through the pipeline stages.
3. **Challenges**:
   - Data dependencies between operations (blur needs neighborhood pixels)
   - Load balancing for irregular image regions
   - Memory bandwidth limitations
   - Synchronization between pipeline stages

### Problem 2: Matrix Operations

1. **Two parallelization approaches**:
   - **Block decomposition**: Divide matrices into blocks, assign blocks to processors
   - **Row/column decomposition**: Assign rows of A or columns of B to processors
2. **Distribution for 4 processors**: Use 2×2 block decomposition. Each processor gets 500×500 blocks of A, B, C, D.
3. **Communication required**:
   - Broadcast of blocks for matrix multiplication
   - Reduction for summing partial results
   - Data movement for block rotation in Cannon's algorithm
4. **For 100 processors**: Use 10×10 block decomposition. Need more sophisticated communication patterns (e.g., 2D decomposition). Communication overhead becomes more significant relative to computation.

### Problem 3: Web Server Load Balancing

1. **Appropriate parallelism**: Task parallelism (different requests are different tasks)
2. **Load balancing**: Use a thread pool with work queue. Dynamic assignment of requests to available threads.
3. **Synchronization needed**:
   - Queue access synchronization
   - Database connection pooling
   - Shared resource access (logging, configuration)
4. **Performance measurement**:
   - Requests per second (throughput)
   - Average response time (latency)
   - CPU utilization
   - Queue length and wait times

## Part C: Design Exercise

### Exercise: Parallel File Search

1. **Parallelization strategy**:
   - Master-worker pattern with work queue
   - Master thread maintains queue of files to search
   - Worker threads (7 workers + 1 master) take files from queue
   - Each worker searches assigned file, returns results to master
2. **Potential bottlenecks**:
   - Queue contention (use lock-free or fine-grained locking)
   - I/O bandwidth (disk read speed)
   - Master thread becoming bottleneck for result aggregation
3. **Speedup estimation**:
   - Assume 95% parallelizable (file I/O and search)
   - Using Amdahl's Law: S_max = 1 / (0.05 + 0.95/8) ≈ 6.15×
   - Realistic: 5-6× speedup due to overhead
4. **Handling challenges**:
   - **Different file sizes**: Dynamic work assignment (small files bundled, large files split)
   - **Dynamic load balancing**: Work stealing when threads idle
   - **Result aggregation**: Asynchronous reporting to avoid master bottleneck

### Exercise: Monte Carlo Simulation

1. **Parallel implementation**:
   - Data parallelism: Each processor generates and tests random points
   - No communication during point generation/testing
   - Final reduction to sum counts from all processors
2. **Decomposition**: Pure data parallelism (embarrassingly parallel)
3. **Communication requirements**:
   - Initial broadcast of random seed or seed strategy
   - Final reduction of point counts
   - Minimal communication (ideal for parallelization)
4. **Scalability analysis**:
   - **Strong scaling**: Excellent near-linear speedup (minimal communication)
   - **Weak scaling**: Perfect efficiency (problem size scales with processors)
   - Memory requirements constant per processor

## Part D: Critical Thinking

### Discussion 1: Amdahl vs Gustafson

1. **Amdahl's Law too pessimistic** when:
   - Problem size can increase with available processors
   - Sequential portion is not fixed but decreases with problem size
   - Real applications often scale problem size with resources (bigger simulations on bigger machines)

2. **Gustafson's Law overly optimistic** when:
   - Problem size is inherently limited (e.g., real-time constraints)
   - Memory or other resources limit problem scaling
   - Sequential portion doesn't scale down with larger problems

3. **Real-world examples**:
   - **Amdahl**: Video encoding fixed-length video (fixed problem)
   - **Gustafson**: Climate simulation (larger domain with more processors)

### Discussion 2: Hardware Trends

1. **Shift to more cores**:
   - Requires explicit parallel programming (no more "free lunch" from faster clocks)
   - Increased importance of parallel algorithms and data structures
   - More focus on scalability and load balancing

2. **Heterogeneous computing challenges**:
   - Multiple programming models (CPU, GPU, FPGA)
   - Data movement between different memory spaces
   - Load balancing across different processor types
   - Development and debugging complexity

3. **Quantum computing impact**:
   - New programming models (quantum circuits, hybrid algorithms)
   - Different notion of parallelism (quantum superposition)
   - Integration with classical HPC systems
   - New performance metrics (quantum volume, circuit depth)

### Discussion 3: Programming Model Selection

**Factors to consider**:

1. **Hardware target**:
   - Single node: OpenMP, pthreads
   - Cluster: MPI
   - GPU: CUDA/OpenCL
   - Hybrid: Combination

2. **Problem characteristics**:
   - Regular data parallelism: OpenMP, CUDA
   - Irregular task parallelism: Task-based models
   - Communication patterns: MPI for complex patterns

3. **Development constraints**:
   - Team expertise
   - Time to solution
   - Performance requirements
   - Portability needs

4. **Software ecosystem**:
   - Existing libraries and frameworks
   - Tool support (debuggers, profilers)
   - Community and documentation

5. **Long-term maintainability**:
   - Code complexity
   - Testing and debugging difficulty
   - Future hardware evolution

**Recommendation process**:
1. Profile sequential version to identify hotspots
2. Analyze data dependencies and communication patterns
3. Consider hardware availability and constraints
4. Start with simplest model that meets requirements
5. Plan for evolution (e.g., OpenMP first, add MPI later if needed)

## Learning Outcomes

By completing these exercises, you should now be able to:
1. Classify different types of parallelism in real-world scenarios
2. Match programming models to hardware architectures
3. Calculate and interpret parallel performance metrics
4. Analyze problems for parallelization potential
5. Design basic parallel algorithms considering decomposition, communication, and load balancing
6. Critically evaluate the applicability of performance laws
7. Make informed decisions about programming model selection

These foundational skills will prepare you for the practical implementation of parallel programs in subsequent modules.