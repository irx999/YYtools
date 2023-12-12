
import flet as ft
import NavigationRail 
NavigationRail = NavigationRail.NavigationRail()



def login(page:ft.Page):
    page.window_width = 300      # window's width is 200 px
    page.window_height = 450  
    page.window_always_on_top = True
    page.window_opacity = 0.95
    page.window_maximizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_center()

    page.title = "账户验证"
    

    def textbox_changed(e):
        t.value = "hello , " + e.control.value
        page.update()
        
    def login_bt_1(e):
        print(username.value,password.value)
        if username.value == "123" and password.value =="123":
            print("密码正确")
            main.page.window_visible = True

    t  = ft.Text(
            "Welcome, Please login in",
            size=40, )
           
    username  = ft.TextField(
        label="账户名:",
        on_change=textbox_changed,
    )

    password = ft.TextField(
            label="Enter-Your-pin", password=True, can_reveal_password=True
        )
    login_bt =  ft.ElevatedButton(text="Elevated button",on_click= login_bt_1)
    page.add(ft.Column([t,username,password,login_bt],alignment=ft)
        )
    
    
    page.update()

def main(page:ft.Page):

    # 页面大小 等控制
    page.window_width = 800      # window's width is 200 px
    page.window_height = 500  
    page.window_always_on_top = True
    page.window_opacity = 1
    page.window_maximizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.title = "运营工具箱V0.0.1"



    page.fonts = {
        "Roboto Mono": "RobotoMono-VariableFont_wght.ttf",
    }
    # 主题切换
    def theme_changed(e):
        page.theme_mode = (
        ft.ThemeMode.DARK
            if page.theme_mode ==ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        c.label = (
            "Light theme" if page.theme_mode ==ft.ThemeMode.LIGHT else "Dark theme"
        )
        page.update()
    c =ft.Switch(label="Light theme", on_change=theme_changed)
    page.theme_mode =ft.ThemeMode.LIGHT

    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        print("终端待开发")
        page.update()




    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.BALLOT),
        leading_width=10,
        toolbar_height = 40,
        title=ft.Text("━━(￣ー￣*|||━━",),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED,on_click=theme_changed),
            ft.IconButton(ft.icons.FILTER_3),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="控件1 代开发"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="是否显示终端", checked=True, on_click=check_item_clicked
                    ),
                ]
            ),
        ],
    )
    #################################
    



    page.add(NavigationRail
        )

    






if __name__ == "__main__":
    
    ft.app(main,)
    
    