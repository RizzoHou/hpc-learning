# Parallel Computing Architectures

## Overview
Parallel computing architectures define how multiple processing elements are organized and how they communicate. Understanding these architectures is crucial for selecting the right programming model and optimizing performance.

## Flynn's Taxonomy

Flynn's taxonomy classifies computer architectures based on the number of concurrent instruction and data streams:

### 1. SISD (Single Instruction, Single Data)
- Traditional sequential computer
- One instruction stream, one data stream
- Example: Classic von Neumann architecture

### 2. SIMD (Single Instruction, Multiple Data)
- Single instruction operates on multiple data elements simultaneously
- Well-suited for data parallelism
- Examples: Vector processors, GPU shader cores, Intel AVX/SSE

### 3. MISD (Multiple Instruction, Single Data)
- Multiple instructions operate on single data stream
- Rarely used in practice
- Example: Fault-tolerant systems with redundancy

### 4. MIMD (Multiple Instruction, Multiple Data)
- Multiple independent processors executing different instructions on different data
- Most common parallel architecture
- Examples: Multicore CPUs, computer clusters

## Memory Organization

### 1. Shared Memory Architecture
- All processors share a common address space
- Communication through reading/writing shared variables
- **Advantages**: Easy to program, fast communication
- **Disadvantages**: Scalability limited by memory bandwidth, cache coherence issues

#### Types of Shared Memory:
- **Uniform Memory Access (UMA)**: Equal access time to all memory (SMP - Symmetric Multiprocessing)
- **Non-Uniform Memory Access (NUMA)**: Access time depends on memory location (common in modern multicore)

### 2. Distributed Memory Architecture
- Each processor has its own private memory
- Communication through message passing
- **Advantages**: Highly scalable, no cache coherence issues
- **Disadvantages**: Explicit communication required, programming complexity

### 3. Hybrid Architecture
- Combination of shared and distributed memory
- Example: Cluster of multicore nodes (distributed memory between nodes, shared within nodes)
- **Advantages**: Balances scalability and programming ease
- **Disadvantages**: Complex programming model

## Common Parallel Architectures

### 1. Multicore Processors
- Multiple CPU cores on single chip
- Shared memory within chip
- Examples: Intel Core i7, AMD Ryzen, Apple M-series
- Programming: OpenMP, pthreads, C++ threads

### 2. Symmetric Multiprocessing (SMP)
- Multiple identical processors sharing memory
- Single operating system image
- Examples: Traditional server systems
- Programming: Similar to multicore but with more processors

### 3. Massively Parallel Processors (MPP)
- Thousands of processors with distributed memory
- High-speed interconnect network
- Examples: Cray XT, IBM Blue Gene
- Programming: MPI, PGAS languages

### 4. Graphics Processing Units (GPUs)
- Originally for graphics, now general-purpose (GPGPU)
- Many simple cores optimized for data parallelism
- Examples: NVIDIA Tesla, AMD Radeon Instinct
- Programming: CUDA, OpenCL, OpenACC

### 5. Computer Clusters
- Network of independent computers
- Commodity hardware with high-speed interconnect
- Examples: Beowulf clusters, cloud instances
- Programming: MPI, MapReduce, distributed frameworks

### 6. Vector Processors
- Specialized for operations on arrays/vectors
- Single instruction operates on entire vector
- Examples: Historical Cray supercomputers, modern SIMD units
- Programming: Vector intrinsics, compiler auto-vectorization

## Interconnection Networks

### Network Topologies
1. **Bus**: Simple but limited bandwidth, contention issues
2. **Ring**: Simple routing, latency increases with size
3. **Mesh/Grid**: Common in multicore chips, scalable
4. **Torus**: Mesh with wrap-around connections
5. **Hypercube**: High connectivity, complex wiring
6. **Fat Tree**: Common in clusters, good bisection bandwidth

### Network Characteristics
- **Latency**: Time to send minimal message
- **Bandwidth**: Maximum data transfer rate
- **Bisection Bandwidth**: Minimum bandwidth when network is cut in half
- **Diameter**: Maximum distance between any two nodes

## Modern Trends

### 1. Heterogeneous Computing
- Mix of different processor types (CPU + GPU + FPGA)
- Each processor optimized for specific tasks
- Examples: AMD APU, NVIDIA DGX, Intel Xeon Phi

### 2. Manycore Processors
- Dozens to hundreds of simpler cores
- Focus on energy efficiency
- Examples: Intel Xeon Phi (Knights Landing), Adapteva Epiphany

### 3. Accelerators
- Specialized hardware for specific computations
- Examples: Google TPU (Tensor Processing Unit), FPGA accelerators
- Programming: Domain-specific languages and frameworks

### 4. Cloud HPC
- HPC resources as a service
- Elastic scaling, pay-per-use
- Examples: AWS ParallelCluster, Google Cloud HPC Toolkit

## Architecture Selection Considerations

### Problem Characteristics
- **Data Parallel Problems**: GPU, SIMD, vector processors
- **Task Parallel Problems**: Multicore, clusters
- **Memory Intensive**: NUMA systems with high bandwidth
- **Communication Intensive**: Systems with low-latency interconnects

### Scale Considerations
- **Small Scale (2-32 cores)**: Multicore, shared memory
- **Medium Scale (32-1024 cores)**: Cluster of multicore nodes
- **Large Scale (1000+ cores)**: MPP systems, GPU clusters

### Cost Considerations
- **Commodity Clusters**: Lower cost, easier maintenance
- **Specialized Systems**: Higher performance, higher cost
- **Cloud HPC**: Operational expense vs capital expense

## Performance Implications

### Memory Hierarchy
```
Registers → L1 Cache → L2 Cache → L3 Cache → Main Memory → Disk
```
- Parallel programs must consider cache effects
- False sharing can degrade performance
- Data locality is critical for performance

### Communication Patterns
- **Nearest Neighbor**: Mesh/torus topologies efficient
- **All-to-All**: Hypercube or fat tree efficient
- **Broadcast**: Tree-based networks efficient

### Load Balancing
- Static vs dynamic load balancing
- Work stealing algorithms
- Domain decomposition strategies

## Case Studies

### 1. Summit Supercomputer (Oak Ridge National Laboratory)
- Hybrid CPU+GPU architecture
- 4,608 nodes, each with 2× IBM POWER9 + 6× NVIDIA V100
- 200 petaflops peak performance
- Programming: MPI + OpenMP + CUDA

### 2. Fugaku Supercomputer (RIKEN, Japan)
- ARM-based manycore architecture
- 158,976 nodes, 7.3 million cores
- 442 petaflops peak performance
- Programming: MPI, OpenMP, ARM SVE

### 3. Google TPU Pod
- Custom tensor processing units
- Optimized for machine learning
- 100+ petaflops for neural network inference
- Programming: TensorFlow, JAX

## Summary

Understanding parallel architectures is essential for writing efficient parallel programs. The architecture determines:
- Which programming models are available
- How communication happens
- What performance bottlenecks to expect
- How to scale applications

Different architectures excel at different types of problems. The trend is toward heterogeneous systems that combine different types of processors, requiring programmers to understand multiple architectures and programming models.

In practice, most HPC applications today run on clusters of multicore nodes, often with GPU accelerators, using hybrid programming models like MPI + OpenMP + CUDA.

---

**Next**: [Parallel Programming Models](03-parallel-programming-models.md)