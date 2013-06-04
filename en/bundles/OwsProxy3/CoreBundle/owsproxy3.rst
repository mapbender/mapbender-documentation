.. _owsproxy3:

OWSProxy3
***********************

OWSProxy3 is a transparent Buzz-based proxy that uses cURL for connection to web
resources via/without a proxy server.


Configuration
=============

The configuration is done in the file config.yml at the section ows_proxy3_core.

.. code-block:: yaml

	ows_proxy3_core:
	    logging: true               # logging of requests, default is true, true logs in table owsproxy_log 
	    obfuscate_client_ip: true   # obfuscats a client ip, use 'true' to hide the last byte of the client's ip address
	    proxy:                      # proxy definition for connnection via a proxy server
		                        # at least 'host' and 'port' are needed for proxy definition
                connecttimeout: 30      # default 30s
                timeout: 60             # default 60s 
		host:                   # host name of the proxy server
		port:                   # port number of the proxy server
		user:                   # user name for proxy server (set user for proxy server if needed)
		password:               # password for proxy server (set password for proxy server if defined)
		noproxy:                # list of hosts for connnections without proxy
		    - host_a            # host name
