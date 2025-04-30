# **Self Healing Infrastructure**

## 🚀 **Project Overview**

This project demonstrates a **self-healing infrastructure** using **Prometheus**, **Alertmanager**, **Ansible**, and **Docker**. It automatically detects service failures, such as a stopped NGINX container, and recovers from them by restarting the container without manual intervention.

### 🏁 **Objective:**
- **Automatically detect service failures** (e.g., NGINX container goes down).
- **Trigger alerts** when the service fails.
- **Run an Ansible playbook** to automatically restart the service (NGINX container).
- **Achieve a fully automated recovery system** that heals itself upon failure.

### 🛠 **Tools Used:**
- **Prometheus**: For monitoring NGINX container metrics.
- **Alertmanager**: To handle and route alerts.
- **Ansible**: For automating the recovery process (restarting the container).
- **Docker**: To containerize the NGINX service.
- **Python**: To trigger Ansible playbooks via webhook.

---
## 🛠 **Setup Instructions**

### 1. **Deploy NGINX in Docker**
Deploy **NGINX** inside a Docker container and expose its metrics using **nginx-prometheus-exporter**.

```bash
docker run -d --name nginx -p 80:80 -p 9113:9113 nginx
```
### 2. **Install**
Install Docker, Ansible, Prometheus, Ansible, Python3

### 3. **Configure**
Use files from repo to configure your prometheus and alertmanager. (prometheus.yml, rules.yml, alertmanager.yml)
prometheus.yml
```yml
#prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'nginx'
    static_configs:
      - targets: ['localhost:9113']  # or use the container IP if Prometheus runs outside Docker

rule_files:
  - 'rules.yml'

alerting:
  alertmanagers:
    - static_configs:
        - targets: ['localhost:9093']
```

rules.yml
```yml
groups:
  - name: nginx.rules
    rules:
      - alert: NginxDown
        expr: up{job="nginx"} == 0
        for: 30s
        labels:
          severity: critical
        annotations:
          summary: "NGINX container is down"
          description: "NGINX Prometheus exporter has stopped responding on port 9113."
```

aletrmanager.yml
```yml
route:
  receiver: 'webhook-receiver'

receivers:
  - name: 'webhook-receiver'
    webhook_configs:
      - url: 'http://localhost:5001/alert'
```

### 4. **Start**
a) Prometheus

--- Change Ownership of prometheus folder
```bash
sudo chown -R prometheus:prometheus /opt/prometheus
```

--- Start
```bash
./prometheus --config.file=./prometheus.yml --storage.tsdb.path=./data
```
b) Ansible

--- Start
```bash
./alertmanager --config.file=./alertmanager.yml
```
