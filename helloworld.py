import tkinter as tk

fields = ["StellaNGC commands", "Receiver commands", "Main script"]

class Application(tk.Frame):
    def __init__(self, master=None):  # 构造函数
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()  # 声明对象方法，创建子组件
        self.createMenu()  # 声明对象方法，创建菜单
        self.takefile()
        root["menu"] = self.menubar  # 附加主菜单到根窗口
        root.bind("<Button-3>", self.f_popup)  # 绑定鼠标右击事件

    def createWidgets(self):
       self.f0 = tk.Frame(self, width=300, height=200, relief=tk.GROOVE, borderwidth=2)
       self.f0Label = tk.Label(self.f0, text = "Please verify the equipment connection before the test!!!")
       self.f0Label.grid()
       self.f0.grid()

       self.f1 = tk.Frame(self, width =300, height = 200, relief = tk.GROOVE, borderwidth = 5)

        # 创建StringVar对象，接收option
       self.vOption = tk.StringVar()
       self.vOption.set("Choose")  # 设置初始值为“Choose”

        # 创建关于option的radiobutton选项
       self.optionChoose = tk.Radiobutton(self.f1, text="Choose tests", value="Choose", variable=self.vOption)
       self.optionCreate = tk.Radiobutton(self.f1, text="Create new test case", value="Create", variable=self.vOption)
       self.optionChoose.grid(row=1, column=1)
       self.optionCreate.grid(row=1, column=2)

       # 创造option标签
       self.lblOption = tk.Label(self.f1, text="Options:")
       self.lblOption.grid(row=0, column=0, columnspan=1)  # option标签位置

       # 创建IntVar对象
       self.test1 = tk.IntVar()
       self.test2 = tk.IntVar()
       self.test3 = tk.IntVar()
       self.test4 = tk.IntVar()
       self.test5 = tk.IntVar()

       # 创建test 复选框
       self.checkBtnTest1 = tk.Checkbutton(self.f1, text="Scenario test", variable=self.test1)
       self.checkBtnTest2 = tk.Checkbutton(self.f1, text="trajectory test", variable=self.test2)
       self.checkBtnTest3 = tk.Checkbutton(self.f1, text="Attitude test", variable=self.test3)
       self.checkBtnTest4 = tk.Checkbutton(self.f1, text="Antenna test", variable=self.test4)
       self.checkBtnTest5 = tk.Checkbutton(self.f1, text="Other tests...", variable=self.test5)

        # tests复选框位置
       self.checkBtnTest1.grid(row=3, column=1)
       self.checkBtnTest2.grid(row=4, column=1)
       self.checkBtnTest3.grid(row=5, column=1)
       self.checkBtnTest4.grid(row=6, column=1)
       self.checkBtnTest5.grid(row=7, column=1)

       self.empty = tk.Label(self.f1, text="")
       self.empty.grid(row=9, column=0, columnspan=1)

       self.testButton = tk.Button(self.f1,text="Run tests")
       self.testButton.grid(row=10, column = 1, columnspan = 2)

       self.f1.grid()

       self.f2 = tk.Frame(self, width =400, height = 200, relief = tk.GROOVE, borderwidth = 5)

       self.resultLable = tk.Label(self.f2, text="Test result:")
       self.resultLable.grid(row=12, column=0)

       self.textarea = tk.Text(self.f2, height = 20, width = 40)
       self.textarea.grid(column = 0)

       self.saveButton = tk.Button(self.f2, text="Export test result to PDF")
       self.saveButton.grid(column=0)
       self.f2.grid()





    def createMenu(self):
        self.menubar = tk.Menu(root)  # 创建主菜单menubar
        self.menufile = tk.Menu(self.menubar)  # 创建菜单menufile
        self.menuedit = tk.Menu(self.menubar, tearoff=0)
        self.menuhelp = tk.Menu(self.menubar, tearoff=0)  # 创建菜单menuhelp
        self.menubar.add_cascade(label="File", menu=self.menufile)
        self.menubar.add_cascade(label="Edit", menu=self.menuedit)
        self.menubar.add_cascade(label="Help", menu=self.menuhelp)
        # 添加菜单项
        # 文件菜单
        self.menufile.add_command(label="New")
        self.menufile.add_command(label="Open")
        self.menufile.add_command(label="Save")
        self.menufile.add_separator()  # 分隔符
        self.menufile.add_command(label="Exit", command=root.destroy)
        # 编辑菜单
        self.menuedit.add_command(label="Cut")
        self.menuedit.add_command(label="Copy")
        self.menuedit.add_command(label="Paste")
        # 帮助菜单
        self.menuhelp.add_command(label="About")


    def f_popup(self, event):  # 弹出式菜单事件处理函数
        self.menuedit.post(event.x_root, event.y_root)  # 在鼠标右键位置显示菜单

    def takefile(self):
        global popup
        popup = tk.Toplevel()
        popup.title("Please select files:")

        entries = []
        row = tk.Frame(popup)
        for field in fields:
            lab = tk.Label(row, width=30, text=field)
            ent = tk.Entry(row)
            row.grid()
            lab.grid()
            ent.grid()
            entries.append(ent)
        popup.btn = tk.Button(popup, text = "Save this test case")
        popup.btn.grid()







root = tk.Tk()
root.geometry("400x600+100+0")
root.title("StellaNGC Test Tool")
app = Application(master=root)  # 创建Application对象实例
app.mainloop()  # 事件循环
