import tkinter as tk
from nltk.chat.util import Chat, reflections
def tokenize_chinese(text):
    return text.split()
pairs = [
    [
        '(你好|您好)',
        ['你好!', '您好!', '你好啊!']
    ],
    [
        '(你叫什么名字|你是谁)', 
        ['我是一个聊天机器人。', '你可以叫我聊天机器人。']
    ],
    [
        '(.*) 你的名字?', 
        ['我的名字是Chatbot。']
    ],
    [
        '(.*) 帮助 (.*)', 
        ['我可以帮助你的。']
    ],
    [
        '(.*) 位置 ?', 
        ['我是一个虚拟助手，我无处不在。']
    ],
    [
        '再见', 
        ['再见!', '拜拜!', '祝你好运!']
    ],
    [
        '一加一',
        ['2']
    ],
    [
        '一加二',
        ['3']
    ],
    [
        '一加三',
        ['4']
    ],
    [
        '一加四',
        ['5']
    ],
    [
        '一加五',
        ['6']
    ],
    [
        '一加六',
        ['7']
    ],
    [
        '一加七',
        ['8']
    ],
    [
        '一加八',
        ['9']
    ],
    [
        '一加九',
        ['10']
    ],
    #================================
        [
        '二加一',
        ['3']
    ],
    [
        '二加二',
        ['4']
    ],
    [
        '二加三',
        ['5']
    ],
    [
        '二加四',
        ['6']
    ],
    [
        '二加五',
        ['7']
    ],
    [
        '二加六',
        ['8']
    ],
    [
        '二加七',
        ['9']
    ],
    [
        '二加八',
        ['10']
    ],
    [
        '二加九',
        ['11']
    ],
    #==========================
    [
        '三加一',
        ['4']
    ],
    [
        '三加二',
        ['5']
    ],
    [
        '三加三',
        ['6']
    ],
    [
        '三加四',
        ['7']
    ],
    [
        '三加五',
        ['8']
    ],
    [
        '三加六',
        ['9']
    ],
    [
        '三加七',
        ['10']
    ],
    [
        '三加八',
        ['11']
    ],
    [
        '三加九',
        ['12']
    ],
    [
        '四加一',
        ['5']
    ],
    [
        '四加二',
        ['6']
    ],
    [
        '四加三',
        ['7']
    ],
    [
        '四加四',
        ['8']
    ],
    [
        '四加五',
        ['9']
    ],
    [
        '四加六',
        ['10']
    ],
    [
        '四加七',
        ['11']
    ],
    [
        '四加八',
        ['12']
    ],
    [
        '四加九',
        ['13']
    ],
]


def chatbot_response(user_input):
    chat = Chat(pairs, reflections)
    response = chat.respond(user_input)
    return response if response else '\n对不起，我不知道,请尝试以下方法：\n1.如果你要问我算式请问10以内的算式,如:一加一（一定要问中文\n2.我的模型不支持请换一个问题吧。'

def send_message(event=None):
    user_input = entry.get()
    if user_input.lower() == '退出':
        messages.insert(tk.END, "Chatbot: 再见!")
        entry.delete(0, tk.END)
        exit()
    else:
        messages.insert(tk.END, "你: " + user_input+'\n')
        response = chatbot_response(user_input)
        messages.insert(tk.END, "Chatbot: " + response+'\n')
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("中文聊天机器人")
'''
bg_image = tk.PhotoImage(file="衢塘绘画AI_1711000685912.png")

# 创建一个标签，将图片作为背景
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
'''
frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

messages = tk.Text(frame, width=80, height=20)
messages.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=messages.yview)

entry = tk.Entry(root, width=80)
entry.pack(pady=10)

send_button = tk.Button(root, text="发送", command=send_message)
send_button.pack()

entry.bind("<Return>", send_message)

messages.insert(tk.END, "Chatbot: 你好！我是一个中文聊天机器人。有什么可以帮助你的吗？\n")

root.mainloop()
