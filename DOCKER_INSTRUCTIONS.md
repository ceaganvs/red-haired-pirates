# Docker Hub Instructions for Red-Haired Pirates Django App

## Step 1: Build the Docker Image

Open PowerShell in the project directory and run:
```bash
docker build -t red-haired-pirates .
```

## Step 2: Test the Image Locally

Run the container locally to ensure it works:
```bash
docker run -p 8000:8000 red-haired-pirates
```

Then visit http://localhost:8000 in your browser.

## Step 3: Tag the Image for Docker Hub

Replace `YOUR_DOCKERHUB_USERNAME` with your actual Docker Hub username:
```bash
docker tag red-haired-pirates YOUR_DOCKERHUB_USERNAME/red-haired-pirates:latest
```

Example:
```bash
docker tag red-haired-pirates ceaganvs/red-haired-pirates:latest
```

## Step 4: Login to Docker Hub

```bash
docker login
```

Enter your Docker Hub username and password when prompted.

## Step 5: Push to Docker Hub

```bash
docker push YOUR_DOCKERHUB_USERNAME/red-haired-pirates:latest
```

Example:
```bash
docker push ceaganvs/red-haired-pirates:latest
```

## Step 6: Test on Docker Playground

1. Go to https://labs.play-with-docker.com/
2. Click "Start" and then "+ Add New Instance"
3. Run your image:
```bash
docker run -p 8000:8000 YOUR_DOCKERHUB_USERNAME/red-haired-pirates:latest
```

4. Click the "8000" port button that appears at the top to view your application

## Verification

Your Docker Hub repository URL will be:
```
https://hub.docker.com/r/YOUR_DOCKERHUB_USERNAME/red-haired-pirates
```

## Troubleshooting

If you get permission errors on Docker Playground, try:
```bash
docker run -d -p 8000:8000 YOUR_DOCKERHUB_USERNAME/red-haired-pirates:latest
```

The `-d` flag runs it in detached mode (background).
