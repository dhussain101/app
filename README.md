# ISA

## Getting Started
### Quickstart (download/build/run containers)

Run this command from the top level directory:

```bash
bin/start
```

### Drop into MySQL repl

```bash
bin/edit-db
```

### Nuclear option

Database is broken? Want to blow it up? Run this:

```bash
bin/wipe-all
```

```
python market/manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent=4> market/db.json
```
