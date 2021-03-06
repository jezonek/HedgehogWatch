import time
import datetime
import logging

from luma.core.interface.serial import spi, noop
from luma.core.virtual import sevensegment
from luma.led_matrix.device import max7219

from utils import prepare_time_for_display, prepare_date_for_display

logging.basicConfig(filename='smartwatch.log', filemode='w+')

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=1)
display = sevensegment(device)
logging.info('Started app')

while True:
    try:
        for cycle in range(10):
            for second in range(30):
                current_time = datetime.datetime.now()
                statement = prepare_time_for_display(current_time.hour, current_time.minute, current_time.second)
                display.text = statement
                time.sleep(1)
            current_date = datetime.datetime.now()
            statement = prepare_date_for_display(current_date.day, current_date.month, current_date.year)
            display.text = str(statement)
            time.sleep(10)
    except Exception as e:
        logging.critical('Critical exception: {}'.format(e.message))
        statement = 'Error'
        display.text = str(statement)
