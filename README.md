# HPC Learning Project

A structured, practical learning path for High Performance Computing (HPC) concepts and implementations.

## Project Overview

This project provides a comprehensive learning path for High Performance Computing, covering parallel computing fundamentals, MPI, OpenMP, GPU computing, and cluster management. Designed for students, researchers, and software engineers transitioning to high-performance applications.

## Current Status

### ✅ **Foundation Complete** (Phase 1)
- **Project Structure**: Comprehensive directory organization established
- **Development Environments**: Docker setup for MPI development ready
- **Basic Examples**: MPI "Hello World" in C and Python implemented
- **Learning Framework**: Modules, exercises, and learning journal created
- **Documentation**: Memory bank and README files comprehensive

### ✅ **Module 01 Complete** (Parallel Concepts)
- **Theory**: 4 comprehensive documents covering parallel computing fundamentals
- **Exercises**: Hands-on problems with detailed solutions
- **Code Examples**: Python demonstrations of data and task parallelism
- **Module Structure**: Template established for future modules

### 🔄 **In Progress** (Phase 2)
- **Content Development**: Working on remaining fundamentals modules (02-04)
- **Environment Expansion**: OpenMP and SSH HPC setups in development
- **Example Enhancement**: Adding collective operations and performance benchmarks

### 📅 **Planned** (Phase 3)
- **Advanced Topics**: GPU computing, job scheduling, cloud HPC
- **Real-world Projects**: Matrix multiplication, Monte Carlo simulations
- **Community Features**: Contribution guidelines, benchmarking framework

**Overall Progress**: 50% complete (First module complete, infrastructure ready)

## Project Structure

### 📁 **docs/** - Project Documentation
- **development/** - Git workflow, commit standards, development guidelines
- **setup/** - Environment setup for Mac M4, SSH HPC access, troubleshooting
- **concepts/** - Theoretical explanations of HPC concepts
- **tutorials/** - Step-by-step learning guides

### 📁 **environments/** - Development Environments
- **docker/** - Containerized environments for reproducible development
- **mac-m4/** - MacBook M4 specific setup scripts (ARM architecture)
- **ssh-hpc/** - Guides and scripts for university HPC access via SSH

### 📁 **modules/** - Structured Learning Path
- **01-fundamentals/** - Basic parallel computing concepts
  - 01-parallel-concepts/ - ✅ Complete: Theory, exercises, code examples
  - 02-mpi-hello-world/ - First MPI programs
  - 03-openmp-basics/ - Shared memory parallelism
  - 04-performance-measurement/ - Benchmarking basics
- **02-intermediate/** - Advanced patterns and optimization
  - 01-collective-operations/ - MPI collective communication
  - 02-hybrid-mpi-openmp/ - Hybrid programming
  - 03-optimization-techniques/ - Performance optimization
  - 04-debugging-parallel/ - Debugging parallel applications
- **03-advanced/** - Specialized topics
  - 01-gpu-computing/ - GPU programming (CUDA/OpenCL)
  - 02-advanced-mpi-patterns/ - Complex MPI patterns
  - 03-job-scheduling/ - Cluster job scheduling (SLURM/PBS)
  - 04-cloud-hpc/ - Cloud HPC deployment

### 📁 **examples/** - Runnable Code Examples
- **c/** - C language implementations (performance-focused)
  - mpi/ - MPI examples in C
  - openmp/ - OpenMP examples in C
  - hybrid/ - Hybrid MPI+OpenMP examples
- **cpp/** - C++ language implementations
  - mpi/ - MPI examples in C++
  - openmp/ - OpenMP examples in C++
  - hybrid/ - Hybrid examples in C++
- **python/** - Python implementations (rapid prototyping)
  - mpi4py/ - MPI with mpi4py
  - multiprocessing/ - Python multiprocessing
  - concurrent-futures/ - Concurrent futures
- **benchmarks/** - Performance comparison examples

### 📁 **projects/** - Complete Applications
- **matrix-multiplication/** - Parallel matrix multiplication
- **monte-carlo-simulation/** - Monte Carlo simulations
- **n-body-problem/** - N-body gravitational simulations
- **image-processing/** - Parallel image processing

### 📁 **exercises/** - Practice Problems
- **beginner/** - Basic parallel programming exercises
- **intermediate/** - Intermediate challenges
- **advanced/** - Advanced optimization problems

### 📁 **scripts/** - Automation Tools
- **build/** - Build scripts for different environments
- **test/** - Testing and validation scripts
- **benchmark/** - Performance benchmarking scripts
- **utils/** - Utility scripts for common tasks

### 📁 **learning-journal/** - Personal Learning Notes
- **concepts/** - Notes on HPC concepts
- **experiments/** - Records of experiments and tests
- **insights/** - Key learnings and insights
- **progress/** - Progress tracking and reflections

### 📁 **memorybank/** - Project Knowledge Base
- Core project documentation and context for AI-assisted development

## Getting Started

### Prerequisites
- Basic programming knowledge in C/C++ or Python
- Access to a multi-core computer (MacBook M4 or similar)
- Optional: SSH access to university HPC cluster
- Docker (for containerized environments)

### Quick Start
1. **Docker Environment (Recommended):**
   ```bash
   # Build and run MPI container
   cd environments/docker/mpi-basic
   docker build -t mpi-basic .
   docker run -it --rm mpi-basic
   
   # Inside container, run MPI example
   cd /workspace/examples/c/mpi
   mpicc -o hello_world hello_world.c
   mpirun -np 4 ./hello_world
   ```

2. **Local Development (If MPI installed):**
   ```bash
   # Run first MPI example
   cd examples/c/mpi
   mpicc -o hello_world hello_world.c
   mpirun -np 4 ./hello_world
   
   # Or Python version
   cd examples/python/mpi4py
   mpirun -np 4 python hello_world.py
   ```

3. **Track Your Learning:**
   ```bash
   # Start your learning journal
   cp learning-journal/progress/template.md learning-journal/progress/daily-log-$(date +%Y-%m-%d).md
   # Edit with your daily learning notes
   ```

## Learning Path

### Phase 1: Fundamentals (Weeks 1-2)
1. ✅ Parallel computing concepts (Module 01 complete)
2. Basic MPI programming (Module 02 in progress)
3. OpenMP basics (Module 03 planned)
4. Performance measurement (Module 04 planned)

### Phase 2: Intermediate (Weeks 3-8)
1. Collective operations
2. Hybrid programming
3. Optimization techniques
4. Debugging parallel code

### Phase 3: Advanced (Weeks 9-12)
1. GPU computing
2. Advanced MPI patterns
3. Job scheduling
4. Cloud HPC deployment

## Development Workflow

### Git Commits
This project uses Conventional Commits. All commit messages must follow the format:
```
<type>[optional scope]: <description>

[optional body]

[optional footer]
```

Valid types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`

### Memory Bank
The `memorybank/` directory contains project knowledge that persists across AI assistant sessions. Key files:
- `projectbrief.md` - Project scope and goals
- `productContext.md` - User needs and success metrics
- `systemPatterns.md` - Architecture and design patterns
- `techContext.md` - Technology stack and setup
- `activeContext.md` - Current work and next steps
- `progress.md` - Project status and milestones

## Contributing

1. Fork the repository
2. Create a feature branch
3. Follow the conventional commits standard
4. Add tests for new features
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

- Check the `docs/troubleshooting.md` for common issues
- Review the `docs/concepts/` directory for theoretical background
- Use the `learning-journal/` to track your personal progress

## Acknowledgments

This project is designed to make HPC learning more accessible and practical. Special thanks to the HPC community for their contributions and insights.

---

**Start your HPC learning journey today!** Begin with `modules/01-fundamentals/01-parallel-concepts/` or check out the quick examples in `examples/c/mpi/`.