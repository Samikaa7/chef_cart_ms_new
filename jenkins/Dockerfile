FROM jenkins/jenkins:lts

USER root

# Install Docker CLI and Docker Compose plugin inside Jenkins container
RUN apt-get update -y && \
    apt-get install -y apt-transport-https ca-certificates curl gnupg2 lsb-release && \
    mkdir -p /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" \
        > /etc/apt/sources.list.d/docker.list && \
    apt-get update -y && \
    apt-get install -y docker-ce-cli docker-compose-plugin && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Add jenkins to root group (so it can access docker.sock)
RUN usermod -aG root jenkins

USER jenkins
