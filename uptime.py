# The script will connect to the Docker Engine, retrieve the list of running containers, and print their status and uptime.
import docker
from datetime import datetime

# Connect to Docker
client = docker.from_env()

# Get a list of all containers (running and stopped)
containers = client.containers.list(all=True)

# Print the status and uptime of each container
for container in containers:
    # Get container status
    status = container.status
    
    # Get container start time and calculate uptime
    start_time_str = container.attrs['State']['StartedAt']
    start_time = datetime.strptime(start_time_str.split('.')[0], "%Y-%m-%dT%H:%M:%S")
    uptime = datetime.utcnow() - start_time
    
    # Display container name, status, and uptime
    print(f"Container: {container.name}")
    print(f"Status: {status.capitalize()}")
    
    # If container is running, show uptime
    if status == "running":
        print(f"Uptime: {uptime}")
    else:
        print("Uptime: N/A (Container is not running)")
    
    print("-" * 40)
