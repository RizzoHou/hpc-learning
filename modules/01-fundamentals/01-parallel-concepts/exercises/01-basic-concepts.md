# Exercise 1: Basic Parallel Concepts

## Objective
Understand fundamental parallel computing concepts through analysis and problem-solving.

## Prerequisites
- Read theory documents 01-04
- Basic understanding of computer architecture
- Familiarity with any programming language

## Part A: Conceptual Questions

### Question 1: Types of Parallelism
For each scenario below, identify whether it demonstrates:
- Data parallelism
- Task parallelism  
- Pipeline parallelism
- Or a combination

1. A web server handling multiple client requests simultaneously
2. Adding 100 to each element of a 10,000-element array
3. A compiler performing lexical analysis, parsing, and code generation on different parts of the same program
4. A video encoder processing different frames of a video simultaneously
5. A scientific simulation calculating forces between particles while also updating positions

### Question 2: Architecture Matching
Match each architecture type with its best-suited programming model:

Architectures:
1. Multicore CPU with shared memory
2. Cluster of computers with distributed memory
3. NVIDIA GPU with many simple cores
4. Hybrid system with CPU and GPU

Programming Models:
A. MPI (Message Passing Interface)
B. OpenMP
C. CUDA
D. MPI + OpenMP + CUDA

### Question 3: Performance Metrics
A parallel program takes 100 seconds to run sequentially. When run on 4 processors, it takes 30 seconds.

1. Calculate the speedup
2. Calculate the efficiency
3. If the program achieves linear speedup on 8 processors, what would the execution time be?
4. Using Amdahl's Law, estimate the sequential fraction of the program

## Part B: Problem Analysis

### Problem 1: Image Processing
Consider an image processing application that applies the following operations to each pixel:
1. Convert RGB to grayscale
2. Apply Gaussian blur
3. Detect edges using Sobel operator
4. Apply threshold to create binary image

**Questions:**
1. Which operations can be parallelized using data parallelism?
2. Could pipeline parallelism be applied? If so, how?
3. What would be the challenges in parallelizing this application?

### Problem 2: Matrix Operations
You need to compute C = A × B + D where A, B, C, D are 1000×1000 matrices.

**Questions:**
1. Describe two different ways to parallelize matrix multiplication
2. How would you distribute the work among 4 processors?
3. What communication would be required between processors?
4. How would the approach change for 100 processors?

### Problem 3: Web Server Load Balancing
A web server receives requests for different types of content:
- Static HTML pages (fast to serve)
- Database queries (slow, variable time)
- File uploads (medium speed, large data)

**Questions:**
1. What type of parallelism is most appropriate?
2. How would you handle load balancing?
3. What synchronization might be needed?
4. How would you measure performance?

## Part C: Design Exercise

### Exercise: Parallel File Search
Design a parallel algorithm to search for a string in multiple files.

**Requirements:**
- Search for string "error" in 1000 log files
- Each file is 1-10 MB in size
- Available: 8-core machine with shared memory

**Tasks:**
1. Describe your parallelization strategy
2. Identify potential bottlenecks
3. Estimate speedup using Amdahl's Law (make reasonable assumptions)
4. Describe how you would handle:
   - Files of different sizes
   - Dynamic load balancing
   - Result aggregation

### Exercise: Monte Carlo Simulation
Design a parallel Monte Carlo simulation to estimate π.

**Algorithm:**
1. Generate random points in a unit square
2. Count points inside quarter circle
3. π ≈ 4 × (points inside / total points)

**Tasks:**
1. Propose a parallel implementation for 16 processors
2. Describe the decomposition (data vs task parallelism)
3. Identify communication requirements
4. Analyze scalability (strong vs weak scaling)

## Part D: Critical Thinking

### Discussion 1: Amdahl vs Gustafson
1. Under what circumstances is Amdahl's Law too pessimistic?
2. When might Gustafson's Law be overly optimistic?
3. Give a real-world example where each law applies

### Discussion 2: Hardware Trends
1. How has the shift from faster clocks to more cores changed parallel programming?
2. What challenges does heterogeneous computing (CPU+GPU+FPGA) present?
3. How might quantum computing affect parallel programming models?

### Discussion 3: Programming Model Selection
You're developing a new scientific application. What factors would you consider when choosing between:
- MPI
- OpenMP  
- CUDA
- A hybrid approach

## Submission Guidelines

### What to Submit
1. Answers to all questions (Part A-D)
2. For design exercises: pseudocode or detailed descriptions
3. For critical thinking: 2-3 paragraph responses

### Evaluation Criteria
- Understanding of parallel concepts (40%)
- Appropriate application of concepts to problems (30%)
- Critical analysis and reasoning (20%)
- Clarity and organization (10%)

### Tips for Success
1. Review the theory documents before attempting exercises
2. For design problems, consider both algorithmic and practical aspects
3. Justify your choices with reasoning
4. Consider edge cases and potential problems

## Additional Resources
- [Parallel Computing Tutorial (LLNL)](https://computing.llnl.gov/tutorials/parallel_comp/)
- [Introduction to Parallel Programming (Intel)](https://www.intel.com/content/www/us/en/developer/articles/technical/introduction-to-parallel-programming.html)
- [Parallel Patterns](https://patterns.eecs.berkeley.edu/)

## Next Steps
After completing these exercises, you should have a solid understanding of:
- Different types of parallelism and when to use them
- How to match programming models to architectures
- Basic performance analysis and laws
- How to approach parallel problem decomposition

Proceed to the next exercise or move to practical implementation in later modules.