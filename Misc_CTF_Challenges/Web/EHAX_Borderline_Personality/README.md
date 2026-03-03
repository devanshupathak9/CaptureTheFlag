<!-- # CTF Writeup: Borderline Personality

ℹ️ Challenge Info
* Event: [EHAX CTF]
* Category: [Web]
* Difficulty: [Easy]


## Description
The proxy thinks it's in control. The backend thinks it's safe. Find the space between their lies and slip through.
### Summary


### Initial Discovery & Analysis

Code snippet
```

```


## Exploitation / Solution Path

## Solve Script


## Flag:
CTF{th1s_is_th3_fl4g}

```
path: http://chall.ehax.in:9098/admin/flag: blocked
path: http://chall.ehax.in:9098/%61%64%6d%69%6e/flag
path: http://chall.ehax.in:9098/%61dmin/flag
``` -->

CTF Writeup: Borderline Personality

ℹ️ Challenge Info

Event: EHAX CTF

Category: Web

Difficulty: Easy

Description

The proxy thinks it's in control. The backend thinks it's safe. Find the space between their lies and slip through.

Summary

This challenge demonstrates a classic reverse proxy bypass using URL encoding.

The /admin/flag endpoint is blocked at the proxy layer using an ACL rule in HAProxy, but the backend (Flask app) still exposes it.

By sending a URL-encoded version of /admin/flag, we bypass the proxy filter and directly access the flag.

Architecture Overview
User → HAProxy (Port 8080) → Flask Backend (Port 5000)

HAProxy acts as a reverse proxy

It blocks /admin using a regex ACL

Flask backend still serves /admin/flag

This creates a trust mismatch between proxy and backend.

Initial Discovery & Analysis

We are given access to:

http://chall.ehax.in:9098/

Trying to directly access:

http://chall.ehax.in:9098/admin/flag

Results in:

Blocked / Denied
🔎 Looking at HAProxy Configuration
frontend http-in
    bind *:8080
    
    acl restricted_path path -m reg ^/+admin
    http-request deny if restricted_path
    
    default_backend application_backend
🚨 Important Line
acl restricted_path path -m reg ^/+admin

This means:

Match any path starting with /admin

If matched → deny request

So HAProxy blocks requests where the path starts with /admin.

🔎 Looking at Backend (Flask)
@app.route('/admin/flag', methods=['GET', 'POST'])
def flag():
    return "EHAX{TEST_FLAG}\n", 200

The backend does expose /admin/flag.

So the vulnerability is:

The proxy blocks based on raw path matching, but the backend processes decoded paths.

Understanding the Vulnerability
🔹 Reverse Proxy

A reverse proxy sits in front of the backend server and filters requests before forwarding them.

Here:

HAProxy is the gatekeeper.

It uses a regex to block /admin.

🔹 URL Encoding

URL encoding replaces characters with % followed by their ASCII hex value.

Example:

Character	ASCII	Encoded
a	97	%61
d	100	%64
m	109	%6d
i	105	%69
n	110	%6e

So:

admin → %61%64%6d%69%6e
Why This Works

HAProxy checks the path before decoding.

So:

/admin/flag      → Blocked
/%61%64%6d%69%6e/flag → NOT blocked

Because the regex ^/+admin does not match %61%64%6d%69%6e.

However…

Flask automatically decodes the URL before routing.

So:

/%61%64%6d%69%6e/flag

Becomes:

/admin/flag

When it reaches Flask.

🔥 Result → Proxy allows it, backend serves it.

This is a classic proxy normalization mismatch vulnerability.

Exploitation / Solution Path

Try accessing:

http://chall.ehax.in:9098/%61%64%6d%69%6e/flag

or even partially encoded:

http://chall.ehax.in:9098/%61dmin/flag

Because:

%61 = a

Rest stays same

HAProxy regex doesn't match

Flask decodes correctly

Working Payload
path: http://chall.ehax.in:9098/admin/flag   → blocked
path: http://chall.ehax.in:9098/%61%64%6d%69%6e/flag  → works
path: http://chall.ehax.in:9098/%61dmin/flag → works
Solve Script

Using curl:

curl http://chall.ehax.in:9098/%61%64%6d%69%6e/flag

Using Python:

import requests

url = "http://chall.ehax.in:9098/%61%64%6d%69%6e/flag"
r = requests.get(url)
print(r.text)
Root Cause

The vulnerability exists because:

HAProxy filters based on raw path.

Flask processes decoded path.

No normalization consistency between proxy and backend.

This is known as:

URL normalization bypass

Reverse proxy bypass

Path encoding attack

How to Fix It (Defensive Insight)

Proper mitigation:

Normalize URL before applying ACL

Use:

http-request set-path %[path,decode]

before ACL checks

Or block after decoding

Final Flag
EHAX{TEST_FLAG}