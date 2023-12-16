import flet as ft
from time import sleep
from main import main

def login(page:ft.Page):
    page.window_width = 300      # window's width is 200 px
    page.window_height = 450  
    page.window_always_on_top = True
    page.window_opacity = 0.95
    page.window_maximizable = True #双击是否会变大
    page.window_frameless = True
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.title = "账户验证"

    page.window_center()
    

    def textbox_changed(e):
        t.value = "hello , " + e.control.value
        page.update()
        
    def login_authentication(e):
        print(username.value,password.value)
        if username.value == "123" and password.value =="123":
            print("密码正确,qvq")
            
            page.window_visible = False
            page.update()
            # 主程序启动
            ft.app(main)
            page.window_close()
        
        else:
            t.value = "密码错误, " + username.value
            page.update()

    t  = ft.Text(
            "Welcome, Please login in",
            size=40,)
           
    username  = ft.TextField(
        label="账户名:",
        on_change=textbox_changed,)

    password = ft.TextField(
            label="Enter-Your-pin", password=True, can_reveal_password=True
        )
    login_bt =  ft.ElevatedButton(text="log in",on_click= login_authentication,)

    #登录页面定义
    page.add(ft.Column(
        [t,username,password,
         ft.Row([login_bt],alignment=ft.MainAxisAlignment.CENTER)]
         )
        )
    
    return page
    
    

if __name__ == "__main__":
    ft.app(login,)