from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional

with SB(uc=True, test=True) as sb:

    if True:
        url = "https://www.reddit.com/r/brutalles"
        sb.uc_open_with_reconnect(url, 5)
        sb.uc_gui_click_captcha()
        sb.sleep(1)
        sb.uc_gui_handle_captcha()
        sb.sleep(1)
        url = "https://gsght.com/c/eo9k4j"
        sb.uc_open_with_reconnect(url, 5)
        sb.uc_gui_click_captcha()
        sb.sleep(1)
        sb.uc_gui_handle_captcha()
        sb.sleep(1)
        try:
            input_field = 'select[id="ageYear"]'
            sb.uc_click(input_field, reconnect_time=4)
            rnd = random.randint(1960,2008)
            sb.uc_gui_write(rnd)
            input_btn = 'a[id="view_product_page_btn"]'
            sb.uc_click(input_btn, reconnect_time=4)
        rnd = random.randint(15,600)
        sb.sleep(15)
