# Parallel Programming Models

## Overview
Parallel programming models provide abstractions that allow programmers to express parallelism without dealing with low-level hardware details. Different models are suited to different architectures and problem types.

## Classification of Programming Models

### Based on Memory View
1. **Shared Memory Models**: Threads/processes share address space
2. **Distributed Memory Models**: Processes have separate address spaces
3. **Partitioned Global Address Space (PGAS)**: Hybrid approach with global view but local partitions

### Based on Parallelism Type
1. **Data Parallel**: Same operation on multiple data elements
2. **Task Parallel**: Different operations executed concurrently
3. **Pipeline Parallel**: Data flows through processing stages

## Major Programming Models

### 1. Message Passing Interface (MPI)
- **Architecture**: Distributed memory systems (clusters)
- **Concept**: Processes communicate by sending/receiving messages
- **Key Features**:
  - Point-to-point communication (send/receive)
  - Collective operations (broadcast, scatter, gather, reduce)
  - Process groups and communicators
- **Advantages**: Highly portable, scalable to thousands of nodes
- **Disadvantages**: Explicit communication, complex error handling
- **Examples**: OpenMPI, MPICH, Intel MPI

### 2. OpenMP (Open Multi-Processing)
- **Architecture**: Shared memory systems (multicore CPUs)
- **Concept**: Directive-based parallelism using compiler pragmas
- **Key Features**:
  - Parallel regions and worksharing constructs
  - Data sharing attributes (shared, private, reduction)
  - Synchronization (barrier, critical, atomic)
- **Advantages**: Incremental parallelization, relatively easy to learn
- **Disadvantages**: Limited to single node, less control than threads
- **Examples**: GCC, Clang, Intel Compiler with OpenMP support

### 3. POSIX Threads (pthreads)
- **Architecture**: Shared memory systems
- **Concept**: Low-level thread API for C/C++
- **Key Features**:
  - Thread creation and management
  - Mutexes, condition variables for synchronization
  - Thread-local storage
- **Advantages**: Fine-grained control, standard across Unix-like systems
- **Disadvantages**: Complex error-prone API, manual memory management
- **Examples**: Standard on Linux, macOS, other Unix systems

### 4. CUDA (Compute Unified Device Architecture)
- **Architecture**: NVIDIA GPUs
- **Concept**: Heterogeneous computing with CPU host and GPU device
- **Key Features**:
  - Kernel functions executed on GPU
  - Thread hierarchy (threads, blocks, grids)
  - Memory hierarchy (global, shared, constant, texture)
- **Advantages**: High performance for data-parallel problems
- **Disadvantages**: NVIDIA hardware only, steep learning curve
- **Examples**: NVIDIA GPU computing platform

### 5. OpenCL (Open Computing Language)
- **Architecture**: Heterogeneous systems (CPUs, GPUs, FPGAs)
- **Concept**: Cross-platform parallel computing standard
- **Key Features**:
  - Platform and device abstraction
  - Kernel programming in C-like language
  - Memory objects and command queues
- **Advantages**: Vendor-neutral, supports diverse hardware
- **Disadvantages**: Verbose API, performance portability challenges
- **Examples**: AMD, Intel, NVIDIA implementations

### 6. OpenACC
- **Architecture**: Accelerators (GPUs, manycore)
- **Concept**: Directive-based like OpenMP but for accelerators
- **Key Features**:
  - Compiler directives for offloading
  - Data management (copyin, copyout, create)
  - Parallel loop constructs
- **Advantages**: Easy porting of existing code, less invasive than CUDA
- **Disadvantages**: Less control than CUDA/OpenCL, compiler dependence
- **Examples**: NVIDIA, GCC, PGI compilers

## Higher-Level Models and Frameworks

### 1. MapReduce
- **Concept**: Process large datasets with parallel, distributed algorithm
- **Key Operations**: Map (process key-value pairs), Reduce (aggregate results)
- **Examples**: Hadoop, Apache Spark
- **Use Cases**: Big data processing, log analysis, web indexing

### 2. Actor Model
- **Concept**: Concurrent computation with actors that communicate via messages
- **Key Features**: Actors as independent units, message passing, no shared state
- **Examples**: Erlang, Akka (Scala/Java), Orleans (.NET)
- **Use Cases**: Distributed systems, reactive applications

### 3. Dataflow Programming
- **Concept**: Program as directed graph of operations (nodes) and data (edges)
- **Key Features**: Implicit parallelism, data dependencies drive execution
- **Examples**: TensorFlow, Apache NiFi, LabVIEW
- **Use Cases**: Signal processing, machine learning, scientific workflows

### 4. Task-based Parallelism
- **Concept**: Decompose work into tasks with dependencies
- **Key Features**: Task graphs, dependency tracking, work stealing
- **Examples**: Intel TBB, C++17 parallel algorithms, StarPU
- **Use Cases**: Irregular parallelism, dynamic workloads

## Language-Specific Parallel Features

### C/C++
- **Standard Threads**: `<thread>`, `<mutex>`, `<atomic>` (C++11+)
- **Parallel Algorithms**: `<algorithm>` with execution policies (C++17)
- **Coroutines**: Asynchronous operations (C++20)
- **External Libraries**: OpenMP, MPI, CUDA, OpenCL bindings

### Python
- **Multiprocessing**: `multiprocessing` module for process-based parallelism
- **Threading**: `threading` module for I/O-bound tasks
- **Concurrent Futures**: High-level interface for thread/process pools
- **External Libraries**: mpi4py (MPI), numba (JIT with GPU), dask (distributed)

### Julia
- **Built-in Parallelism**: `@threads`, `@distributed`, `@spawn`
- **Distributed Computing**: `@everywhere`, remote references, channels
- **GPU Support**: CUDA.jl, AMDGPU.jl, oneAPI.jl
- **External Packages**: MPI.jl, DistributedArrays.jl

### Java
- **Threads**: `java.lang.Thread`, `Runnable`, `Callable`
- **Executors**: Thread pools in `java.util.concurrent`
- **Fork/Join Framework**: Work stealing for recursive tasks
- **Parallel Streams**: Functional-style parallel operations

## Hybrid Programming Models

### Common Combinations
1. **MPI + OpenMP**: Distributed memory between nodes, shared memory within nodes
2. **MPI + CUDA**: Cluster of GPU-accelerated nodes
3. **OpenMP + OpenACC**: CPU parallelism with GPU offloading
4. **MPI + OpenMP + CUDA**: Full hybrid model for modern supercomputers

### Benefits of Hybrid Models
- **Better Resource Utilization**: Match programming model to hardware
- **Improved Scalability**: Combine strengths of different models
- **Performance Optimization**: Fine-tune for specific architectures

### Challenges
- **Complexity**: Multiple programming models in same application
- **Debugging**: More difficult with mixed models
- **Performance Tuning**: Interactions between models can be subtle

## Selecting a Programming Model

### Decision Factors
1. **Hardware Architecture**
   - Multicore CPU: OpenMP, pthreads, C++ threads
   - GPU: CUDA, OpenCL, OpenACC
   - Cluster: MPI, MapReduce
   - Hybrid: MPI+X combinations

2. **Problem Characteristics**
   - Regular data parallelism: OpenMP, CUDA
   - Irregular task parallelism: Task-based models, actors
   - Large-scale data processing: MapReduce, dataflow

3. **Development Constraints**
   - Time to solution: Higher-level models (OpenMP, OpenACC)
   - Performance requirements: Lower-level models (MPI, CUDA)
   - Team expertise: Match to existing skills

4. **Portability Requirements**
   - Cross-platform: OpenCL, MPI
   - Vendor-specific: CUDA (NVIDIA), Metal (Apple)
   - Cloud deployment: Container-friendly models

## Performance Considerations

### Communication vs Computation
- **Granularity**: Balance between communication overhead and parallel work
- **Overlap**: Hide communication latency with computation
- **Batching**: Aggregate small messages into larger ones

### Memory Access Patterns
- **Spatial Locality**: Access contiguous memory locations
- **Temporal Locality**: Reuse recently accessed data
- **False Sharing**: Different cores modifying same cache line

### Load Balancing
- **Static**: Work distribution determined before execution
- **Dynamic**: Work assigned during execution (work stealing)
- **Adaptive**: Adjust based on runtime measurements

## Tools and Ecosystem

### Development Tools
- **Compilers**: GCC, Clang, Intel, NVIDIA nvcc
- **Debuggers**: TotalView, DDT, gdb with MPI/OpenMP support
- **Profilers**: Intel VTune, NVIDIA Nsight, TAU, Scalasca

### Libraries and Frameworks
- **Numerical Libraries**: BLAS, LAPACK, FFTW (parallel versions)
- **Communication Libraries**: UCX, libfabric (high-performance networking)
- **Scheduling**: SLURM, PBS, Kubernetes (for containerized workloads)

## Future Trends

### 1. Domain-Specific Languages (DSLs)
- Specialized languages for specific problem domains
- Examples: Halide (image processing), Triton (GPU programming)

### 2. AI-Assisted Parallelization
- Machine learning for automatic parallelization
- Performance prediction and optimization

### 3. Quantum-Classical Hybrid
- Combining quantum and classical processors
- Programming models for quantum advantage

### 4. Serverless HPC
- Function-as-a-service for HPC workloads
- Event-driven parallel execution

## Summary

Choosing the right parallel programming model depends on hardware, problem characteristics, and development constraints. Modern HPC often requires hybrid approaches combining multiple models. The key is to match the abstraction level to the problem: higher-level models for productivity, lower-level models for performance.

As hardware becomes more heterogeneous and applications more complex, understanding multiple programming models and how to combine them effectively becomes increasingly important for HPC developers.

---

**Next**: [Performance Analysis and Laws](04-performance-analysis.md)