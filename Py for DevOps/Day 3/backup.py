import os
import shutil
import time

def create_backup(source_path, dest_path):
    # Check if source path exists
    if not os.path.exists(source_path):
        print(f"Error: Source path '{source_path}' does not exist.")
        return

    # Ensure destination path exists
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    # Generate timestamped backup name
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    backup_name = os.path.join(dest_path, f"backup_{timestamp}")

    try:
        # Create backup archive
        shutil.make_archive(backup_name, 'zip', source_path)
        print(f"Backup created at {backup_name}.zip")
    except Exception as e:
        print(f"An error occurred during backup: {e}")

# Define source and destination paths
source_path = r"C:\Users\akash\Desktop\Py Projects\python-advance\Py for DevOps"
dest_path = r"C:\Users\akash\Desktop\Py Projects\python-advance\Py for DevOps-Backup"

# Call the backup function
create_backup(source_path, dest_path)
