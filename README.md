Geoapp
============

### Application

Run application
```
sh run_app.sh
```
This script will:
- Initialize postgresql database
- Populate database
- Activate PostGis extension
- Activate app environment
- Install all requirements
- Serve flask application on http://0.0.0.0:8000

*Note that **Docker** and **Python 3.8** should be installed for the script to work

---

### Requests

To access the routes with authorization (with default user/passsword) using *curl*:

```shell
curl -u test_username:test_password -i -X GET http://0.0.0.0:8000/geoapp/zipcode/[zipcode]
```

(Can also be done choosing *BasicAuth* in Postman for example and setting username and password)

A successful response looks like:

```json
[
  {
    "AGE": "<=24",
    "F": "800,580.92€",
    "M": "498,425.54€"
  },
  {
    "AGE": "25-34",
    "F": "3,099,364.30€",
    "M": "1,881,514.79€"
  },
  {
    "AGE": "35-44",
    "F": "3,851,275.79€",
    "M": "2,636,725.90€"
  },
  {
    "AGE": "45-54",
    "F": "4,232,049.79€",
    "M": "3,083,918.31€"
  },
  {
    "AGE": "55-64",
    "F": "3,728,128.00€",
    "M": "1,955,855.30€"
  },
  {
    "AGE": ">=65",
    "F": "2,942,063.39€",
    "M": "1,664,503.04€"
  }
]
```

Other routes:
```shell
curl -u test_username:test_password -i -X GET http://0.0.0.0:8000/geoapp/geometry/[geometry]
curl -u test_username:test_password -i -X GET http://0.0.0.0:8000/geoapp/all
```

---
### Registration
To register a new user:

```shell
curl -X POST -H "Content-Type: application/json" -d '{"username":"username","password":"password"}' http://0.0.0.0:8000/registration/users
```
