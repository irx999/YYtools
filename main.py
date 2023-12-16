
import flet as ft


from time import sleep


def main(page:ft.Page):

    # 页面大小 等控制
    page.window_center()
    page.window_width = 1200      # window's width is 200 px
    page.window_height = 800  
    page.window_always_on_top = False
    page.window_opacity = 1
    page.window_maximizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_frameless = False

    page.title = "运营工具箱V0.0.1.1"



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




    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.BALLOT),
        leading_width=10,
        toolbar_height = 40,
        title=ft.Text("    QVQ",),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED,on_click=theme_changed),
            ft.IconButton(icon = ft.icons.MINIMIZE_SHARP,on_click=lambda __: (setattr(page, 'window_minimized', True), page.update())),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="待开发",icon=ft.icons.CODE_OFF_OUTLINED),
                    ft.PopupMenuItem(text="待开发",icon=ft.icons.CODE_OFF_OUTLINED),
                    ft.PopupMenuItem(text="待开发",icon=ft.icons.CODE_OFF_OUTLINED),
                    ft.PopupMenuItem(text="待开发",icon=ft.icons.CODE_OFF_OUTLINED),
                    ft.PopupMenuItem(icon= ft.icons.CLOSE,text="退出",checked= False,on_click = lambda __: page.window_destroy() ),
                    ft.PopupMenuItem(),  # divider 空行
                    ft.PopupMenuItem(
                        text="是否显示终端", checked=True, on_click=check_item_clicked
                    ),
                    
                ],icon=ft.icons.FILTER_3
            ),
            ft.IconButton(icon= ft.icons.CLOSE,on_click = lambda __: page.window_destroy() ),
        ],
    )






    #退出确认框

    def window_event(e):
        if e.data == "close":
            page.dialog = confirm_dialog
            confirm_dialog.open = True
            page.update()

    page.window_prevent_close = True
    page.on_window_event = window_event

    def yes_click(e):
        page.window_destroy()

    def no_click(e):
        confirm_dialog.open = False
        page.update()

    confirm_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you really want to exit this app?"),
        actions=[
            ft.ElevatedButton("Yes", on_click=yes_click),
            ft.OutlinedButton("No", on_click=no_click),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    #################################
    


    import NavigationRail 
    NavigationRail = NavigationRail.NavigationRail(page)
    page.add(NavigationRail
        )
    page.show_banner





if __name__ == "__main__":
    
    # ft.app(main,view=ft.AppView.FLET_APP_HIDDEN)
    ft.app(main)
    