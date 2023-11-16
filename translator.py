from tkinter import *
import tkinter.ttk as ttk
import requests
from tkinter import messagebox

token = 'afe1fa60afe1fa60afe1fa6083acf7d8e3aafe1afe1fa60caa15fbacb31cdb69a225a39'

window = Tk()
window.title('Лучший переводчик')
window.geometry('500x450')



from_lang = ttk.Combobox(window)
to_lang = ttk.Combobox(window)
from_lang['value'] = ('английский', 'испанский','португальский','русский')
to_lang['value'] = ('английский', 'испанский','португальский','русский')

from_lang.set('английский')
to_lang.set('русский')



langs = {
    'английский': 'en',
    'испанский': 'es',
    'португальский': 'pt',
    'русский': 'ru'
}


from_lang_label = Label(window, text='Перевести с')
to_lang_label = Label(window, text='На')
output = Label(window, font=('', 15))

input = Text(window, width=56, height=10)
input.focus()



def translate(*args):
    try:
        if from_lang.get() == 'русский' or to_lang.get() == 'русский':
            text = input.get("1.0", "end-1c")
            lang = str(langs[from_lang.get()]+'-'+langs[to_lang.get()])
            response = requests.get('https://api.vk.com/method/translations.translate',
                                    params={
                                        'access_token': token,
                                        'v': 5.154,
                                        'texts': text,
                                        'translation_language': lang
                                    }
                                    )

            data = response.json()


            output.configure(text=text+':' + '\n'+str(''.join(data['response']['texts'])))
            print(output)
            input.delete('1.0', END)

        else:
            messagebox.showerror(message='Некорректный язык перевода,\n выберите другой')
            output.configure(text='')
    except KeyError:
        messagebox.showerror(message='Введите текст')



        #обнуляем комбобоксы
     #   from_lang.set('')
     #   to_lang.set('')


def switch_langs_func(*args):

    help = to_lang.get()
    to_lang.set(from_lang.get())
    from_lang.set(help)


transl_button = Button(window, text='перевести', command=translate)
switch_langs = Button(window, text='↔', font=('', 20), command=switch_langs_func)


from_lang_label.place(relx=0.13, rely=0.13)
to_lang_label.place(relx=0.77, rely=0.13)
from_lang.place(relx=0.01, rely=0.2)
to_lang.place(relx=0.58, rely=0.2)
input.place(relx=0.1, rely=0.3)
output.place(relx=0.43, rely=0.8)
transl_button.place(relx=0.4, rely=0.7)
switch_langs.place(relx=0.45, rely=0.191)

#transl_button.bind('<Button-1>', translate)
#transl_button.bind('<Return>', translate)

window.mainloop()

