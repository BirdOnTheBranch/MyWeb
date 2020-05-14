&nbsp;
# MyWeb

>I develop my personal web site with Flask.


If you want to visit it, click here: [Luisplanelles.com](https://www.luisplanelles.com/)

&nbsp;

---

## Run app 


You need docker "https://www.docker.com/"
*Ensure you have Docker installed in your system.*

&nbsp;

**-First we build the docker-compose.**


`$ docker-compose build`  

*You should get an output like this:*

```
 ...
Step 1/5 : FROM python:3.8-slim-buster
3.8-slim-buster: Pulling from library/python
...

...
---> a1c95d6a940f
Successfully built a1c95d6a940f
Successfully tagged myweb_web:latest

```


**-Second run the server in background, and conect your host at Flask-server.**


`$ docker-compose up -d`


*You should get an output like this:*

`Creating my-web_web ... done`

&nbsp;

---

## Starting the application

To run the application, open a terminal and call `docker-compose run` and migrate your data base and using the port `0.0.0.0:8000`


`$ docker-compose run web`

*You should get an output like this:*

```
Starting server
 * Serving Flask app "my-web"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)
```

&nbsp;


---

## Starting the test

`$ docker-compose run test`

**Tests for:**
 * Test to check the correct working to the app.
 * Test to check the datas of the apis whit mocks.

&nbsp;

---

**Built with:**
* [Python 3](https://www.python.org/download/releases/3.0/ "Python 3") - v3.7.2
* [Flask](https://flask.palletsprojects.com/en/1.1.x/ "Flask") - 1.1.1
* [Docker](https://www.docker.com/ "Docker"): Tool to create, deploy and run applications using containers. v19.03.5, build 633a0ea

&nbsp;
&nbsp;

**welcome to my-web.**