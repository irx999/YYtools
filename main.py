
import flet as ft


from time import sleep


def main(page:ft.Page):

    # 页面大小 等控制
    page.window_center()
    page.window_width = 1200      # window's width is 200 px
    page.window_height = 800  
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

        
    def windowClosing(e):
        page.window_close()




    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.BALLOT),
        leading_width=10,
        toolbar_height = 40,
        title=ft.Text("    QVQ",),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED,on_click=theme_changed),
            ft.IconButton(ft.icons.FILTER_3),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="控件1 待开发"),
                    ft.PopupMenuItem(icon= ft.icons.OUTBOND,text="退出",checked= False,on_click = windowClosing ),
                    ft.PopupMenuItem(),  # divider 空行
                    ft.PopupMenuItem(
                        text="是否显示终端", checked=True, on_click=check_item_clicked
                    ),
                    
                ]
            ),
        ],
    )
    #################################
    


    import NavigationRail 
    NavigationRail = NavigationRail.NavigationRail(page)
    page.add(NavigationRail
        )

    sleep(3)
    page.update()






if __name__ == "__main__":
    
    # ft.app(main,view=ft.AppView.FLET_APP_HIDDEN)
    ft.app(main)
    
    