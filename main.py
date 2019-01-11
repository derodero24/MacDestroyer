
import os
import threading
import time
import tkinter as tk
from time import sleep

import pyautogui as pgui


class Terminal(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('ターミナル ー -bash ー 80×24')
        self.configure(width=750, height=450)

        self.wtext = tk.Text(self,
                             width=50, height=40,
                             padx=10, pady=8,
                             bg='#313131', fg='#ffffff',
                             wrap=tk.CHAR,
                             font=('Osaka', 14))
        self.wtext.place(x=-5, y=-5, width=760, height=460)
        self.wtext.tag_config('prompt', foreground='#00FFFF')
        self.wtext.tag_config('warning', foreground='#E50000')
        self.wtext.tag_config('error', foreground='#E5E500')

        self.frame = self.frame_gen()
        self.after(500, self.animation)

    def frame_gen(self):
        ''' animation frames '''
        # (text, wait_time, tag)
        frames = (
            ('Last login: Thu Jan 10 12:45:36 on ttys000\n', 1000, ''),
            (f'{os.uname()[1].split(".")[0]}:~ {os.environ["USER"]}$ ', 2000, 'prompt'),
            ('r', 50, ''),
            ('m', 100, ''),
            (' ', 300, ''),
            ('-', 200, ''),
            ('r', 50, ''),
            ('f', 100, ''),
            (' ', 100, ''),
            ('/', 1000, ''),
            ('\n', 200, ''),
            ("rm: '/' に関して再帰的に操作することは危険です\n", 20, 'warning'),
            ('rm: このフェイルセーフを上書きするには --no-preserve-root を使用してください\n', 20, 'warning'),
            (f'{os.uname()[1].split(".")[0]}:~ {os.environ["USER"]}$ ', 3000, 'prompt'),
            ('r', 50, ''),
            ('m', 100, ''),
            (' ', 600, ''),
            ('--no-preserve-root ', 600, ''),
            ('-', 80, ''),
            ('r', 50, ''),
            ('f', 100, ''),
            (' ', 200, ''),
            ('/', 1000, ''),
            ('\n', 200, '')
        )
        for f in frames:
            yield f

        # ディレクトリ・ファイル
        file_num = 0
        for root, dirs, files in os.walk('/'):
            yield (f"removed derectory: '{root}''\n", 10, '')
            for file_ in files:
                fpath = os.path.join(root, file_)
                fsize = os.path.getsize(fpath)
                yield (f"removed '{fpath}'\n", int(fsize / 50000), '')
                file_num += 1

            if file_num > 100:
                break

        # ネタばらし
        frames = (
            ('■■    ■  ■                     ■■         ■■      ■■\n', 10, ''),
            ('■■    ■■ ■■                    ■■         ■■      ■■\n', 10, ''),
            ('■■    ■■ ■■                    ■■         ■■      ■■\n', 10, ''),
            ('■■                         ■■■■■■■■■■     ■■      ■■\n', 10, ''),
            ('■■           ■■  ■    ■■       ■■         ■■      ■■\n', 10, ''),
            ('■■           ■■  ■■   ■■       ■■         ■■      ■■\n', 10, ''),
            ('■■■■■■       ■■  ■■  ■■         ■■        ■■      ■■\n', 10, ''),
            ('■■  ■■■■■■    ■■ ■■  ■■         ■■ ■■■    ■■      ■■\n', 10, ''),
            ('■■            ■■    ■■     ■■■■■■■■■      ■■      ■■\n', 10, ''),
            ('■■                  ■■          ■■               ■■\n', 10, ''),
            ('■■                 ■■           ■■               ■■\n', 10, ''),
            ('■■                ■■             ■■             ■■\n', 10, ''),
            ('■■               ■■              ■■             ■■\n', 10, ''),
            ('■■              ■■               ■■            ■■\n', 10, '')
        )
        for f in frames:
            yield f

    def animation(self):
        ''' タイマー設定 '''
        try:
            next_frame, wait, tag = next(self.frame)
        except:
            return
        last_insert = self.wtext.index(tk.INSERT)
        self.wtext.insert(tk.INSERT, next_frame)
        self.wtext.tag_add(tag, last_insert, tk.INSERT)
        self.wtext.see('end')
        self.after(wait, self.animation)


def cursor_animation():
    pgui.moveTo(1500, 480, duration=1)  # dock
    pgui.moveTo(1420, 480, duration=1)  # ターミナルアイコン
    sleep(0.6)
    pgui.moveTo(100, 300, duration=1)   # ターミナル画面



if __name__ == '__main__':
    thread = threading.Thread(target=cursor_animation)
    thread.start()
    sleep(4)
    terminal = Terminal()
    terminal.mainloop()
