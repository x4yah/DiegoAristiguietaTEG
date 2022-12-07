#imports

from lib import ngroktunnel
from http.server import  HTTPServer
from clases import Server


URL = ngroktunnel.create_tunnel() #tunel tcp para el apk
print(f"\n\tNGROK URL: {URL}\n")

# ----------------> ejecucion s1 <---------------- #
if __name__ == "__main__":

	WebServer = HTTPServer(("127.0.0.1",3000), Server)
	WebServer.serve_forever()
