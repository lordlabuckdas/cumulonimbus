# team cumulonimbus

* [frontend](frontend)
* [backend](backend)
* [dcol](dcol)

**sample db item:**

```json
{
  "mac_address":"00:0d:83:b1:c0:8e",
  "os":"linux",
  "domain":"abc.com",
  "workgroup":"abc",
  "last_seen":"2021/06/23 12:45:23",
  "ip_address":"192.168.1.5",
  "hostname":"ubuntu-dell-xps13"
}
```

can be changed acc to convenience

## setup

### requirements

* docker
* docker-compose
* nmap
* python (w/ pip)

### backend server and db

```shell
$ docker-compose up
```

### dcol dev env

```shell
$ cd backend
$ pip install -r requirements.txt
$ cd dcol
$ python main.py --help
```

### populate db

```shell
$ python tests/test_populate_db.py
```

### test frontend2api connection

```shell
$ python -m http.server 3000 --directory tests/
```

then, open `http://localhost:3000/test_backend_api.html`

## standards

* always prefer modules over executing sys commands
* code in a pythonic way
* snake_case and OOPs supremacy
