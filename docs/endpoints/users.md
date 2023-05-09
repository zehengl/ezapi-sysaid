```python
from sysaid import SysAid

host = "..."
username = "..."
password = "..."

s = SysAid(host, username, password)
```

## Get list of users in SysAid

```python
s.get_users_list()
s.get_users_list(offset=1000, limit=200)
```

## Get information on the specified user

```python
s.get_user(1234)
```

## Get list of users in SysAid, according to a search criteria

```python
s.search_users("John Doe")
s.search_users("John Doe", limit=10)
```

## Get user permissions

```python
s.get_user_permissions(1234)
```
