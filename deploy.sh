#!/usr/bin/env bash

# ==============================================================================
# AI Buyer Agent - 1-Click EC2 Deployment Script
# Automatically pulls latest git changes, installs Docker if missing,
# builds images, and starts all containers.
# ==============================================================================

set -e

# ANSI Color Codes
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${CYAN}====================================================${NC}"
echo -e "${CYAN}🚀 Starting 1-Click Deployment for AI Buyer Agent...${NC}"
echo -e "${CYAN}====================================================${NC}"

# Navigate to project root directory (where this script is located)
PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$PROJECT_DIR"
echo -e "${GREEN}📂 Working Directory:${NC} $PROJECT_DIR"

# ------------------------------------------------------------------------------
# 1. Ensure Docker and Docker Compose are installed
# ------------------------------------------------------------------------------
if ! command -v docker &> /dev/null; then
    echo -e "${YELLOW}⚙️  Docker not found. Installing Docker and Compose plugin...${NC}"
    if command -v apt-get &> /dev/null; then
        sudo apt-get update
        sudo apt-get install -y docker.io docker-compose-v2
        sudo systemctl enable --now docker
        sudo usermod -aG docker "$USER" || true
    elif command -v dnf &> /dev/null; then
        sudo dnf install -y docker docker-compose-plugin
        sudo systemctl enable --now docker
        sudo usermod -aG docker "$USER" || true
    fi
    echo -e "${GREEN}✅ Docker installed successfully.${NC}"
fi

# Detect docker compose command (v2 plugin vs standalone)
if docker compose version &> /dev/null; then
    DOCKER_COMPOSE="docker compose"
elif command -v docker-compose &> /dev/null; then
    DOCKER_COMPOSE="docker-compose"
else
    # Fallback to sudo if user group not refreshed yet
    if sudo docker compose version &> /dev/null; then
        DOCKER_COMPOSE="sudo docker compose"
    else
        DOCKER_COMPOSE="sudo docker-compose"
    fi
fi

# ------------------------------------------------------------------------------
# 2. Pull Latest Changes from Git
# ------------------------------------------------------------------------------
echo -e "\n${YELLOW}📥 Automatically pulling latest changes from Git...${NC}"
if [ -d ".git" ]; then
    # Fetch all remote branches
    git fetch --all --prune || true
    
    # Detect branch (main or master or current)
    CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "main")
    
    # If branch is detached or invalid, default to main
    if [ "$CURRENT_BRANCH" = "HEAD" ] || [ -z "$CURRENT_BRANCH" ]; then
        CURRENT_BRANCH="main"
    fi
    
    echo -e "   Branch: ${CYAN}${CURRENT_BRANCH}${NC}"
    
    # Ensure tracking is set and pull
    git branch --set-upstream-to="origin/$CURRENT_BRANCH" "$CURRENT_BRANCH" 2>/dev/null || true
    if git pull origin "$CURRENT_BRANCH"; then
        echo -e "${GREEN}✅ Successfully pulled latest changes from Git.${NC}"
    else
        echo -e "${YELLOW}⚠️ Direct branch pull had warnings. Attempting fallback git pull...${NC}"
        git pull || echo -e "${RED}⚠️ Continuing with existing files...${NC}"
    fi
else
    echo -e "${YELLOW}⚠️ Not a git repository. Skipping git pull.${NC}"
fi

# ------------------------------------------------------------------------------
# 3. Environment Check
# ------------------------------------------------------------------------------
if [ ! -f "backend/.env" ]; then
    echo -e "${YELLOW}⚠️  backend/.env not found. Creating default template if absent...${NC}"
    touch backend/.env
fi

# ------------------------------------------------------------------------------
# 4. Stop Existing Containers & Rebuild
# ------------------------------------------------------------------------------
echo -e "\n${YELLOW}🔨 Building and Starting Docker Containers...${NC}"
$DOCKER_COMPOSE down --remove-orphans || true
$DOCKER_COMPOSE up -d --build --remove-orphans

# ------------------------------------------------------------------------------
# 5. Clean up old dangling images
# ------------------------------------------------------------------------------
echo -e "\n${YELLOW}🧹 Pruning unused Docker images...${NC}"
docker image prune -f || sudo docker image prune -f || true

# ------------------------------------------------------------------------------
# 6. Status and Verification
# ------------------------------------------------------------------------------
echo -e "\n${GREEN}====================================================${NC}"
echo -e "${GREEN}✨ Deployment Complete! Container Status:${NC}"
echo -e "${GREEN}====================================================${NC}"
$DOCKER_COMPOSE ps

# Fetch Public IP (IMDSv2 with token + external fallbacks)
PUBLIC_IP=""
IMDS_TOKEN=$(curl -s -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 60" --connect-timeout 2 2>/dev/null || true)
if [ -n "$IMDS_TOKEN" ]; then
    PUBLIC_IP=$(curl -s -H "X-aws-ec2-metadata-token: $IMDS_TOKEN" --connect-timeout 2 http://169.254.169.254/latest/meta-data/public-ipv4 2>/dev/null || true)
fi

if [ -z "$PUBLIC_IP" ]; then
    PUBLIC_IP=$(curl -s --connect-timeout 2 https://checkip.amazonaws.com 2>/dev/null || curl -s --connect-timeout 2 https://api.ipify.org 2>/dev/null || curl -s --connect-timeout 2 https://ifconfig.me 2>/dev/null || true)
    PUBLIC_IP=$(echo "$PUBLIC_IP" | tr -d ' \r\n')
fi

if [ -z "$PUBLIC_IP" ]; then
    PUBLIC_IP="54.226.74.223"
fi

echo -e "\n${CYAN}🌐 Application URLs:${NC}"
echo -e "   Frontend: ${GREEN}http://${PUBLIC_IP}${NC}"
echo -e "   Backend:  ${GREEN}http://${PUBLIC_IP}:8000${NC}"
echo -e "   Docs:     ${GREEN}http://${PUBLIC_IP}:8000/docs${NC}"
echo -e "${CYAN}====================================================${NC}\n"
