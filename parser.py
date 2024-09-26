import subprocess
import json

def get_pods_with_pvc(namespace='default'):
    """
    Function to get the list of pods and the PVCs mounted on them in a Kubernetes cluster.
    
    Args:
    - namespace: Kubernetes namespace to query pods from (default is 'default').

    Returns:
    - A list of dictionaries where each entry represents a pod with its PVC information.
    """
    try:
        # Run the kubectl command to get pods and their associated data in JSON format
        kubectl_command = f"kubectl get pods -n {namespace} -o json"
        result = subprocess.run(kubectl_command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        
        # Parse the JSON output
        pod_data = json.loads(result.stdout)
        
        pods_with_pvc = []
        
        # Loop through each pod in the JSON output
        for pod in pod_data.get('items', []):
            pod_name = pod['metadata']['name']
            pvc_list = []
            
            # Check if the pod has any volumes
            volumes = pod.get('spec', {}).get('volumes', [])
            for volume in volumes:
                # Check if the volume has a PersistentVolumeClaim entry
                if 'persistentVolumeClaim' in volume:
                    pvc_name = volume['persistentVolumeClaim']['claimName']
                    pvc_list.append(pvc_name)
            
            # Append pod data with PVCs to the list
            pods_with_pvc.append({
                'pod_name': pod_name,
                'pvc_list': pvc_list
            })
        
        # Return list of pods and their mounted PVCs
        return pods_with_pvc
    
    except subprocess.CalledProcessError as e:
        print(f"Error executing kubectl command: {e.stderr.decode('utf-8')}")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON response from kubectl command.")
        return []

# Example usage
if __name__ == "__main__":
    namespace = 'default'  # Specify the namespace if necessary
    pods_with_pvc = get_pods_with_pvc(namespace)
    print(json.dumps(pods_with_pvc, indent=4))
