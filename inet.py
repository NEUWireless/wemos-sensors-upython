import gc
import socket
import network
import esp

esp.osdebug(None)
gc.collect()


class INet:
    def __init__(self, ssid, pword):
        if len(pword) < 8:
            raise ValueError("INet: password length less than 8 characters!")
        self.ap = network.WLAN(network.AP_IF)
        self.ap.active(True)
        self.ap.config(essid=ssid, password=pword)
        while self.ap.active() == False:
            pass
        print('Connection successful')
        print(self.ap.ifconfig())

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('', 80))
        self.s.listen(5)

    def web_page(self) -> str:
        html = \
            """\
            <html><head><meta name="viewport" content="width=device-width, \
                initial-scale=1"></head><body><h1>Hello, World!</h1></body></html>\
            """
        return html

    def serve(self):
        while True:
            conn, addr = self.s.accept()
            print('Got a connection from %s' % str(addr))
            request = conn.recv(1024)
            print('Content = %s' % str(request))
            response = self.web_page()
            conn.send(response)
            conn.close()
