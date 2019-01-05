import time
import datetime
import logging

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import sevensegment
from luma.led_matrix.device import max7219

logging.basicConfig(filename='smartwatch.log', filemode='w+')

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=1)
display = sevensegment(device)
logging.info('Started app')


def prepare_time_for_display(hour, minute, second):
    return 't {hour}.{minute}.{second}'.format(hour=str(hour).zfill(2), minute=str(minute).zfill(2), second=str(second).zfill(2))

def prepare_date_for_display(day, month, year)
    return pass

while (True):
    # TODO set time format from datetme library, next try to send systemtime to watch
    logging.debug('Started new loop')
    try:
        for second in range(10):
            for second in range(30):
                czas = datetime.datetime.now()
                komunikat = prepare_time_for_display(czas.hour, czas.minute, czas.second)
                display.text = komunikat
                time.sleep(1)
            data = datetime.datetime.now()
            komunikat = str(data.day).zfill(2) + '.' + str(data.month).zfill(2) + '.' + str(data.year)
            display.text = str(komunikat)
            time.sleep(10)
    except Exception as e:
        logging.critical('Critical exception: {}'.format(e.message))
        komunikat = 'Error'
        display.text = str(komunikat)
