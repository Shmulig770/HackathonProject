from pynput.keyboard import Listener

def key_listening():
    with Listener(on_press=letter_import) as listening:
        listening.join()

def letter_import(letter):
    global a
    letter = str(letter)
    letter = letter.replace("'", "")
    if letter in ['Key.space', 'Key.enter']:
        letter = ' '
    if letter in ["Key.caps_lock" , "Key.shift_r" , "Key.backspace" , "Key.ctrl_l" , "Key.shift"]:
        letter = ""
    print(letter)
    #פה צריך להיות קריאה לפונקציה שנכתוב (המנג'ר) שלוקח את האות שהתקבלה ושומר אותה בבפר
    return letter


key_listening()
