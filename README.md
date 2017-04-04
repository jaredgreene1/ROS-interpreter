# Setup
Install `virtualenv` and `virtualenvwrapper:
    - [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
    - [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/install.html)

Create your virtualenv:
```sh
mkvirtualenv ros
```

To activate or dectivate, do the following:
```sh
workon ros // activates ros virtualenv
deactivate // deactivates current virtualenv
```

Install requirements:
```sh
pip install -r requirements.txt
```

Now run the app:
```sh
python app.py
```

---

Here is how you pick up a VERY rudimentary interpreter:

1) Start the application with 'python parser.py' which uses cherrypy to pick up a very basic server listening for an HTTP request containing JSON"
2) Now, since the webhook URL for API.AI needs to be a public url, we use ngrok which establishes a public url that tunnels the request to our locally hosted server by running './ngrok http [PORT #]'
3) The default port number used by cherrypy is 8080 so the command would be './ngrok http 8080' which will provide a forwarding url which will look something like 'http://433bd302.ngrok.io'
4) This forwarding URL is what will be placed in the URL input on API.AI
5) The place to put this URL is found in the Fulfillment screen
6) Then you can use the practice agent on the right hand side to start testing the JSON requests sent by API.AI
