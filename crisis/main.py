from __future__ import print_function, unicode_literals, absolute_import
from threading import *
import subprocess
import json
import tempfile
import asyncio
import os
from os.path import exists

#flet imports
import flet as ft
#from file import class

def main(page: ft.Page):

    topInfo = ft.Column(scroll='auto', height = 300)
    for i in range(10):
        infoCard = ft.Container(
            border_radius=20,
            bgcolor=ft.colors.BLACK,
            height=100,
            width=350,
            padding=15,
            #on_click=lambda _: page.go('/ActivityManagerView'),
            content=ft.Column(
                controls=[
                    ft.Text(value="top", color=ft.colors.WHITE, size=15, weight=ft.FontWeight.W_100, height = 20),
                    ft.Container(width = 320, height = 2, border_radius = 5, bgcolor = ft.colors.BLUE),
                    ft.Text(value="bot", color=ft.colors.WHITE, size=12, italic = True, height = 15, width = 100),
                ]
            )
        )
    topInfo.controls.append(infoCard)

    FirstScreen = ft.Column(alignment='end',
                      controls=[
                          ft.Container(
                              width=400,
                              height=850,
                              bgcolor=ft.colors.WHITE,
                              border_radius=35,
                              animate=ft.animation.Animation(600, ft.AnimationCurve.DECELERATE),
                              animate_scale=ft.animation.Animation(400, curve='decelerate'),
                              padding=ft.padding.only(top=50, left=20, right=20, bottom=5),
                              content=ft.Column(
                                  controls=[
                                        ft.IconButton(
                                            icon = ft.icons.ARROW_BACK, 
                                            icon_color=ft.colors.BLACK, 
                                            icon_size=24,
                                            on_click = lambda _: page.go('/'),
                                            tooltip = "Go Back"),
                                        #class()
                                  ]
                              )
                          ), 
                      ]
                    )

    #Animate to the host screen
    buffer = ft.Container(width = 1)
    Host = ft.Column(alignment='end',
                      controls=[
                          ft.Container(
                              width=400,
                              height=850,
                              bgcolor=ft.colors.WHITE,
                              border_radius=35,
                              animate=ft.animation.Animation(600, ft.AnimationCurve.DECELERATE),
                              animate_scale=ft.animation.Animation(400, curve='decelerate'),
                              padding=ft.padding.only(top=50, left=20, right=20, bottom=5),
                              content=ft.Column(
                                  controls=[
                                    ft.Row(alignment='spaceBetween', width = 360,
                                        controls=[
                                                ft.IconButton(icon = ft.icons.DIRECTIONS_RUN, 
                                                    icon_color=ft.colors.BLACK, 
                                                    tooltip = "Screen 1",
                                                    on_click = lambda _: page.go('/ScreenOne')),
                                                ft.Row(alignment='center',
                                                    controls=[
                                                        ft.Row(alignment='center',
                                                                controls=[
                                                                ],
                                                                ),
                                                    ],
                                                    ),
                                        ],
                                        ),
                                      topInfo,
                                      #classes
                                      
                                    ]
                                )
                            ),     
                        ]
                    )
    #Construct the app
    Layout = ft.Container(
        width=400,
        height=850,
        bgcolor=ft.colors.WHITE,
        border_radius=35,
        content=ft.Stack(
            controls=[
                Host,
            ]
        )
    )

    global pages
    pages = {
        '/': ft.View(
            "/",
            [
                Host
            ]
        ),
        '/ScreenOne': ft.View(
            "/ScreenOne",
            [
                FirstScreen
            ]
        ),
        #'/EmailAndFrequencyView': ft.View(
         #   "/EmailAndFrequencyView",
          #  [
           #     EmailAndFrequency
            #]
        #),
    }

    # Transfer page function
    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )

    # Setup
    page.title = "UCrisus"
    page.on_route_change = route_change
    page.go(page.route)
    page.add(Layout)



ft.app(main)
