## This .tar.gz files created from WSL-Kali Linus ( from Windows )

```python
# for linux
# # for Linux
# source_path = "/home/akash/Documents/PyProjects/python-advance/PyForDevOps"
# dest_path = "/home/akash/Documents/PyProjects/python-advance/PyForDevOps-Backup"



# for WSL
import os
import shutil
import time

def create_backup(source_path, dest_path):
    print(f"Source path: '{source_path}'")  # Debug print
    print(f"Destination path: '{dest_path}'")  # Debug print

    # Check if source path exists
    if not os.path.exists(source_path):
        print(f"Error: Source path '{source_path}' does not exist.")
        return

    # Ensure destination path exists
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    # Generate timestamped backup name
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    backup_name = os.path.join(dest_path, f"backup_{timestamp}.tar.gz")

    try:
        # Create tar.gz archive
        shutil.make_archive(backup_name.replace('.tar.gz', ''), 'gztar', source_path)
        print(f"Backup created at {backup_name}")
    except Exception as e:
        print(f"An error occurred during backup: {e}")

# for WSL
source_path = "/mnt/c/Users/akash/Desktop/Py Projects/python-advance/Py For DevOps"
dest_path = "/mnt/c/Users/akash/Desktop/Py Projects/python-advance/PyForDevOps-Backup"

# Call the backup function
create_backup(source_path, dest_path)
```

| [code for Windows](../Py%20for%20DevOps/Day%203/backup.py) |
| --- |