### Extracting ZIP Archives on Windows and Linux

Below are the commands for extracting a `.zip` file on both **Windows** and **Linux**.

---

### **1. Windows**
#### Using File Explorer (GUI):
1. Right-click the `.zip` file.
2. Select **Extract All...**.
3. Choose the destination folder and click **Extract**.

#### Using Command Prompt (CLI):
Windows has the `tar` command starting with Windows 10. To extract a `.zip` file:
```cmd
tar -xf backup.zip -C <destination-folder>
```
- **Example**:
  ```cmd
  tar -xf C:\Users\akash\Desktop\Py Projects\python-advance\Py for DevOps-Backup\backup_20241208-153045.zip -C C:\Users\akash\Desktop\ExtractedFolder
  ```

Alternatively, use **PowerShell**:
```powershell
Expand-Archive -Path "C:\path\to\backup.zip" -DestinationPath "C:\path\to\destination"
```
- **Example**:
  ```powershell
  Expand-Archive -Path "C:\Users\akash\Desktop\Py Projects\python-advance\Py for DevOps-Backup\backup_20241208-153045.zip" -DestinationPath "C:\Users\akash\Desktop\ExtractedFolder"
  ```

---

### **2. Linux**
#### Using Terminal:
The `unzip` command is commonly used. To extract:
```bash
unzip backup.zip -d <destination-folder>
```
- **Example**:
  ```bash
  unzip backup_20241208-153045.zip -d ~/ExtractedFolder
  ```

#### Using `tar` (If Installed):
Linux also supports the `tar` command for zip files:
```bash
tar -xf backup.zip -C <destination-folder>
```
- **Example**:
  ```bash
  tar -xf backup_20241208-153045.zip -C ~/ExtractedFolder
  ```

#### Install Tools if Missing:
If the commands aren’t available:
- Install `unzip`:
  ```bash
  sudo apt update && sudo apt install unzip -y  # For Debian/Ubuntu
  sudo yum install unzip -y                    # For RedHat/CentOS
  ```
- Install `tar` (most distributions include this by default):
  ```bash
  sudo apt update && sudo apt install tar -y
  ```

---

### Summary Table

| **OS**           | **Command**                                   | **Example**                                                                                                                                                     |
|-------------------|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows CMD       | `tar -xf <file.zip> -C <dest-folder>`         | `tar -xf C:\path\to\backup.zip -C C:\path\to\destination`                                                                                                       |
| Windows PowerShell| `Expand-Archive -Path <file.zip> -DestinationPath <dest>` | `Expand-Archive -Path "C:\path\to\backup.zip" -DestinationPath "C:\path\to\destination"`                                                                         |
| Linux `unzip`     | `unzip <file.zip> -d <dest-folder>`           | `unzip backup.zip -d ~/destination`                                                                                                                             |
| Linux `tar`       | `tar -xf <file.zip> -C <dest-folder>`         | `tar -xf backup.zip -C ~/destination`                                                                                                                           |

Let me know if you need further clarification! 😊