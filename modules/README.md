# Learning Modules

Structured learning path for High Performance Computing concepts, organized by difficulty level.

## Learning Path Overview

### 🟢 **01-fundamentals/** - Beginner Level
**Prerequisites**: Basic programming knowledge in C/C++ or Python  
**Duration**: 2-3 weeks  
**Topics**:
1. **01-parallel-concepts/** - Understanding parallelism, concurrency, and distributed computing
2. **02-mpi-hello-world/** - First MPI programs and basic communication
3. **03-openmp-basics/** - Shared memory parallelism with OpenMP
4. **04-performance-measurement/** - Benchmarking and performance analysis

### 🟡 **02-intermediate/** - Intermediate Level  
**Prerequisites**: Completion of fundamentals or equivalent experience  
**Duration**: 4-5 weeks  
**Topics**:
1. **01-collective-operations/** - MPI collective communication (broadcast, scatter, gather, reduce)
2. **02-hybrid-mpi-openmp/** - Combining MPI and OpenMP for hybrid parallelism
3. **03-optimization-techniques/** - Performance optimization strategies
4. **04-debugging-parallel/** - Tools and techniques for debugging parallel applications

### 🔴 **03-advanced/** - Advanced Level
**Prerequisites**: Strong understanding of intermediate concepts  
**Duration**: 4-6 weeks  
**Topics**:
1. **01-gpu-computing/** - GPU programming with CUDA and OpenCL
2. **02-advanced-mpi-patterns/** - Complex MPI communication patterns
3. **03-job-scheduling/** - Cluster job scheduling with SLURM/PBS
4. **04-cloud-hpc/** - HPC in cloud environments (AWS, Google Cloud, Azure)

## Module Structure

Each module directory contains:

```
module-name/
├── README.md              # Module overview and learning objectives
├── theory/               # Theoretical concepts and explanations
│   ├── concepts.md       # Key concepts
│   ├── examples.md       # Worked examples
│   └── references.md     # Additional resources
├── exercises/            # Practice problems
│   ├── beginner/         # Basic exercises
│   ├── intermediate/     # Intermediate challenges  
│   └── solutions/        # Exercise solutions
└── code/                 # Code examples (linked from examples/)
    ├── c/               # C implementations
    ├── cpp/             # C++ implementations
    └── python/          # Python implementations
```

## Learning Approach

### 1. **Theory First**
- Read the theoretical concepts in `theory/concepts.md`
- Understand the key principles before coding
- Review worked examples in `theory/examples.md`

### 2. **Hands-on Practice**
- Start with simple examples in the `code/` directory
- Modify and experiment with the code
- Run benchmarks to understand performance characteristics

### 3. **Exercise Reinforcement**
- Attempt exercises in the `exercises/` directory
- Start with beginner exercises and progress to advanced
- Check solutions only after attempting the problems

### 4. **Project Application**
- Apply concepts to real projects in the `projects/` directory
- Document your learning in `learning-journal/`

## Recommended Study Schedule

### Week 1-2: Fundamentals
- Day 1-3: Parallel concepts and theory
- Day 4-7: MPI basics and "Hello World"
- Day 8-10: OpenMP parallel regions
- Day 11-14: Performance measurement basics

### Week 3-6: Intermediate
- Week 3: Collective operations
- Week 4: Hybrid programming
- Week 5: Optimization techniques
- Week 6: Debugging parallel code

### Week 7-12: Advanced
- Week 7-8: GPU computing
- Week 9: Advanced MPI patterns
- Week 10: Job scheduling
- Week 11-12: Cloud HPC and final project

## Assessment

### Self-Assessment Checklist
- [ ] Can explain the concept in your own words
- [ ] Can implement a basic example without reference
- [ ] Can identify when to use the technique
- [ ] Can debug common issues
- [ ] Can optimize for performance

### Progress Tracking
Use the `learning-journal/progress/` directory to:
1. Record what you've learned each day
2. Note challenges and how you overcame them
3. Track completion of exercises and projects
4. Reflect on key insights

## Getting Help

1. **Check Examples**: Review code in the `examples/` directory
2. **Review Theory**: Re-read concepts in `theory/` directories
3. **Search Documentation**: Look for answers in `docs/concepts/`
4. **Experiment**: Modify code and observe behavior
5. **Community**: Consider joining HPC forums or user groups

## Contributing New Modules

To contribute a new module:
1. Follow the existing directory structure
2. Include comprehensive theory and examples
3. Add exercises with solutions
4. Test all code examples
5. Update this README with the new module information

---

**Start with `01-fundamentals/01-parallel-concepts/` to begin your HPC learning journey!**