Geoapp
============

### Application

Run application
```
sh run_app.sh
```
This script will:
- Initialize database
- Activate app environment
- Install all requirements
- Serve flask application

---

### Requests

To access the routes with authorization (with default user/passsword) using *curl*:

```shell
curl -u test_username:test_password -i -X GET http://0.0.0.0:8000/geoapp/zipcode/[zipcode]
```

(Can also be done choosing *BasicAuth* in Postman for example and setting username and password)

A successful response looks like:

```json
{
  "<=24": [
    {
      "gender": "F",
      "turnover": "800,580.92€"
    },
    {
      "gender": "M",
      "turnover": "498,425.54€"
    }
  ],
  "25-34": [
    {
      "gender": "M",
      "turnover": "1,881,514.79€"
    },
    {
      "gender": "F",
      "turnover": "3,099,364.30€"
    }
  ],
  "35-44": [
    {
      "gender": "F",
      "turnover": "3,851,275.79€"
    },
    {
      "gender": "M",
      "turnover": "2,636,725.90€"
    }
  ],
  "45-54": [
    {
      "gender": "F",
      "turnover": "4,232,049.79€"
    },
    {
      "gender": "M",
      "turnover": "3,083,918.31€"
    }
  ],
  "55-64": [
    {
      "gender": "F",
      "turnover": "3,728,128.00€"
    },
    {
      "gender": "M",
      "turnover": "1,955,855.30€"
    }
  ],
  ">=65": [
    {
      "gender": "M",
      "turnover": "1,664,503.04€"
    },
    {
      "gender": "F",
      "turnover": "2,942,063.39€"
    }
  ]
}
```

---
### Registration
To register a new user:

```shell
curl -i -X POST -H "Content-Type: application/json" -d '{"username":"username","password":"password"}' http://0.0.0.0:8000/registration/users
```
