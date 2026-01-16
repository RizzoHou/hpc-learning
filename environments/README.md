# Development Environments

This directory contains configurations and scripts for setting up HPC development environments on different platforms.

## Directory Structure

### 📁 **docker/** - Containerized Environments
- **mpi-basic/** - Basic MPI development environment
- **openmp-basic/** - OpenMP development environment  
- **hybrid-mpi-openmp/** - Hybrid MPI+OpenMP environment

### 📁 **mac-m4/** - MacBook M4 (ARM) Setup
- Scripts and configurations optimized for Apple Silicon
- ARM-specific compilation flags and optimizations
- Local development setup without containers

### 📁 **ssh-hpc/** - University HPC Access
- SSH connection guides and scripts
- File transfer utilities
- Job submission templates

## Usage

### Docker Environments
```bash
# Build and run MPI environment
cd environments/docker/mpi-basic
docker build -t mpi-dev .
docker run -it --rm mpi-dev

# For GPU support (if available)
cd environments/docker/cuda-mpi
docker build -t cuda-mpi-dev .
docker run --gpus all -it --rm cuda-mpi-dev
```

### MacBook M4 Setup
```bash
# Install MPI and OpenMP
cd environments/mac-m4
./install-mpi.sh
./install-openmp.sh

# Test installation
./test-environment.sh
```

### SSH HPC Access
```bash
# Connect to university HPC
cd environments/ssh-hpc
./connect-hpc.sh

# Transfer files
./transfer-files.sh local_file.txt hpc-cluster:~/hpc-learning/
```

## Environment Requirements

### Docker
- Docker Desktop for Mac/Windows/Linux
- Minimum 4GB RAM allocated to Docker
- For GPU: NVIDIA Docker runtime (Linux) or Docker Desktop with GPU support

### MacBook M4
- macOS 13.0 or later
- Homebrew package manager
- Xcode Command Line Tools

### SSH HPC
- SSH client installed
- University HPC account and credentials
- Basic familiarity with terminal/command line

## Best Practices

1. **Start with Docker**: Use containerized environments for consistency
2. **Test Locally First**: Develop and test on local machine before moving to HPC
3. **Version Control**: Keep environment configurations in git
4. **Document Dependencies**: Update README files when adding new dependencies
5. **Security**: Never commit passwords or sensitive credentials

## Troubleshooting

Common issues and solutions are documented in `docs/setup/troubleshooting.md`.