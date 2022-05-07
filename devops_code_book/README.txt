ตั้งแต่ Chapter8 - Chapter16 ผู้อ่านจะได้รับ Code สำหรับการทำ Practice Workshop เพื่อความสะดวกโดยไม่ต้องพิมพ์ Code เองตั้งแต่ต้น

Chapter8
docker101/
.
├── Dockerfile
└── main.py

Chapter9
small_image/
.
├── Dockerfile
└── Dockerfile_edit #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ Dockerfile เมื่อทำ Practice Workshop ถึงหน้า 132

web_dock/
.
├── docker-compose.yml
└── server/
    ├── Dockerfile
    ├── index.html
    └── server.py

port_dock/
.
├── docker-compose.yml
└── .env

Chapter10
httpd_dock/
.
├── docker-compose.yml
└── html/
    └── index.html

nginx_dock/
.
├── docker-compose.yml
└── static-html/
    └── index.html

lemp_dock/
.
├── docker-compose.yml
├── docker-compose_edit.yml #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ docker-compose.yml เมื่อทำ Practice Workshop ถึงหน้า 167
├── html/
│   ├── index.php
│   └── index_edit.php #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ index.php เมื่อทำ Practice Workshop ถึงหน้า 169
├── mariadb/
│   ├── backup/
│   ├── data/
│   └── initdb/
│       └── titanic.sql
├── nginx
│   ├── conf/
│   │   └── nginx.conf
│   └── conf.d/
│       └── default.conf
└── php/
    └── Dockerfile

Chapter11
nginx_proxy_dock/
.
├── docker-compose.yml
└── docker-compose_edit.yml #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ docker-compose.yml เมื่อทำ Practice Workshop ถึงหน้า 190

website1/
.
├── docker-compose.yml
├── docker-compose_edit.yml #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ docker-compose.yml เมื่อทำ Practice Workshop ถึงหน้า 182
├── docker-compose_edit2.yml #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ docker-compose.yml เมื่อทำ Practice Workshop ถึงหน้า 192
├── docker-compose_edit3.yml #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ docker-compose.yml เมื่อทำ Practice Workshop ถึงหน้า 195
├── html/
│   ├── index.php
│   └── index_edit.php #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ index.php เมื่อทำ Practice Workshop ถึงหน้า 183
├── mariadb/
│   ├── backup/
│   ├── data/
│   └── initdb/
│       └── titanic.sql
├── nginx/
│   ├── conf/
│   │   └── nginx.conf
│   └── conf.d/
│       └── default.conf
└── php/
    └── Dockerfile

website2/
.
├── docker-compose.yml
├── docker-compose_edit.yml #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ docker-compose.yml เมื่อทำ Practice Workshop ถึงหน้า 186
├── docker-compose_edit2.yml #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ docker-compose.yml เมื่อทำ Practice Workshop ถึงหน้า 194
├── html/
│   ├── index.php
│   └── index_edit.php #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ index.php เมื่อทำ Practice Workshop ถึงหน้า 187
├── mariadb/
│   ├── backup/
│   ├── data/
│   └── initdb/
│       └── titanic.sql
├── nginx/
│   ├── conf/
│   │   └── nginx.conf
│   └── conf.d/
│       └── default.conf
└── php/
    └── Dockerfile

Chapter12
mq_dock/
.
└── docker-compose.yml

register_gateway_dock/
.
├── docker-compose.yml
└── python/
    ├── Dockerfile
    ├── api.py
    └── requirements.txt

student_dock/
.
├── docker-compose.yml
├── mariadb/
│   ├── backup/
│   ├── data/
│   └── initdb/
│       └── devops_db.sql
└── python/
    ├── Dockerfile
    ├── requirements.txt
    └── rpc.py

enroll_dock/
.
├── docker-compose.yml
├── mariadb/
│   ├── backup/
│   ├── data/
│   └── initdb/
│       └── devops_db.sql
└── python/
    ├── Dockerfile
    ├── requirements.txt
    └── rpc.py

email_dock/
.
├── docker-compose.yml
└── python/
    ├── Dockerfile
    ├── requirements.txt
    └── rpc.py

Chapter13
kong_dock/
.
├── docker-compose.yml
└── prometheus.yml

grafana_dock/
.
└── docker-compose.yml

Chapter14
otp_dock/
.
├── docker-compose.yml
└── python/
    ├── Dockerfile
    ├── requirements.txt
    └── rpc.py

send_email_otp_dock/
.
├── docker-compose.yml
└── python/
    ├── Dockerfile
    ├── requirements.txt
    └── rpc.py

otp_gateway_dock/
.
├── docker-compose.yml
└── python/
    ├── Dockerfile
    ├── api.py
    └── requirements.txt

session_server_dock/
.
└── docker-compose.yml

register_ui_dock/
.
├── docker-compose.yml
└── python/
    ├── Dockerfile
    ├── model.py
    ├── requirements.txt
    ├── templates/
    │   ├── authen.html
    │   ├── otp.html
    │   └── reg.html
    └── ui.py

Chapter15
register_ui_dock/
.
├── docker-compose.yml
├── docker-compose_edit.yml #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ docker-compose.yml เมื่อทำ Practice Workshop ถึงหน้า 341
└── python/
    ├── Dockerfile
    ├── model.py
    ├── requirements.txt
    ├── requirements_edit.txt #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ requirements.txt เมื่อทำ Practice Workshop ถึงหน้า 333
    ├── templates/
    │   ├── authen.html
    │   ├── authen_edit.html #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ authen.html เมื่อทำ Practice Workshop ถึงหน้า 350
    │   ├── otp.html
    │   ├── otp_edit.html #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ otp.html เมื่อทำ Practice Workshop ถึงหน้า 350
    │   ├── otp_edit2.html #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ otp.html เมื่อทำ Practice Workshop ถึงหน้า 383
    │   ├── reg.html
    │   └── reg_edit.html #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ reg.html เมื่อทำ Practice Workshop ถึงหน้า 351
    ├── ui.py
    ├── ui_edit.py #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ ui.py เมื่อทำ Practice Workshop ถึงหน้า 334
    └── ui_edit2.py #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ ui.py เมื่อทำ Practice Workshop ถึงหน้า 347

register_gateway_dock/
.
├── docker-compose.yml
├── docker-compose_edit.yml #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ docker-compose.yml เมื่อทำ Practice Workshop ถึงหน้า 354
└── python/
    ├── Dockerfile
    ├── api.py
    ├── api_edit.py #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ api.py เมื่อทำ Practice Workshop ถึงหน้า 355
    └── requirements.txt

otp_gateway_dock/
.
├── docker-compose.yml
├── docker-compose_edit.yml #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ docker-compose.yml เมื่อทำ Practice Workshop ถึงหน้า 357
└── python/
    ├── Dockerfile
    ├── api.py
    ├── api_edit.py #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ api.py เมื่อทำ Practice Workshop ถึงหน้า 357
    └── requirements.txt

student_dock/
.
├── docker-compose.yml
├── docker-compose_edit.yml #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ docker-compose.yml เมื่อทำ Practice Workshop ถึงหน้า 360
├── mariadb/
│   ├── backup/
│   ├── data/
│   └── initdb/
│       └── devops_db.sql
└── python/
    ├── Dockerfile
    ├── Dockerfile_edit #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ Dockerfile เมื่อทำ Practice Workshop ถึงหน้า 361
    ├── requirements.txt
    └── rpc.py

enroll_dock/
.
├── docker-compose.yml
├── docker-compose_edit.yml #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ docker-compose.yml เมื่อทำ Practice Workshop ถึงหน้า 362
├── mariadb/
│   ├── backup/
│   ├── data/
│   └── initdb/
│       └── devops_db.sql
└── python/
    ├── Dockerfile
    ├── Dockerfile_edit #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ Dockerfile เมื่อทำ Practice Workshop ถึงหน้า 363
    ├── requirements.txt
    └── rpc.py

email_dock/
.
├── docker-compose.yml
├── docker-compose_edit.yml #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ docker-compose.yml เมื่อทำ Practice Workshop ถึงหน้า 364
└── python/
    ├── Dockerfile
    ├── Dockerfile_edit #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ Dockerfile เมื่อทำ Practice Workshop ถึงหน้า 365
    ├── requirements.txt
    └── rpc.py

otp_dock/
.
├── docker-compose.yml
├── docker-compose_edit.yml #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ docker-compose.yml เมื่อทำ Practice Workshop ถึงหน้า 367
└── python/
    ├── Dockerfile
    ├── Dockerfile_edit #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ Dockerfile เมื่อทำ Practice Workshop ถึงหน้า 368
    ├── requirements.txt
    └── rpc.py

send_email_otp_dock/
.
├── docker-compose.yml
├── docker-compose_edit.yml #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ docker-compose.yml เมื่อทำ Practice Workshop ถึงหน้า 370
└── python/
    ├── Dockerfile
    ├── Dockerfile_edit #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ Dockerfile เมื่อทำ Practice Workshop ถึงหน้า 371
    ├── requirements.txt
    └── rpc.py

mq_dock/
.
├── docker-compose.yml
└── docker-compose_edit.yml #นำ Code ในไฟล์นี้ไปแทนที่ Code ในไฟล์ docker-compose.yml เมื่อทำ Practice Workshop ถึงหน้า 372

Chapter16
test_project/
.
├── app.py
├── conftest.py
├── pytest.ini
├── src/
│   ├── __init__.py
│   └── math.py
└── tests/
    └── unit_tests
        └── math_test.py

otp_dock/
.
├── docker-compose.yml
├── .gitlab-ci.yml
└── python/
    ├── Dockerfile
    ├── conftest.py
    ├── pytest.ini
    ├── requirements.txt
    ├── rpc.py
    ├── src/
    │   ├── __init__.py
    │   └── otp.py
    ├── tests/
    │   └── unit_tests/
    │       └── otp_test.py
    └── .env

gitlab_dock/
.
└── docker-compose.yml

runner_dock/
.
├── docker-compose.yml
└── runner_registry.sh
