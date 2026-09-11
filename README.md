# Selvi Hospital – Sinapse v16

## Deployment & Installation Guide

# 1. System Requirements

The following environment is required for deploying Selvi Hospital Sinapse v16.

### Operating System

* Ubuntu 24.04 LTS
* WSL2 when deploying through Windows

### Required Software

* Git
* Podman
* Podman Compose

### Recommended Hardware

* Minimum 8 GB RAM
* 4 CPU cores or more
* Minimum 30 GB available storage
* SSD recommended

Additional resources may be required depending on the number of users, patient records, attachments, reports, and background jobs.

---

# 2. Prerequisites

Before starting the deployment, verify that the required software is installed.

## 2.1 Check Ubuntu

```bash
lsb_release -a
```

or:

```bash
cat /etc/os-release
```

The deployment environment should use Ubuntu 24.04 LTS.

---

## 2.2 Check Git

```bash
git --version
```

If Git is not installed:

```bash
sudo apt update
sudo apt install git -y
```

---

## 2.3 Check Podman

```bash
podman --version
```

If Podman is not installed:

```bash
sudo apt update
sudo apt install podman -y
```

Verify the installation:

```bash
podman info
```

---

## 2.4 Check Podman Compose

```bash
podman compose version
```

Podman Compose must be available before starting the application.

---

# 3. Get the Selvi Hospital Source Code

Clone the Selvi Hospital Sinapse v16 repository:

```bash
git clone https://github.com/bfx-labs/sinapse-v16
```

Move into the project directory:

```bash
cd sinapse-v16
```

Check the repository:

```bash
git status
```

Check the current branch:

```bash
git branch
```

To retrieve the latest code from the configured branch:

```bash
git pull
```

---

# 4. Selvi Hospital Container Image

Selvi Hospital Sinapse v16 uses a **custom container image maintained specifically for the Selvi Hospital deployment**.

The approved image is:

```text
ghcr.io/bfx-labs/selvi-v16:v16.1-selvi-9031cd994b92cde660a37571f2bbbf6d834702ec
```

## 4.1 Pull the Selvi Hospital Image

Using Podman:

```bash
podman pull ghcr.io/bfx-labs/selvi-v16:v16.1-selvi-9031cd994b92cde660a37571f2bbbf6d834702ec
```

## 4.2 Verify the Image

After pulling the image:

```bash
podman images
```

The image should appear similar to:

```text
REPOSITORY                 TAG
ghcr.io/bfx-labs/selvi-v16 v16.1-selvi-9031cd994b92cde660a37571f2bbbf6d834702ec
```

You can also inspect the image:

```bash
podman inspect ghcr.io/bfx-labs/selvi-v16:v16.1-selvi-9031cd994b92cde660a37571f2bbbf6d834702ec
```

---

# 5. Project Directory

After cloning the repository:

```bash
cd sinapse-v16
```

Check the project files:

```bash
ls -lah
```

Check the directory structure:

```bash
find . -maxdepth 2 -type d
```

The project contains the deployment configuration required to run the Selvi Hospital Sinapse environment.

---

# 6. Container Configuration

Before starting the application, verify the compose configuration.

Check for the compose file:

```bash
ls -lah
```

Common configuration files include:

```text
compose.yaml
docker-compose.yml
```

Open the compose configuration:

```bash
cat compose.yaml
```

If the project uses `docker-compose.yml`:

```bash
cat docker-compose.yml
```

The configuration should reference the Selvi Hospital image:

```text
ghcr.io/bfx-labs/selvi-v16:v16.1-selvi-9031cd994b92cde660a37571f2bbbf6d834702ec
```

---

# 7. Start Selvi Hospital Sinapse

From the project directory:

```bash
cd sinapse-v16
```

Start the services:

```bash
podman compose up -d
```

If the images have not already been pulled, Podman Compose may pull the required images according to the compose configuration.

For a controlled deployment, it is recommended to explicitly pull the required Selvi image first:

```bash
podman pull ghcr.io/bfx-labs/selvi-v16:v16.1-selvi-9031cd994b92cde660a37571f2bbbf6d834702ec
```

Then start:

```bash
podman compose up -d
```

---

# 8. Database Migration

After deploying a new application version or restoring an existing environment, run the migration.

Inside the backend container:

```bash
cd /home/frappe/frappe-bench
```

Run:

```bash
bench --site sinapse.localhost migrate
```

Migration may perform:

* Database schema updates
* Application patches
* DocType updates
* Customization updates
* Fixture synchronization
* Application metadata updates

Check the terminal output carefully and ensure there are no migration errors.

---

# 9. Build Application Assets

After application updates or changes to frontend files, rebuild the assets:

```bash
bench build
```

After the build completes successfully, clear the cache:

```bash
bench --site sinapse.localhost clear-cache
```

Clear website cache:

```bash
bench --site sinapse.localhost clear-website-cache
```

---

# 10. Restart the Application

Exit the backend container:

```bash
exit
```

Restart the services:

```bash
podman compose restart
```

Check the containers:

```bash
podman ps
```

---

# 11. Access Selvi Hospital Sinapse

Once all required containers are running, access the application using the configured URL.

For local deployment:

```text
http://localhost:<PORT>
```

For production deployment:

```text
https://<SELVI-HOSPITAL-DOMAIN>
```

The production domain and port should match the deployment configuration.

---

# 12. Database Backup

Before performing updates, migrations, or major configuration changes, create a database backup.

Enter the backend container:

```bash
podman exec -it <backend-container> bash
```

Navigate to:

```bash
cd /home/frappe/frappe-bench
```

Run:

```bash
bench --site sinapse.localhost backup
```

Check the backup directory:

```bash
ls -lah sites/sinapse.localhost/private/backups/
```

Backups should also be copied to storage outside the application server.

---

# 13. Application Update Procedure

When a new Selvi Hospital Sinapse version is released, follow this sequence.

## Step 1 – Backup

Create a database backup:

```bash
bench --site sinapse.localhost backup
```

---

## Step 2 – Update Source Code

On the host machine:

```bash
cd sinapse-v16
```

Pull the latest code:

```bash
git pull
```

Check the changes:

```bash
git status
```

---

## Step 3 – Pull the Updated Container Image

Pull the image specified for the new release.

For the currently documented version:

```bash
podman pull ghcr.io/bfx-labs/selvi-v16:v16.1-selvi-9031cd994b92cde660a37571f2bbbf6d834702ec
```

---

## Step 4 – Recreate Services

```bash
podman compose up -d
```

Verify:

```bash
podman ps
```

---

## Step 5 – Run Migration

Enter the backend:

```bash
podman exec -it <backend-container> bash
```

Then:

```bash
cd /home/frappe/frappe-bench
```

Run:

```bash
bench --site sinapse.localhost migrate
```

---

## Step 6 – Build Assets

```bash
bench build
```

Clear cache:

```bash
bench --site sinapse.localhost clear-cache
```

---

## Step 7 – Restart

Exit:

```bash
exit
```

Restart:

```bash
podman compose restart
```

---

## Step 8 – Verify

Check:

```bash
podman ps
```

# 14. Troubleshooting

## Sinapse is not opening

Check:

```bash
podman ps
```

If a container is stopped:

```bash
podman ps -a
```

Check its logs:

```bash
podman logs <container-name>
```

Restart:

```bash
podman compose restart
```

---

## Port conflict

Check ports:

```bash
sudo ss -ltnp
```

Check Podman:

```bash
podman ps
```

Update the port configuration if necessary and recreate the containers:

```bash
podman compose down
podman compose up -d
```

---

## Container keeps restarting

Check:

```bash
podman ps -a
```

Then:

```bash
podman logs <container-name>
```

Check for:

* Database connection errors
* Redis connection errors
* Missing configuration
* Permission errors
* Python exceptions
* Port conflicts
* Missing files

---

## Application changes are not visible

Run:

```bash
bench --site sinapse.localhost migrate
```

Then:

```bash
bench build
```

Clear cache:

```bash
bench --site sinapse.localhost clear-cache
```

Restart:

```bash
podman compose restart
```

Perform a hard refresh in the browser.

---
