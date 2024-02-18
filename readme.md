---
runme:
  id: 01HPKAS45H4FWYQ077G44PNHSG
  version: v3
---

```sh {"id":"01HPKAS7W2J5SS1AXSGRRESXTM"}
#Install Packages
pip install -r requirements.txt
```

```sh {"id":"01HPXDFP9C550Q53028FRB1D30"}
#Install Dev Packges
pip install -r requirements-dev.txt 
```

```sh {"id":"01HPTSRKZM3MMW14XTCQZ6HHDA"}
#Django makemigrations
py manage.py makemigrations
```

```sh {"id":"01HPTSSX4RVPNGZ1TA5KN9PGH1"}
#Django migrate
py manage.py migrate
```

```sh {"id":"01HPXD8D650K482YBK66RKFHQ4"}
#Flake8 Code Style
flake8
```