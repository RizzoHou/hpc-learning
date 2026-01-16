# Tech Context

## Technology Stack

### Core Technologies
1. **Programming Languages**
   - **C/C++**: For performance-critical MPI/OpenMP implementations
   - **Python**: For accessible examples and data science integration
   - **Julia**: For high-performance scientific computing
   - **Bash/Shell**: For cluster management and job scheduling

2. **Parallel Computing Frameworks**
   - **MPI (Message Passing Interface)**: OpenMPI, MPICH for distributed memory parallelism
   - **OpenMP**: For shared memory parallelism on multi-core CPUs
   - **CUDA**: NVIDIA's platform for GPU computing
   - **OpenCL**: Cross-platform GPU computing
   - **OpenACC**: Directive-based GPU programming

3. **Containerization & Virtualization**
   - **Docker**: For reproducible development environments
   - **Podman**: Docker alternative with rootless containers
   - **Singularity/Apptainer**: HPC-focused container runtime
   - **Kubernetes**: For container orchestration examples

4. **Job Scheduling & Cluster Management**
   - **SLURM**: Simple Linux Utility for Resource Management
   - **PBS/Torque**: Portable Batch System
   - **Apache Mesos**: Distributed systems kernel
   - **Kubernetes**: For modern containerized workloads

### Development Tools
1. **Build Systems**
   - **CMake**: Cross-platform build system
   - **Make**: Traditional build automation
   - **Meson**: Modern build system

2. **Performance Analysis**
   - **gprof**: GNU profiler
   - **perf**: Linux performance analysis tool
   - **Intel VTune**: Advanced performance profiling
   - **NVIDIA Nsight**: GPU performance analysis
   - **Scalasca**: Scalable performance analysis

3. **Debugging Tools**
   - **gdb**: GNU debugger with MPI support
   - **TotalView**: Parallel debugger
   - **Valgrind**: Memory debugging and profiling

## Development Setup

### Local Development Environment
1. **Minimum Requirements**
   - Multi-core CPU (4+ cores recommended)
   - 8GB+ RAM (16GB+ for GPU examples)
   - Linux/macOS/Windows with WSL2
   - Docker or Podman installed

2. **Recommended Setup**
   - Linux distribution (Ubuntu 20.04+, CentOS 7+)
   - Development tools: gcc/g++, python3, julia
   - MPI implementation: OpenMPI or MPICH
   - Docker with GPU support (for CUDA examples)

### Containerized Development
```bash
# Example Docker setup for MPI development
docker run -it --rm \
  --name mpi-dev \
  -v $(pwd):/workspace \
  openmpi/mpi:latest
```

### Cloud HPC Setup
- **AWS**: EC2 instances, ParallelCluster
- **Google Cloud**: Compute Engine, HPC Toolkit
- **Azure**: Virtual Machines, CycleCloud
- **Oracle Cloud**: HPC instances

## Dependencies

### Core Dependencies
1. **MPI Implementations**
   - OpenMPI (≥ 4.0.0)
   - MPICH (≥ 3.4.0)

2. **Python Packages**
   - mpi4py (for MPI in Python)
   - numpy, scipy (scientific computing)
   - numba (JIT compilation)
   - dask (parallel computing)

3. **Julia Packages**
   - MPI.jl (MPI interface)
   - CUDA.jl (GPU computing)
   - Distributed.jl (built-in distributed computing)

### Optional Dependencies
1. **GPU Computing**
   - NVIDIA CUDA Toolkit (≥ 11.0)
   - cuDNN, cuBLAS libraries
   - NVIDIA drivers

2. **Visualization**
   - matplotlib, plotly (Python)
   - Plots.jl (Julia)
   - ParaView, VisIt (scientific visualization)

## Tool Usage Patterns

### Development Workflow
1. **Local Testing**
   ```bash
   # Compile MPI program
   mpicc -o hello hello.c
   
   # Run with 4 processes
   mpirun -np 4 ./hello
   ```

2. **Container Development**
   ```bash
   # Build Docker image with MPI
   docker build -t hpc-example .
   
   # Run MPI program in container
   docker run --rm hpc-example mpirun -np 4 ./hello
   ```

3. **Cluster Submission**
   ```bash
   # SLURM job script
   #!/bin/bash
   #SBATCH --nodes=2
   #SBATCH --ntasks-per-node=4
   mpirun ./program
   ```

### Performance Analysis Workflow
1. **Compile with profiling flags**
2. **Run with performance counters**
3. **Analyze results with visualization tools**
4. **Iterate with optimizations**

## Technical Constraints

### Platform Compatibility
- Primary target: Linux (most HPC clusters run Linux)
- Secondary: macOS with MPI via Homebrew
- Tertiary: Windows via WSL2 or virtual machines

### Resource Requirements
- MPI examples require multiple processes (can be on single machine)
- GPU examples require NVIDIA GPU with CUDA support
- Large-scale examples may require cloud resources

### Learning Curve Considerations
- Start with simple examples before complex patterns
- Provide clear error messages and troubleshooting guides
- Include both command-line and script-based approaches