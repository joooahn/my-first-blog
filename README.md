# Todo List

Django로 만든 Todo List


### Installing

1. Python 3.6 설치

```
$ sudo apt install python3.6
```

(Could not get lock /var/lib/dpkg/lock - open (11: Resource temporarily unavailable) 오류 발생 시)
```
$ rm /var/lib/dpkg/lock
```
이후에
```
$ sudo apt install python3.6
```


2. git 설치

```
$ sudo apt install git
```


3. git에서 코드 복사

```
$ git clone https://github.com/joooahn/my-first-blog.git
```


4. 가상환경(virtualenv) 설치 후 실행

```
$ cd my-first-blog
$ sudo apt install virtualenv
$ virtualenv --python=python3.6 myvenv
$ source myvenv/bin/activate
```


5. 데이터베이스 설치

```
(mvenv) $ python manage.py migrate
(mvenv) $ python manage.py createsuperuser
```


6. 서버 실행

```
(myenv) $ python manage.py runserver
```


7. 웹브라우저로 접속

```
(웹 브라우저 주소창에) http://127.0.0.1:8000/
```
