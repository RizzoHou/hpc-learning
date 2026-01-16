/*
 * MPI Hello World Example
 * 
 * This is a basic MPI program that demonstrates:
 * 1. MPI initialization and finalization
 * 2. Getting process rank and total number of processes
 * 3. Basic point-to-point communication
 * 
 * Compile: mpicc -o hello_world hello_world.c
 * Run: mpirun -np 4 ./hello_world
 */

#include <stdio.h>
#include <mpi.h>

int main(int argc, char** argv) {
    int rank, size;
    char processor_name[MPI_MAX_PROCESSOR_NAME];
    int name_len;
    
    // Initialize MPI environment
    MPI_Init(&argc, &argv);
    
    // Get the rank of the process (unique ID for each process)
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    
    // Get the total number of processes
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    
    // Get the processor name
    MPI_Get_processor_name(processor_name, &name_len);
    
    // Each process prints its information
    printf("Hello from process %d out of %d on processor %s\n", 
           rank, size, processor_name);
    
    // Simple demonstration of communication
    if (rank == 0) {
        // Process 0 sends a message to process 1
        int message = 42;
        MPI_Send(&message, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
        printf("Process 0 sent message: %d to process 1\n", message);
    } else if (rank == 1) {
        // Process 1 receives the message from process 0
        int received_message;
        MPI_Recv(&received_message, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("Process 1 received message: %d from process 0\n", received_message);
    }
    
    // Barrier synchronization - all processes wait here
    MPI_Barrier(MPI_COMM_WORLD);
    
    // Finalize MPI environment
    MPI_Finalize();
    
    return 0;
}