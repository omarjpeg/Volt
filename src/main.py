from ppadb.client import Client as AdbClient
import time
def home():
    device.shell('input tap  540 2080')

def lookup(stock):
    device.shell(f'input tap  500 840')
    time.sleep(3)
    device.shell(f'input text "{stock}"')
    device.shell(f'input tap  500 840')
    device.shell(f'input tap  515 545')

def tap(x,y):
    device.shell(f'input tap {x} {y}')

def buy(stock,amount):
    home()
    lookup(stock)

numpad = {
1:(155,1425),
2:(545,1425),
3:(920,1425),
4:(155,1625),
5:(545,1625),
6:(920,1625),
7:(155,1825),
8:(545,1825),
9:(920,1825),
0:(545,2025),
'point':(155,2025),
'backspace':(920,2025)
}

uicoords = {
    'searchbar': (515,870),
    'explore': (540,2080),
    'firststock':(530,520),
    'buy': (300,2050),
    'sell':(800,2050),
    'marketprice(shares)':(555,745),
    'marketprice(amount)':(555,1035),
    'review' :(535,1220),
    'submit':(535,1220),
    'done':(535,1810)
}

if __name__ == '__main__':
    client = AdbClient(host="127.0.0.1", port=5037)  # Default is "127.0.0.1" and 5037

    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]

    print(f'Connected to {device}')
    home()
    lookup('MNHD')
    print('wtf')
    for i,coords in numpad.items():
        tap(coords[0],coords[1])
        print('lol')
    # device.shell('input tap  500 500 500 900 1000')
