# coding=utf-8
from subprocess import check_call, check_output
import time
from uiautomator import Device


class PhoneControl:
    def __init__(self, timeout=3):
        self.device = None
        self.serial = ""
        self.time = timeout

    def read_serial(self):
        output = check_output(['adb', 'devices'])
        lines = output.splitlines()
        self.serial = lines[1].split()[0]
        return self.serial

    def init_device(self):
        d = Device(self.serial)
        self.device = d

    def unlock_phone(self):
        check_call(['adb', '-s', self.serial, 'shell', 'input keyevent', 'KEYCODE_WAKEUP'])
        time.sleep(self.time)

    def click_home(self):
        check_call(['adb', '-s', self.serial, 'shell', 'input keyevent', 'KEYCODE_HOME'])
        time.sleep(self.time)

    def switch_button(self, text):
        self.device(text=text, className='android.widget.Switch').click()
        time.sleep(self.time)

    def click_button(self, text):
        self.device(text=text, className='android.widget.TextView').click()
        time.sleep(self.time)

    def longclick_button(self, text):
        self.device(text=text, className='android.widget.TextView').long_click()
        time.sleep(self.time)

    def button_exists(self, text, classname):
        if self.device(text=text, className=classname).exists:
            return True
        else:
            return False

    def click_detailed_button(self, classname, packagename, description):
        self.device(packageName=packagename, className=classname, description=description).click()
        time.sleep(self.time)

    def detailed_button_exists(self, classname, packagename, description):
        if self.device(packageName=packagename, className=classname, description=description).exists:
            return True
        else:
            return False

    def longclick_detailed_button(self, classname, packagename, description):
        self.device(packageName=packagename, className=classname, description=description).long_click()

    def set_text_textfield(self, packagename, content):
        self.device(packageName=packagename, className='android.widget.EditText').set_text(content)

