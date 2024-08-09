# Very important point
# Do not forget to install docker uusing python 

pip install docker

# If you are not automating the project, make sure you remember to run the below command manually on your Jenkins agent servers. 
Update Docker Socket Permissions: Ensure that the Docker socket has the appropriate permissions.

sudo chmod 666 /var/run/docker.sock

# For this project, you must build a Jenkins image to use for the CI/CD pipeline using jenkins/jenkins as the base image.
