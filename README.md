# pydemo
A simple demo docker swarm service in python for testing TLS
It runs a simple cherrypy service that listens on port 443, and serves over TLS.
To setup TLS certificates, pass in the server certificate and key as secrets named
`server.crt` and `server.key`.

Hitting https://<hostname>/sleep/<secs> will cause the server to sleep that many
seconds (emitting a line every second). This allows for simulating differing workloads.


