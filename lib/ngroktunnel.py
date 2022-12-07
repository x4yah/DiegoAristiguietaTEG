from pyngrok import ngrok

def create_tunnel():
    try: 
        http_tunnel = ngrok.connect(4444, 'tcp')
        return(http_tunnel.public_url)
    except:
        print("\n\tNo se pudo conectar a nrgok, intente de forma manual.\n")
        return(None)
