"""
程序主入口
"""
from video_converter import convert_to_text
import os, sys


if sys.version_info[0] == 2:
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    # Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    import tkFileDialog
    import tkSimpleDialog
else:  #Python 3.x
    from tkinter import *
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    import tkinter.filedialog as tkFileDialog
    import tkinter.simpledialog as tkSimpleDialog    #askstring()


if __name__ == '__main__':
    try:
        # 输入目标文件路径 for_example: r'/Users/xx/xxx.mp4'
        print("选择需要转换的视频文件")
        file_path = tkFileDialog.askopenfilename(title=u'选择需要转换的视频文件', filetypes=(
            ("MP4 Files", "*.mp4"), ("all files", "*.*")))
        print("已经选取文件：【%s】"%file_path)
        if file_path==None:
            if not os.path.exists(file_path):
                print("文件不存在，请重新选择！")
            print("文件异常，请重新选择！")
        else:
            source_media_path =file_path
            convert_to_text(source_media_path=source_media_path)
    except Exception as e:
        print(str(e))