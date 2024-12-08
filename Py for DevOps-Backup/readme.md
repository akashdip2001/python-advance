### Name: backup_20241208-131451.zip
```python
import time
```
```python
timestamp = time.strftime("%Y%m%d-%H%M%S")
```
---

### Name: backup_2024-12-08--13-33-25.zip
```python
import time
```
```python
timestamp = time.strftime("%Y-%m-%d--%H-%M-%S")
```
---

### Name: backup_2024-12-08.zip

#### its not recommended because of the `.zip file` not include `Time` in the file name ... so the the file `replaced`, if you backup many times in `same day`.

```python
import datetime
```
```python
timestamp = datetime.date.today()
```

#### or you can use 
```python
timestamp = datetime.date.today().strftime("%Y%m%d-%H%M%S")
```

# [code](../Py%20for%20DevOps/Day%203/)