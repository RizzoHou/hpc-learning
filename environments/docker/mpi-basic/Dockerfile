# MPI Development Environment
# Basic MPI development environment with OpenMPI and common development tools

FROM ubuntu:22.04

# Set environment variables to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    wget \
    curl \
    python3 \
    python3-pip \
    python3-dev \
    gdb \
    valgrind \
    htop \
    nano \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Install OpenMPI
RUN apt-get update && apt-get install -y \
    openmpi-bin \
    openmpi-common \
    libopenmpi-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python MPI bindings
RUN pip3 install --no-cache-dir mpi4py numpy

# Create working directory
WORKDIR /workspace

# Set MPI environment variables
ENV OMPI_ALLOW_RUN_AS_ROOT=1
ENV OMPI_ALLOW_RUN_AS_ROOT_CONFIRM=1

# Create a non-root user for better security (optional)
RUN useradd -m -s /bin/bash developer && \
    chown -R developer:developer /workspace
USER developer

# Default command
CMD ["/bin/bash"]