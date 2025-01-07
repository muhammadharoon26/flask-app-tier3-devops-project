This project demonstrates containerization, CI/CD, and cloud deployment, showcasing strong Tier 3 DevOps skills while using free resources.

Here’s a comprehensive, step-by-step tutorial for a **Tier 3 DevOps project**, designed for learning and showcasing your skills. We'll focus on deploying a containerized web application with Continuous Integration (CI) and Continuous Deployment (CD) pipelines using only free tools and platforms.

---

### **Project Overview**
We’ll:
1. Build and containerize a simple web application.
2. Set up version control with GitHub.
3. Implement CI/CD pipelines using GitHub Actions.
4. Deploy the application on a free platform like **Railway.app** or **Render.com**.

---

### **Step 1: Prerequisites**
#### Install the following tools:
- **Git**: Version control system ([Download Git](https://git-scm.com/)).
- **Docker**: Containerization platform ([Download Docker](https://www.docker.com/products/docker-desktop/)).
- **VS Code**: Text editor for coding ([Download VS Code](https://code.visualstudio.com/)).
- **Railway CLI** (if using Railway): [Railway CLI Installation Guide](https://docs.railway.app/develop/cli).

#### Create free accounts:
- **GitHub**: For version control and CI/CD ([Sign up](https://github.com/)).
- **Railway.app** or **Render.com**: For free app hosting ([Railway](https://railway.app/) | [Render](https://render.com/)).

---

### **Step 2: Create a Simple Web Application**
We’ll create a **Python Flask** app.

1. **Initialize a Project:**
   ```bash
   mkdir tier3-devops && cd tier3-devops
   git init
   ```

2. **Install Flask:**
   ```bash
   mkdir app && cd app
   python3 -m venv venv
   source venv/bin/activate
   pip install flask
   ```

3. **Write Flask App (`app.py`):**
   ```python
   from flask import Flask
   
   app = Flask(__name__)

   @app.route('/')
   def home():
       return "Hello, DevOps!"

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)
   ```

4. **Add a Requirements File (`requirements.txt`):**
   ```plaintext
   flask
   ```

5. **Test Locally:**
   ```bash
   python app.py
   ```

---

### **Step 3: Dockerize the Application**
1. **Create a `Dockerfile`:**
   ```dockerfile
   # Use a lightweight Python image
   FROM python:3.9-slim

   # Set the working directory
   WORKDIR /app

   # Copy files
   COPY . /app

   # Install dependencies
   RUN pip install -r requirements.txt

   # Expose port 5000
   EXPOSE 5000

   # Start the app
   CMD ["python", "app.py"]
   ```

2. **Build and Run the Docker Image Locally:**
   ```bash
   docker build -t tier3-devops .
   docker run -p 5000:5000 tier3-devops
   ```

---

### **Step 4: Push to GitHub**
1. **Create a Repository:**
   - Go to GitHub, create a new repo (e.g., `tier3-devops`).

2. **Push Code:**
   ```bash
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/your-username/tier3-devops.git
   git push -u origin main
   ```

---

### **Step 5: Set Up CI/CD with GitHub Actions**
1. **Create `.github/workflows/deploy.yml`:**
   ```yaml
   name: CI/CD Pipeline

   on:
     push:
       branches:
         - main

   jobs:
     build:
       runs-on: ubuntu-latest

       steps:
       - name: Checkout Code
         uses: actions/checkout@v3

       - name: Set up Docker Buildx
         uses: docker/setup-buildx-action@v2

       - name: Log in to DockerHub
         uses: docker/login-action@v2
         with:
           username: ${{ secrets.DOCKER_USERNAME }}
           password: ${{ secrets.DOCKER_PASSWORD }}

       - name: Build and Push Docker Image
         uses: docker/build-push-action@v4
         with:
           context: .
           tags: your-dockerhub-username/tier3-devops:latest

     deploy:
       runs-on: ubuntu-latest
       needs: build

       steps:
       - name: Deploy to Railway
         run: railway up
   ```

2. **Add GitHub Secrets:**
   - Add `DOCKER_USERNAME` and `DOCKER_PASSWORD` in **GitHub → Settings → Secrets and Variables**.

---

### **Step 6: Deploy on Railway.app**
1. **Link Repo to Railway:**
   - Go to [Railway](https://railway.app/), create a new project, and link your GitHub repo.

2. **Set Up Deployment:**
   - Railway will detect the Dockerfile and deploy your app.

3. **Test Your App:**
   - You’ll get a live URL (e.g., `https://your-app.up.railway.app`).

---

### **Step 7: Monitor and Improve**
1. **Set Up Logs:**
   - Use Railway’s built-in logs to monitor your app.

2. **Extend the App:**
   - Add more routes, integrate a database, or improve the UI.

3. **Optimize Pipelines:**
   - Add test steps in your CI/CD pipelines.

---

### **Free Tier Limits**
- **Railway**: Free tier includes 500 hours and 1GB RAM/month.
- **GitHub Actions**: Free tier includes 2,000 CI/CD minutes/month.

This project demonstrates containerization, CI/CD, and cloud deployment, showcasing strong Tier 3 DevOps skills while using free resources.