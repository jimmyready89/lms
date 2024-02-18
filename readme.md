---
runme:
  id: 01HPKAS45H4FWYQ077G44PNHSG
  version: v3
---

```sh {"id":"01HPKAS7W2J5SS1AXSGRRESXTM"}
#Install Packages
pip install -r requirements.txt
```

```sh {"id":"01HPTSRKZM3MMW14XTCQZ6HHDA"}
#Django makemigrations
py manage.py makemigrations
```

```sh {"id":"01HPTSSX4RVPNGZ1TA5KN9PGH1"}
#Django migrate
py manage.py migrate
```