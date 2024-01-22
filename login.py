import flet as ft
from time import sleep
from main import main
import hashlib,requests

def login(page:ft.Page):
    page.window_width = 300      # window's width is 200 px
    page.window_height = 450  
    page.window_always_on_top = True
    page.window_opacity = 0.95
    page.window_maximizable = True #双击是否会变大
    page.window_frameless = True
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_center()
    page.title = "账户验证"
    

    

    #键盘事件
    def on_keyboard(e: ft.KeyboardEvent):
        
        if e.key =="Enter":
            login_authentication(e)
        elif e.key == "ESC":
            page.window_destroy()
            print("退出")
            
            
            
            

    page.on_keyboard_event = on_keyboard
    

    def textbox_changed(e):
        t.value = "hello , " + e.control.value
        page.update()
    # 密码验证
    def generate_md5_hash(password):
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        return md5.hexdigest()
        
    def login_authentication(e):
        loading.visible = True
        page.update()
        true_pw = requests.get("https://irx999.fun/pw.php").text.replace("\n","")
        pw = str(username.value+password.value)
        input_pw = str(generate_md5_hash(pw))
        sleep(0.5)
        loading.visible = False
        page.update()
        
    
        if  input_pw==true_pw:
            loading2.visible = True
            page.update()
            sleep(0.3)
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
    out_bt = ft.ElevatedButton(text="leave",on_click= lambda __ : page.window_destroy(),)

    loading = ft.ProgressBar(width=400, color="blue", bgcolor="#eeeeee")
    loading2 = ft.ProgressRing()

    
    import subprocess

    def install_packages(package_list):
        subprocess.check_call(["pip", "install"] + package_list)

    # 要安装的包的列表
    packages_to_install = ["wakeonlan"]

    def update_packages(e):

        loading.visible = True
        page.update()
        try:
            install_packages(packages_to_install)
            
            Updatebutton.visible =False

        except Exception as e :
            t.value = f"更新失败 {e}"
            loading.visible = False
            
        finally:
            page.update()

        
        



    # 安装多个包
    

    
    Updatebutton = ft.ElevatedButton("检测到缺失部件,请更新",icon="WEBHOOK_OUTLINED",icon_color="red400",on_click=update_packages)
    Updatebutton.visible = False

    try:
        import  wakeonlan
    except:
        Updatebutton.visible = True
        page.update()






    #登录页面定义
    loading.visible = False
    loading2.visible = False
    page.add(ft.Column(
        [t,username,password,
         ft.Row([login_bt,out_bt],alignment=ft.MainAxisAlignment.CENTER),
         ft.Row([loading,loading2],alignment=ft.MainAxisAlignment.CENTER),
         ft.Row([Updatebutton],alignment= ft.MainAxisAlignment.CENTER)

         ]
         )
        )
    
    return page
    
    

if __name__ == "__main__":
    ft.app(login,)