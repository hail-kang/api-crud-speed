# api-crud-speed
데이터 CRUD 속도를 측정하는 API

# 사용 모듈
- django == 3.2.7
- djangorestframewokr == 3.12.4
- drf-yasg == 1.20.0
```
# pip 사용시
$ pip install django djangorestframework drf-yasg
```

# 사용 방법
```
$ python ./api_crud_speed/manage.py migrate
$ python ./api_crud_speed/manage.py runserver {host}:{port}
```

# API Docs
- runserver이후 "{host}:{port}/swagger"에 접속 
