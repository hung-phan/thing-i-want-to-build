# TinyURL

## Requirement
```bash
$ pip install -r requirements.txt
```

## Migration
```bash
$ yoyo apply --database postgresql://tinyurl:tinyurl@localhost/tinyurl ./migrations # apply migration
$ yoyo rollback --database postgresql://tinyurl:tinyurl@localhost/tinyurl ./migrations # apply migration
```

## Development
```bash
$ docker-compose up
$ python main.py
```
