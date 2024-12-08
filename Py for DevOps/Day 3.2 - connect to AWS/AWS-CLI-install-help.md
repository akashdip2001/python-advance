## install AWS-CLI

| using WSL | [not using WSL](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#getting-started-install-instructions) |
| --- | --- |

To install the AWS CLI on WSL (Windows Subsystem for Linux), follow these guided steps to avoid confusion. This example assumes you're using Ubuntu on WSL, but the steps are similar for other distributions.

---

### **Step 1: Install Prerequisites**
Ensure you have the necessary tools installed.

1. **Update your package manager:**
   ```bash
   sudo apt update
   sudo apt upgrade -y
   ```
   
<p float="left">
  <img src="https://github.com/user-attachments/assets/0b4cf318-78bc-4349-a5db-e4b95d4b2787" alt="Image 1" width="45%" />
  <img src="https://github.com/user-attachments/assets/fa013739-733d-41d2-9735-2f7048d6b2d3" alt="Image 2" width="45%" />
</p>

2. **Install required tools (`curl`, `unzip`):**
   ```bash
   sudo apt install -y curl unzip
   ```

---

### **Step 2: Download the AWS CLI Installer**

1. **Download the AWS CLI zip file:**
   ```bash
   curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
   ```

2. **Verify the file exists:**
   ```bash
   ls -l awscliv2.zip
   ```

---

### **Step 3: Extract the Installer**

1. **Unzip the downloaded file:**
   ```bash
   unzip awscliv2.zip
   ```

2. **Verify the files were extracted:**
   ```bash
   ls -l aws
   ```

---

<details>	
 <summary><b>add Git ignore</b></summary><br>

To add a `.gitignore` file to exclude certain files or directories from being tracked in Git, follow these steps:

---

### **1. Create a `.gitignore` File**
Navigate to the directory where you want to create the `.gitignore` file (in this case, inside `awscliv2`):

```bash
touch .gitignore
```

---

### **2. Edit the `.gitignore` File**
Add patterns to exclude specific files, directories, or patterns from being tracked. Open the `.gitignore` file using a text editor (e.g., `nano` or `vim`):

```bash
nano .gitignore
```

Add the following lines to exclude:
```plaintext
# Ignore the AWS CLI installation directory
aws/

# Ignore the zip file
awscliv2.zip

# Ignore other temporary files (optional)
*.log
*.tmp
```

Save and exit (`CTRL + O`, then `CTRL + X` in `nano`).
</details>

---

### **3. Verify Ignored Files**
Check which files will be ignored by running:

```bash
git status --ignored
```

This will display the files that are excluded by `.gitignore`.

---

### **Optional: Commit the `.gitignore`**
If you want to track the `.gitignore` file in your repository:

```bash
git add .gitignore
git commit -m "Add .gitignore to exclude AWS CLI installation files"
```


---

### **Step 4: Install the AWS CLI**

1. **Run the installer with `sudo`:**
   ```bash
   sudo ./aws/install
   ```

2. **Optional: Customize the installation location (if necessary):**
   Specify directories using the `-i` and `-b` parameters.
   ```bash
   sudo ./aws/install -i /usr/local/aws-cli -b /usr/local/bin
   ```

3. **Update an existing installation:**
   If you are updating the CLI, use:
   ```bash
   sudo ./aws/install --update
   ```

---

### **Step 5: Verify Installation**

1. **Check the installed version:**
   ```bash
   aws --version
   ```

   Example output:
   ```
   aws-cli/2.19.1 Python/3.11.6 Linux/5.10.16.3-microsoft-standard-WSL2 botocore/2.4.5
   ```

2. If `aws` is not recognized, add the installation directory to your `PATH` and restart your terminal:
   ```bash
   export PATH=/usr/local/bin:$PATH
   ```

---

### **Optional: Verify Integrity (for extra security)**

1. **Download the PGP signature:**
   ```bash
   curl -o awscliv2.sig https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip.sig
   ```

2. **Import the AWS CLI PGP key:**
   Create a file with the PGP key provided in the instructions and import it:
   ```bash
   gpg --import public-key-file
   ```

3. **Verify the signature:**
   ```bash
   gpg --verify awscliv2.sig awscliv2.zip
   ```

   If verification is successful, proceed with installation.

---

### **Troubleshooting**

1. **AWS Command Not Found**:
   Ensure the installation directory (`/usr/local/bin/aws`) is in your PATH.
   ```bash
   echo $PATH
   ```

2. **Installation Issues**:
   Confirm prerequisites like `unzip` and `curl` are installed and check file permissions.

3. **Need Help?**
   Refer to [AWS CLI Installation Troubleshooting](https://docs.aws.amazon.com/cli/latest/userguide/troubleshooting.html).

With these steps, you should have the AWS CLI successfully installed and ready to use on your WSL environment!
