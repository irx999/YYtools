
import flet as ft

name = "NavigationRail Example"

def NavigationRail():

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=200,
        leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="First"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                label="Second",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Settings"),
            ),
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )

    # return ft.Row(
    #         [
    #             rail,
    #             ft.VerticalDivider(width=1),
    #             ft.Column([ ft.Text("Body!")], alignment=ft.MainAxisAlignment.START, expand=True),
    #         ],
    #         expand=True,
    #     )


    return    ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1)
               
            ],
            expand=True,
            alignment= ft.alignment.center_left
        )
    
