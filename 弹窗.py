import tkinter as tk
import random
import time


def show_warm_tip():
    # 创建窗口
    window = tk.Tk()
    # 获取屏幕宽高
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # 随机窗口位置
    window_width = 322
    window_height = 120
    x = random.randrange(0, screen_width - window_width)
    y = random.randrange(0, screen_height - window_height)
    # 窗口标题和大小位置
    window.title("宝宝宝宝！")
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # 文字列表
    tips = ['我想你了','很想', '今天过得开心嘛', '见面', '顺顺利利', '早点休息', '天冷添衣', '有想我嘛',
            '想和你一起吃糖炒板栗','烤红薯也好吃','你好厉害','宝宝 你好厉害','宝宝你好厉害','你好厉害',
            '我爱你','你要想我','在干嘛','我要抱抱','记得喝水','摸摸我','我想打电话','好想你','我爱你,好爱你',
            '我在','你最好了','我买了新茶','最近有新出的好吃的','什么时候有空？','宝宝','； ；','我给你买了','给你寄了东西',
            '我记得的，你说过','我爱你我爱你我爱你','想听你的声音','你好厉害','你好厉害','你好厉害','你好厉害',
            '我在努力，你等等我','宝宝你好棒','宝宝你好厉害','宝宝，你是最棒的','宝宝，你就是最棒的','宝宝，你是最棒的','宝宝，你是最棒的',
            '🥺🥺🥺','我准备了！','想和你共享同一份气息','明天见！','如何别后，三换梅枝','贴贴',
            '宝宝你好棒','宝宝你好棒','宝宝你好棒','宝宝你好棒','宝宝你好棒','宝宝 你好棒','宝宝你好棒','宝宝你好棒',
            '我只要你，是你就要','你要开心，别的不怕','不要惧，我和你一起','会是春风吹又生','我和你','想你想的晕乎乎的',
            '我一直在爱你呀','钻你被窝！','好喜欢你','我在的我在的我在的！','宝宝 有你真好','mua','ლ(°◕‵ƹ′◕ლ)',]
    tip = random.choice(tips)

    # 多样的背景颜色
    bg_colors = ['lavender', 'violet', 'plum', 'light pink', 'pink', 'coral', 'peach puff',
                 'misty rose', 'hot pink', 'light salmon', 'orange', 'light coral', 'thistle',
                 'orchid','pale violet red', 'deep pink', 'salmon','tomato', 'dark orange']
    bg = random.choice(bg_colors)

    # 创建标签，显示文字
    tk.Label(
        window,
        text=tip,
        bg=bg,
        font=('微软雅黑', 34),
        width=30,
        height=3
    ).pack()

    # 窗口置顶显示
    window.attributes('-topmost', True)

    # 10秒后自动关闭窗口
    window.after(10000, window.destroy)

    return window


def main():
    windows = []

    for i in range(300):
        try:
            window = show_warm_tip()
            windows.append(window)
            window.update()
            time.sleep(0.0029)
        except Exception as e:
            print(f"创建窗口时出错: {e}")
            continue

    # 启动主循环
    try:
        windows[0].mainloop() if windows else None
    except:
        pass


if __name__ == "__main__":
    main()