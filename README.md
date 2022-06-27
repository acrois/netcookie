# netcookie

Netcookie is a small Python script to generate standard cookie.txt files from various inputs such as Google Chrome (Application -> Cookies) to circumvent the need to install overly-permissive WebKit plugins to do the job.

## Installation

```sh
git clone https://github.com/kinetechsolutions/netcookie.git
cd netcookie
pip install -r requirements.txt
```

## Running

Netscape style output to `moz.txt` is achieved using Python's `cookiejar.MozillaCookieJar()` class.

### Chrome conversion

1. Copy the output of Developer Tools (Application -> Cookies) to `chrome.txt`
2. Ensure the header row is present in the file `chrome.txt`.
3. Convert

#### chrome.txt File Headers

```tsv
name	value	domain	path	max_age	size	http_only	secure	same_site	same_party	priority
```

#### Conversion

This will generate a `cookies.txt` and a `moz.txt`, you want to use `moz.txt` for your application's purposes.

```sh
py chrome.py
```