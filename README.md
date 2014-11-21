#Heroku-config-grep
About to decomission that AWS key? Or perhaps want to find which app has their logs set to verbose? With this tool, it makes it easy to grep through all of your heroku apps
to make sure that you won't accidently change something that an Application is using.

##Dependencies
Relies on the Heroku command line client being installed and signed in to your account.

##Usage
```bash
$ heroku-config-grep.py MY_SEARCH_STRING
< sit back and wait for matching entries to be printed >
```

##Future Work
Lots of things could be added: 
- highlighting of the matching strings
- paralellizing the Heroku API calls for better speed
- repl mode so we don't fetch config every time
- proper command line interface, with verbose or quiet options.
- better error handling
