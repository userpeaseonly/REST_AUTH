# Project Setup and Run Guide

This project is containerized using Docker, making it easy to set up and run on any operating system.

---

## Quick Start

Run the appropriate command for your operating system to set up and run the project in under 2 minutes:

### For Linux
```bash
sudo apt update && sudo apt install -y git docker.io docker-compose-plugin && git clone <your-repo-url> && cd <repository-folder> && sudo docker-compose -f docker-compose.local.yml up --build
```
### For MacOS
```bash
brew install git && brew install --cask docker && open -a Docker && git clone <your-repo-url> && cd <repository-folder> && docker-compose -f docker-compose.local.yml up --build
```
### For Windows
```bash
winget install -e --id Git.Git && winget install -e --id Docker.DockerDesktop && git clone <your-repo-url> ; cd <repository-folder> ; docker-compose -f docker-compose.local.yml up --build
```
