from interface import uicoords
import time
global device

typelist = ['cash_amount', 'share_amount', 'limit_price']

def init_current_device(passed_device):
    global device
    device = passed_device
def type(text):
    device.shell(f'input text "{text}"')


def tap(x, y):
    buffer()
    device.shell(f'input tap {x} {y}')


def back():
    device.shell(f'input keyevent 4')


def reorient_to_explore():
    x, y = uicoords.get('explore')
    device.shell(f'input tap  {x} {y}')


def lookup_stock(stock):
    tap(*uicoords.get('searchbar'))
    time.sleep(2)
    type(stock)
    time.sleep(2)
    tap(*uicoords.get('first_stock'))
    tap(*uicoords.get('first_stock'))


def buy_stock(stock, amount, type='cash_amount'):
    reorient_to_explore()
    lookup_stock(stock)
    tap(*uicoords.get('buy_button'))
    tap(*uicoords.get('marketprice_cash_amount'))
    enter_amount(amount)
    tap(*uicoords.get('review_button'))
    tap(*uicoords.get('submit_button'))
    buffer(8)
    tap(*uicoords.get('done_button'))
    back()
    back()


def sell_stock(stock, amount, type='cash_amount'):
    reorient_to_explore()
    lookup_stock(stock)
    tap(*uicoords.get('sell_button'))
    tap(*uicoords.get('marketprice_cash_amount'))
    tap(*uicoords.get('max_button'))
    tap(*uicoords.get('review_button'))
    tap(*uicoords.get('submit_button'))
    buffer(8)
    tap(*uicoords.get('done_button'))
    back()
    back()


def buffer(seconds=0.5):
    time.sleep(seconds)


def enter_amount(amount: float):
    buffer()
    for number in str(amount):
        tap(*uicoords.get(number))
