from tkinter import *
import time,datetime
class A():
    def __init__(self):
        global b,f,result,list
        self.hl=Tk()
        self.hl.geometry('800x600')
        self.hl.title('身份验证系统')
        self.hl['bg'] = 'lightblue'

        self.image = PhotoImage(file='校验.png')
        self.a=Label(self.hl,image=self.image)
        self.a.place(x=10,y=10)

        self.b=Label(self.hl,text='请输入身份证号码：',font=('微软雅黑',14,'bold'),bg='navy',fg='lightblue')
        self.b.place(x=380,y=20,width=200)

        self.c=Entry(self.hl,font=('微软雅黑',15,'bold'))
        self.c.place(x=380,y=58,width=270,height=30)

        self.d=Button(self.hl,text='校验',font=('微软雅黑',9,'bold'),fg='navy',command=self.jiaoyan)
        self.d.place(x=660,y=58,width=60)

        self.e = Label(self.hl, text='是否有效：', font=('微软雅黑', 14, 'bold'), fg="navy", bg="lightblue")
        self.e.place(x=380, y=150)

        self.result=StringVar()
        self.result.set('')
        self.f = Entry(self.hl,state=DISABLED,textvariable=self.result,font=('微软雅黑', 14, 'bold'))
        self.f.place(x=480, y=153,height=25,width=90)

        self.g = Label(self.hl, text='      性别：', font=('微软雅黑', 14, 'bold'), fg="navy", bg="lightblue")
        self.g.place(x=380, y=210)

        self.result2=StringVar()
        self.result2.set('')
        self.h= Entry(self.hl, state=DISABLED, font=('微软雅黑', 14, 'bold'),textvariable=self.result2)
        self.h.place(x=480, y=213, height=25, width=90)

        self.i= Label(self.hl, text='出生日期：', font=('微软雅黑', 14, 'bold'), fg="navy", bg="lightblue")
        self.i.place(x=380, y=270)

        self.result3=StringVar()
        self.result3.set('')
        self.j= Entry(self.hl, state=DISABLED, font=('微软雅黑', 14, 'bold'),textvariable=self.result3)
        self.j.place(x=480, y=273, height=25, width=210)

        self.k = Label(self.hl, text='   所在地：', font=('微软雅黑', 14, 'bold'), fg="navy", bg="lightblue")
        self.k.place(x=381, y=330)

        self.result4=StringVar()
        self.result4.set('')
        self.l = Entry(self.hl, state=DISABLED, font=('微软雅黑', 14, 'bold'),textvariable=self.result4)
        self.l.place(x=480, y=333, height=25, width=210)

        self.d = Button(self.hl, text='关闭', font=('微软雅黑', 9, 'bold'), fg='navy',command=self.close)
        self.d.place(x=660, y=400, width=60,height=30)

    def jiaoyan(self):
        list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'X']
        aa = self.c.get()

        try:
            end = aa[-1]
            number = aa[0:17]
            xishu_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
            duiying_number = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
            sum = 0
            for index in range(len(number)):
                sum += int(number[index]) * int(xishu_list[index])

            remainder = sum % 11
            end_num = duiying_number[remainder]

            for i in aa:
                if i in list and len(aa) == 18 and end_num == end:
                    year = aa[6:10]
                    month = aa[10:12]
                    day = aa[12:14]
                    sex = aa[16]

                    try:
                        file = open('身份证归属地.txt', mode='r',encoding='utf-8')
                        text = file.readlines()
                        family = aa[:6]
                        for i in text:
                            if family in i:
                                self.result4.set(i[9:])
                                break
                            continue
                        else:
                            year = 0
                        b = time.mktime(datetime.datetime(int(year), int(month), int(day)).timetuple())
                        y = time.mktime(datetime.datetime(1970, 1, 1, 8, 00).timetuple())
                        x = time.time()
                        if b >= y and b <= x:
                            self.result.set('有效')
                            self.result3.set("%s-%s-%s"%(year,month,day))
                            if int(sex) % 2 == 0:
                                self.result2.set('女')
                            else:
                                self.result2.set('男')
                        else:
                            self.result.set('无效')
                            self.result2.set("")
                            self.result3.set("")
                            self.result4.set("")
                    except:
                        self.result.set('无效')
                        self.result2.set("")
                        self.result3.set("")
                        self.result4.set("")
                else:
                    self.result.set('无效')
                    self.result2.set("")
                    self.result3.set("")
                    self.result4.set("")
        except:
            self.result.set('无效')
            self.result2.set("")
            self.result3.set("")
            self.result4.set("")

    def close(self):
        self.hl.destroy()

    def show(self):
        self.hl.mainloop()

if __name__ == '__main__':
    long = A()
    long.show()