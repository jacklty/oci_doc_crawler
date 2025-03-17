Updated 2025-01-14
# Enable Session Persistence with Sticky Cookies
Enable persistent sessions using cookies in an App Gateway. The sticky cookie is forwarded to the same backend server.
You only need to use sticky support when you have multiple origins, and you do this by creating a NGINX upstream block .
  1. Enable the sticky module in App Gateway by editing the file `/usr/local/nginx/conf/nginx.conf`.
     * Below the line `load_module               /scratch/oracle/cloudgate/home/lib/idcs_cloudgate_ngx.so;`, add```
load_module /scratch/oracle/cloudgate/home/lib/ngx_http_sticky_module.so;
```

     * Below the line `include               /usr/local/nginx/conf/agent_conf/*.conf;`, add```
include /usr/local/nginx/conf/origin_conf/*.conf;
```

  2. Create a NGINX upstream block using```
$ vi /usr/local/nginx/conf/origin_conf/myupstream.conf
Add below entry to myupstream.conf
upstream weblogic {
  sticky;
  server 100.111.190.221:7003;
  server 100.111.190.220:7003;
}
```

  3. Change the origin server.
    1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
    2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Security** and then **App gateways**.
    3. Under Resources select Apps, and select the App gateway.
    4. In the App details, modify the **Origin server** to point to the upstream.


## Sticky Parameters 🔗 
```
upstream {
 sticky; 
 server 127.0.0.1:9001;
 server 127.0.0.1:9002;
}
 sticky [hash=index|md5|sha1] [no_fallback]
    [name=route] [domain=.example.com] [path=/] [expires=1h] [secure] [httponly];
  or
 sticky [hmac=md5|sha1 hmac_key=<foobar_key>] [no_fallback]
    [name=route] [domain=.example.com] [path=/] [expires=1h] [secure] [httponly];
  or
 sticky [text=raw] [no_fallback]
    [name=route] [domain=.example.com] [path=/] [expires=1h] [secure] [httponly];
```

## Server Selection Algorithm 🔗 
Algorithm | Description  
---|---  
`hash` |  The hash mechanism used to encode upstream server. It can't be used with `hmac` or `text`.
  * `md5|sha1`. Standard cryptographic hash functions to encode the information.
  * `index`. The information is not hashed and instead an in-memory index is used. This is quicker and the overhead is shorter, but the matching against upstream servers list is inconsistent and if the upstream server has changed index values might not correspond to the same server. Only use `index` if you are certain you want to use it despite this.

The default is `md5`.  
`hmac` | The HMAC hash mechanism used to encode upstream server It's like the hash mechanism but it uses `hmac_key` to secure the hashing. It can't be used with `hash` or `text`.  
`hmac_key` | The cryptographic key to use with `hmac`. Set a `hmac_key` if you use `hmac`.  
`no_fallback` | Set this flag so that if a request comes with a cookie and the corresponding backend is unavailable, a 502 (Bad Gateway or Proxy Error) is returned. You can set it to the upstream block, or set `sticky_no_fallback` in a server or location block.  
## Cookie Settings 🔗 
Setting | Description  
---|---  
`name` | The name of the cookie used to track the persistent upstream server. The default is `route`.  
`domain` | The domain in which the cookie is valid. The default is `none` when the browser handles the domain.  
`path` | The path in which the cookie is valid. The default is `/`.  
`expires` |  The validity duration of the cookie. The default is `nothing` which means that it's a session cookie and deleted when the client shuts down.  Enter a value to have the cookie expire after the specified time. The value is set relative to the client, and it must be for a period greater than one second.  
`secure` | Enable secure cookies (transferred only using https).  
`httponly` | Tells the browser that the cookie can only be accessed by the server.  
Was this article helpful?
YesNo

