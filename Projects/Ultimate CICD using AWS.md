What you will learn in this Project:

- GitOps Principals
- Monitoring Application Using Grafana and Prometheus
- Deploying Containerized Application in EKS
- Configuring Jenkins to runs build using the Best Security Practices

![](https://miro.medium.com/v2/resize:fit:875/0*qpYyrWiXHCZRtAAn)

[Github with code and Instructions](https://github.com/inderharrysingh/ultimate-devops)

# Phase 1: Initial Set UP and Deployment

**Step 1: Launch EC2 (Ubuntu 22.04):**

- Provision an EC2 instance on AWS with Ubuntu 22.04.
- Connect to the instance using SSH.

**Step 2: Clone the Code:**

- Clone your application’s code repository onto the EC2 instance:

git clone https://github.com/inderharrysingh/ultimate-devops.git

**Step 3: Install Docker and Run the App Using a Container:**

It will show an error cause you need API key

**Step 4: Get the API Key:**

- Open a web browser and navigate to TMDB (The Movie Database) website.
- Click on “Login” and create an account.
- Once logged in, go to your profile and select “Settings.”
- Click on “API” from the left-side panel.
- Create a new API key by clicking “Create” and accepting the terms and conditions.
- Provide the required basic details and click “Submit.”
- You will receive your TMDB API key.

Now recreate the Docker image with your api key:

docker build --build-arg TMDB_V3_API_KEY=<your-api-key> -t netflix .

# **Phase 2: Security**

**Installing SonarQube and Trivy**

docker run -d --name sonar -p 9000:9000 sonarqube:lts-community

1. To access: **_publicIP:9000_** (by default username & password is admin)
2. To install Trivy:

sudo apt-get install  
wget apt-transport-https gnupg lsb-release wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add - echo deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | sudo tee -a /etc/apt/sources.list.d/trivy.list   
sudo apt-get update sudo apt-get install trivy

**To scan image using trivy**

trivy image <imageid>

**Integrate SonarQube and Configure:**

- Integrate SonarQube with your CI/CD pipeline.
- Configure SonarQube to analyze code for quality and security issues.

# **Phase 3: CI/CD Setup**

1. **Install Jenkins for Automation:**

# Update package list  
sudo apt update  
  
# Install required packages  
sudo apt install -y fontconfig openjdk-17-jre  
  
# Check Java version  
java -version  
  
# Download Jenkins GPG key  
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key  
  
# Add Jenkins repository  
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null  
  
# Update package list with Jenkins repository  
sudo apt-get update  
  
# Install Jenkins  
sudo apt-get install -y jenkins  
  
# Start Jenkins service  
sudo systemctl start jenkins  
  
# Enable Jenkins service to start on boot  
sudo systemctl enable jenkins

## **Install Necessary Plugins in Jenkins:**

Goto Manage Jenkins →Plugins → Available Plugins

Install below plugins

1. Eclipse Temurin Installer (Install without restart)

2. SonarQube Scanner (Install without restart)

3. NodeJs Plugin (Install Without restart)

4. Email Extension Plugin

Goto Manage Jenkins → Tools → Install JDK(17) and NodeJs(16)→ Click on Apply and Save

## Create the token

1. Goto Jenkins Dashboard → Manage Jenkins → Credentials → Add Secret Text. It should look like this

2. After adding sonar token

3. Click on Apply and Save

**The Configure System option** is used in Jenkins to configure different server

**Global Tool Configuration** is used to configure different tools that we install using Plugins

We will install a sonar scanner in the tools.

Create a Jenkins webhook

Certainly, here are the instructions without step numbers:

Install Dependency-Check and Docker Tools in Jenkin

## **Install Dependency-Check Plugin:**

- Go to “Dashboard” in your Jenkins web interface.
- Navigate to “Manage Jenkins” → “Manage Plugins.”
- Click on the “Available” tab and search for “OWASP Dependency-Check.”
- Check the checkbox for “OWASP Dependency-Check” and click on the “Install without restart” button.

## **Configure Dependency-Check Tool:**

- After installing the Dependency-Check plugin, you need to configure the tool.
- Go to “Dashboard” → “Manage Jenkins” → “Global Tool Configuration.”
- Find the section for “OWASP Dependency-Check.”
- Add the tool’s name, e.g., “DP-Check.”
- Save your settings.

**Install Docker Tools and Docker Plugins:**

- Go to “Dashboard” in your Jenkins web interface.
- Navigate to “Manage Jenkins” → “Manage Plugins.”
- Click on the “Available” tab and search for “Docker.”
- Check the following Docker-related plugins:
- Docker
- Docker Commons
- Docker Pipeline
- Docker API
- docker-build-step
- Click on the “Install without restart” button to install these plugins.

## **Add DockerHub Credentials:**

- Go to “Dashboard” → “Manage Jenkins” → “Manage Credentials.”
- Click on “System” and then “Global credentials (unrestricted).”
- Click on “Add Credentials” on the left side.
- Choose “Secret text” as the kind of credentials.
- Enter your DockerHub credentials (Username and Password) and give the credentials an ID (e.g., “docker”).
- Click “OK” to save your DockerHub credentials.

Now, you have installed the Dependency-Check plugin, configured the tool, and added Docker-related plugins along with your DockerHub credentials in Jenkins. You can now proceed with configuring your Jenkins pipeline to include these tools and credentials in your CI/CD process.

pipeline {  
    agent any  
    tools {  
        jdk 'nodejs'  
    }  
    environment {  
        SCANNER_HOME = tool  
    }  
    stages {  
        stage() {  
            steps {  
                cleanWs()  
            }  
        }  
        stage() {  
            steps {  
                git branch: '', url: 'https://github.com/inderharrysingh/ultimate-devops.git'  
            }  
        }  
        stage() {  
            steps {  
                withSonarQubeEnv() {  
                    sh '''  
                        $SCANNER_HOME/bin/sonar-scanner -Dsonar.projectName=Netflix \  
                        -Dsonar.projectKey=Netflix  
                    '''  
                }  
            }  
        }  
        stage() {  
            steps {  
                script {  
                    waitForQualityGate abortPipeline: false, credentialsId: ''  
                }  
            }  
        }  
        stage() {  
            steps {  
                sh ''  
            }  
        }  
        stage() {  
            steps {  
                dependencyCheck additionalArguments: '--scan ./ --disableYarnAudit --disableNodeAudit',  
                                odcInstallation: 'dependencyCheckPublisher',  
                                pattern: '**/dependency-check-report.xml'  
            }  
        }  
        stage() {  
            steps {  
                sh ''  
            }  
        }  
        stage() {  
            steps {  
                script {  
                    withDockerRegistry(credentialsId: '', toolName: '') {  
                        sh '''  
                            docker build --build-arg TMDB_V3_API_KEY=<yourapikey> -t netflix .  
                            docker tag netflix inderharrysingh/netflix:latest  
                            docker push nasi101/netflix:latest  
                        '''  
                    }  
                }  
            }  
        }  
        stage() {  
            steps {  
                sh 'trivy image inderharry/netflix:latest > trivyimage.txt'  
            }  
        }  
        stage() {  
            steps {  
                sh 'docker run -d --name netflix -p 8081:80 inderharrysingh/netflix:latest'  
            }  
        }  
    }  
}  
  

# Phase 4 Monitoring

1. **Install Prometheus and Grafana:**
2. Set up Prometheus and Grafana to monitor your application.
3. **Installing Prometheus:**
4. First, create a dedicated Linux user for Prometheus and download Prometheus:

sudo useradd --system --no-create-home --shell /bin/false prometheus  
wget https://github.com/prometheus/prometheus/releases/download/v2.47.1/prometheus-2.47.1.linux-amd64.tar.gz

5. Extract Prometheus files, move them, and create directories:

tar -xvf prometheus-2.47.1.linux-amd64.tar.gz  
cd prometheus-2.47.1.linux-amd64/  
sudo mkdir -p /data /etc/prometheus  
sudo mv prometheus promtool /usr/local/bin/  
sudo mv consoles/ console_libraries/ /etc/prometheus/  
sudo mv prometheus.yml /etc/prometheus/prometheus.yml

7. Set ownership for directories:

sudo chown -R prometheus:prometheus /etc/prometheus/ /data/

8. Create a systemd unit configuration file for Prometheus:

sudo nano /etc/systemd/system/prometheus.service

9. Add the following content to the `prometheus.service` file:

[Unit]  
Description=Prometheus  
Wants=network-online.target  
After=network-online.target  
  
StartLimitIntervalSec=500  
StartLimitBurst=5  
  
[Service]  
User=prometheus  
Group=prometheus  
Type=simple  
Restart=on-failure  
RestartSec=5s  
ExecStart=/usr/local/bin/prometheus \  
  --config.file=/etc/prometheus/prometheus.yml \  
  --storage.tsdb.path=/data \  
  --web.console.templates=/etc/prometheus/consoles \  
  --web.console.libraries=/etc/prometheus/console_libraries \  
  --web.listen-address=0.0.0.0:9090 \  
  --web.enable-lifecycle  
  
[Install]  
WantedBy=multi-user.target

Here’s a brief explanation of the key parts in this `prometheus.service` file:

- `User` and `Group` specify the Linux user and group under which Prometheus will run.
- `ExecStart` is where you specify the Prometheus binary path, the location of the configuration file ( `prometheus.yml`), the storage directory, and other settings.
- `web.listen-address` configures Prometheus to listen on all network interfaces on port 9090.
- `web.enable-lifecycle` allows for management of Prometheus through API calls.

10. Enable and start Prometheus:

sudo systemctl enable prometheus 

11. Verify Prometheus’s status:

sudo systemctl start prometheus

12. You can access Prometheus in a web browser using your server’s IP and port 9090

## **Installing Node Exporter:**

1. Create a system user for Node Exporter and download Node Exporter:

sudo useradd --system --no-create-home --shell /bin/false node_exporter  
wget https://github.com/prometheus/node_exporter/releases/download/v1.6.1/node_exporter-1.6.1.linux-amd64.tar.gz

2. Extract Node Exporter files, move the binary, and clean up:

tar -xvf node_exporter-1.6.1.linux-amd64.tar.gz  
sudo mv node_exporter-1.6.1.linux-amd64/node_exporter /usr/local/bin/  
rm -rf node_exporter*

3. Create a systemd unit configuration file for Node Exporter:

sudo nano /etc/systemd/system/node_exporter.service

4. Add the following content to the `node_exporter.service` file:

[Unit]  
Description=Node Exporter  
Wants=network-online.target  
After=network-online.target  
  
StartLimitIntervalSec=500  
StartLimitBurst=5  
  
[Service]  
User=node_exporter  
Group=node_exporter  
Type=simple  
Restart=on-failure  
RestartSec=5s  
ExecStart=/usr/local/bin/node_exporter --collector.logind  
  
[Install]  
WantedBy=multi-user.target

5. Replace `--collector.logind` with any additional flags as needed.

6. Enable and start Node Exporter:

sudo systemctl enable node_exporter

Verify the Node Exporter’s status:

sudo systemctl start node_exporter

1. You can access Node Exporter metrics in Prometheus.
2. **Configure Prometheus Plugin Integration:**
3. Integrate Jenkins with Prometheus to monitor the CI/CD pipeline.
4. **Prometheus Configuration:**
5. To configure Prometheus to scrape metrics from Node Exporter and Jenkins, you need to modify the `prometheus.yml` file. Here is an example `prometheus.yml` configuration for your setup:
6. Make sure to replace `<your-jenkins-ip>` and `<your-jenkins-port>` with the appropriate values for your Jenkins setup.
7. Check the validity of the configuration file:

promtool check config /etc/prometheus/prometheus.yml

1. Reload the Prometheus configuration without restarting:

curl -X POST http://localhost:9090/-/reload

2. You can access Prometheus targets at `http://<your-prometheus-ip>:9090/targets`

# Grafana

**Install Grafana on Ubuntu 22.04 and Set it up to Work with Prometheus**

**Step 1: Install Dependencies:**

First, ensure that all necessary dependencies are installed:

sudo apt-get update  
sudo apt-get install -y apt-transport-https software-properties-common

**Step 2: Add the GPG Key:**

Add the GPG key for Grafana:

wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -

**Step 3: Add Grafana Repository:**

Add the repository for Grafana stable releases:

echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list

**Step 4: Update and Install Grafana:**

Update the package list and install Grafana:

sudo apt-get update   
sudo apt-get -y install grafana

**Step 5: Enable and Start Grafana Service:**

To automatically start Grafana after a reboot, enable the service:

sudo systemctl enable grafana-server

Then, start Grafana:

sudo systemctl start grafana-server

**Step 6: Check Grafana Status:**

Verify the status of the Grafana service to ensure it’s running correctly:

sudo systemctl status grafana-server

**Step 7: Access Grafana Web Interface:**

Open a web browser and navigate to Grafana using your server’s IP address. The default port for Grafana is 3000. For example:

You’ll be prompted to log in to Grafana. The default username is “admin,” and the default password is also “admin.”

**Step 8: Change the Default Password:**

When you log in for the first time, Grafana will prompt you to change the default password for security reasons. Follow the prompts to set a new password.

**Step 9: Add Prometheus Data Source:**

To visualize metrics, you need to add a data source. Follow these steps:

- Click on the gear icon (⚙️) in the left sidebar to open the “Configuration” menu.
- Select “Data Sources.”
- Click on the “Add data source” button.
- Choose “Prometheus” as the data source type.
- In the “HTTP” section:
- Set the “URL” to `http://localhost:9090` (assuming Prometheus is running on the same server).
- Click the “Save & Test” button to ensure the data source is working.

**Step 10: Import a Dashboard:**

To make it easier to view metrics, you can import a pre-configured dashboard. Follow these steps:

- Click on the “+” (plus) icon in the left sidebar to open the “Create” menu.
- Select “Dashboard.”
- Click on the “Import” dashboard option.
- Enter the dashboard code you want to import (e.g., code 1860).
- Click the “Load” button.
- Select the data source you added (Prometheus) from the dropdown.
- Click on the “Import” button.

You should now have a Grafana dashboard set up to visualize metrics from Prometheus.

Grafana is a powerful tool for creating visualizations and dashboards, and you can further customize it to suit your specific monitoring needs.

That’s it! You’ve successfully installed and set up Grafana to work with Prometheus for monitoring and visualization.

# Phase 6: Kubernetes

In this phase, you’ll set up a Kubernetes cluster with node groups. This will provide a scalable environment to deploy and manage your applications.

Prometheus is a powerful monitoring and alerting toolkit, and you’ll use it to monitor your Kubernetes cluster. Additionally, you’ll install the node exporter using Helm to collect metrics from your cluster nodes.

To begin monitoring your Kubernetes cluster, you’ll install the Prometheus Node Exporter. This component allows you to collect system-level metrics from your cluster nodes. Here are the steps to install the Node Exporter using Helm:

1. Add the Prometheus Community Helm repository:

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

2. Create a Kubernetes namespace for the Node Exporter:

kubectl create namespace prometheus-node-exporter

3. Install the Node Exporter using Helm:

helm install prometheus-node-exporter prometheus-community/prometheus-node-exporter - namespace prometheus-node-exporter

4. Add a Job to Scrape Metrics on nodeip:9001/metrics in prometheus.yml:

Update your Prometheus configuration (prometheus.yml) to add a new job for scraping metrics from nodeip:9001/metrics. You can do this by adding the following configuration to your prometheus.yml file:

  - job_name: 'Netflix'  
    metrics_path: '/metrics'  
    static_configs:  
      - targets: ['node1Ip:9100']

Replace ‘your-job-name’ with a descriptive name for your job. The static_configs section specifies the targets to scrape metrics from, and in this case, it’s set to nodeip:9001.

Don’t forget to reload or restart Prometheus to apply these changes to your configuration.

To deploy an application with ArgoCD, you can follow these steps, which I’ll outline in Markdown format:

1. **Install ArgoCD:**
2. You can install ArgoCD on your Kubernetes cluster by following the instructions provided in the [EKS Workshop](https://archive.eksworkshop.com/intermediate/290_argocd/install/) documentation.
3. **Set Your GitHub Repository as a Source:**

After installing ArgoCD, you need to set up your GitHub repository as a source for your application deployment. This typically involves configuring the connection to your repository and defining the source for your ArgoCD application. The specific steps will depend on your setup and requirements.

**4. Create an ArgoCD Application:**

- `name`: Set the name for your application.
- `destination`: Define the destination where your application should be deployed.
- `project`: Specify the project the application belongs to.
- `source`: Set the source of your application, including the GitHub repository URL, revision, and the path to the application within the repository.
- `syncPolicy`: Configure the sync policy, including automatic syncing, pruning, and self-healing.

1. **Access your Application**

**Phase 7: Cleanup**

Cleanup AWS EC2 Instances:

Terminate AWS EC2 instances that are no longer needed.