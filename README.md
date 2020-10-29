# Flask-Requests Demo

## Showcase interactions between Flask and Requests.

Start the server with:

``` bash
% python main.py server
```

and then run the client loop in a separate terminal:

``` bash
% python main.py client
```

The client makes this call:

``` python
requests.post(
    address+'?some-name=from-url-parameters',
    data={'some-name': 'from data'},
    headers={'some-name': 'from headers'})
```

And the server logs the following:

``` log
INFO:root:##################################################
INFO:root:request.headers.get | from headers
INFO:root:request.args.get    | from-url-parameters
INFO:root:request.form.get    | from data
```

See how the `Flask headers` map to the `request headers` nicely. But the `args` come from the `url`, and the `form` comes from the `data` argument.
