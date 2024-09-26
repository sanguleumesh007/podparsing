# Kubernetes Pod PVC Parser

This repository contains a Python script that parses the output of `kubectl get pods` to list the Persistent Volume Claims (PVCs) mounted on each pod in a Kubernetes cluster.

## Features

- Retrieves pod information from a specific namespace using `kubectl`.
- Lists PVCs mounted to each pod.
- Converts the `kubectl` output to JSON and parses the necessary information.
- Can be used to troubleshoot or monitor PVC usage across pods in a namespace.

## Requirements

- Python 3.x
- Kubernetes cluster configured with `kubectl`
- Access to the desired Kubernetes namespace

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/kubernetes-pvc-parser.git
   cd kubernetes-pvc-parser
