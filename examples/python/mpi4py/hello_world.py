"""
MPI Hello World Example in Python using mpi4py

This is a basic MPI program that demonstrates:
1. MPI initialization and finalization
2. Getting process rank and total number of processes
3. Basic point-to-point communication

Run: mpirun -np 4 python hello_world.py
"""

from mpi4py import MPI
import sys

def main():
    # Initialize MPI
    comm = MPI.COMM_WORLD
    
    # Get the rank of the process (unique ID for each process)
    rank = comm.Get_rank()
    
    # Get the total number of processes
    size = comm.Get_size()
    
    # Get the processor name
    processor_name = MPI.Get_processor_name()
    
    # Each process prints its information
    print(f"Hello from process {rank} out of {size} on processor {processor_name}")
    
    # Simple demonstration of communication
    if rank == 0:
        # Process 0 sends a message to process 1
        message = 42
        comm.send(message, dest=1, tag=0)
        print(f"Process 0 sent message: {message} to process 1")
    elif rank == 1:
        # Process 1 receives the message from process 0
        received_message = comm.recv(source=0, tag=0)
        print(f"Process 1 received message: {received_message} from process 0")
    
    # Barrier synchronization - all processes wait here
    comm.Barrier()
    
    # Collective operation example: broadcast from root to all processes
    if rank == 0:
        broadcast_data = {"data": "Hello from root!", "number": 123}
    else:
        broadcast_data = None
    
    # Broadcast the data from process 0 to all processes
    broadcast_data = comm.bcast(broadcast_data, root=0)
    
    print(f"Process {rank} received broadcast: {broadcast_data}")
    
    # Another collective operation: gather data from all processes
    local_data = rank * 10  # Each process has different data
    
    if rank == 0:
        # Process 0 will gather data from all processes
        gathered_data = comm.gather(local_data, root=0)
        print(f"Process 0 gathered data: {gathered_data}")
    else:
        # Other processes send their data
        comm.gather(local_data, root=0)
    
    # Final barrier to ensure all output is complete
    comm.Barrier()
    
    if rank == 0:
        print("\nMPI Hello World example completed successfully!")

if __name__ == "__main__":
    main()