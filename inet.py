import gc
import socket
import network
import esp

esp.osdebug(None)
gc.collect()


class WebDriver:
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

    def web_page(self, headers: list[str], body: list[str]) -> str:
        if len(headers) != len(body):
            raise ValueError(
                "web_page: expected one header for each body element!")
        html = \
            """<html><head><meta name="viewport" content="width = device-width, initial-scale = 1"></head><body>""" \
            + \
            "".join(["<h1>" + a + "</h1>" + b for (a, b) in zip(headers, body)]) \
            + \
            """</body></html>"""
        return html

    def serve(self, headers: list[str], callbacks):
        while True:
            conn, addr = self.s.accept()
            print('Got a connection from %s' % str(addr))
            request = conn.recv(1024)
            print('Content = %s' % str(request))
            body = [str(f()) for f in callbacks]
            response = self.web_page(headers, body)
            conn.send(response)
            conn.close()
