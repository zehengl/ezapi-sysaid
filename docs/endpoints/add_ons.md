```python
from sysaid import SysAid

host = "..."
username = "..."
password = "..."

s = SysAid(host, username, password)
```

## Get a list of all available add-ons in SysAid

```python
s.get_application_add_ons()
```
