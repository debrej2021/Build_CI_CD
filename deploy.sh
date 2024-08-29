#!/bin/bash

# Variables
REPO_URL="https://github.com/debrej2021/Build_CI_CD.git"
DEPLOY_DIR="/var/www/Deployed_Code"
NGINX_SERVICE="nginx"

# Step 1: Create the deployment directory if it doesn't exist
if [ ! -d "$DEPLOY_DIR" ]; then
    echo "Directory does not exist. Creating directory..."
    sudo mkdir -p "$DEPLOY_DIR"
    sudo chown ubuntu:ubuntu "$DEPLOY_DIR"   # Change to your correct username
    sudo chmod 755 "$DEPLOY_DIR"
fi

# Step 1: Clone the latest code from the GitHub repository
echo "Cloning the latest code from the repository..."
if [ -d "$DEPLOY_DIR" ]; then
    echo "Directory exists. Pulling the latest changes..."
    cd "$DEPLOY_DIR" || exit
    git pull origin main
else
    echo "Directory does not exist. Cloning repository..."
    git clone "$REPO_URL" "$DEPLOY_DIR"
    cd "$DEPLOY_DIR" || exit
fi

# Step 2: Restart Nginx service
echo "Restarting Nginx..."
sudo systemctl restart "$NGINX_SERVICE"

# Step 3: Verify Nginx restart
if systemctl is-active --quiet "$NGINX_SERVICE"; then
    echo "Nginx restarted successfully!"
else
    echo "Failed to restart Nginx. Please check the service status."
fi
