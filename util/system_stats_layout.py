    stop_event = threading.Event()
    
system_stats_layout = [
        [
            sg.Frame('',[ 
                [
                    sg.Frame('',[ 
         
                        [
                            sg.Button("CPU Usage",size=(15,2),font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),disabled=True),
                            sg.Button("",key=SYSTEM_STATS_CPU_USAGE_PRECENT_LBL_KEY,size=(40,2),font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),disabled=True),
                        ],                         
                        [
                            sg.Button("RAM Usage",size=(15,2),font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),disabled=True),        
                            sg.Button("",key=SYSTEM_STATS_RAM_USAGE_LBL_KEY,size=(40,2),font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),disabled=True),
                        ],                                     
                    ],expand_x=True,expand_y=False,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="c",background_color=color.DARK_GRAY)
                ],                                  
            ], expand_x=True, expand_y=False, border_width=5, pad=(10,10), relief=sg.RELIEF_FLAT, element_justification="c", background_color=color.DARK_GRAY)
        ],  
    ]

    # gpu_stats = system_stats.get_gpu_stats()
    # for i, gpu_stat in enumerate(gpu_stats):
    #     system_stats_tab_column.append([
    #         sg.Frame('',[
    #             [
    #                 sg.Text(gpu_stat['name'], key=f"-{SYSTEM_STATS_GPU_NAME_LBL_KEY}_{i}-", font=FONT_H1, background_color=color.DARK_GRAY, text_color=color.LIGHT_GRAY),
    #             ],
    #             [
    #                 sg.Frame("",[       
    #                         [
    #                             sg.Button("Temperature",size=(15,2),font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),disabled=True),
            
    #                             sg.Button('', key=f"-{SYSTEM_STATS_GPU_TEMP_LBL_KEY}_{i}-",size=(40,2),font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),disabled=True),
    #                         ], 
    #                         [
    #                             sg.Button("VRAM Usage",size=(15,2),font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),disabled=True),
    #                             sg.Button(f"",size=(40,2), key=f"-{SYSTEM_STATS_GPU_VRAM_LBL_KEY}_{i}-",font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),disabled=True),
    #                         ],                                 
    #                         [
    #                             sg.Button("Power Usage",size=(15,2),font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),disabled=True),
            
    #                             sg.Button(f"",size=(40,2), key=f"-{SYSTEM_STATS_GPU_POWER_USAGE_LBL_KEY}_{i}-",font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),disabled=True),
    #                         ],                              
    #                     ],expand_x=True,expand_y=True,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)
    #             ]
    #         ], expand_x=True, expand_y=False, border_width=5, pad=(10,10), relief=sg.RELIEF_FLAT, element_justification="c", background_color=color.DARK_GRAY)
    #     ])



    
    def system_stats_monitor(stop_event,update_interval=1):
            while not stop_event.is_set():
                window[SYSTEM_STATS_CPU_USAGE_PRECENT_LBL_KEY].update(f"{system_stats_layout.get_cpu_stats()['cpu_percent']} %")
                window[SYSTEM_STATS_RAM_USAGE_LBL_KEY].update(f"{system_stats_layout.get_ram_stats()['ram_used']} / {system_stats_layout.get_ram_stats()['ram_total']}") 
                for i, gpu_stat in enumerate(system_stats_layout.get_gpu_stats()):
                    window[f"-{SYSTEM_STATS_GPU_NAME_LBL_KEY}_{i}-"].update(gpu_stat['name'])
                    window[f"-{SYSTEM_STATS_GPU_TEMP_LBL_KEY}_{i}-"].update(f"{gpu_stat['temperature']} °C")
                    window[f"-{SYSTEM_STATS_GPU_POWER_USAGE_LBL_KEY}_{i}-"].update(f"{gpu_stat['power_usage']:.2f} / {gpu_stat['card_power']:.2f}  W")
                    window[f"-{SYSTEM_STATS_GPU_VRAM_LBL_KEY}_{i}-"].update(f"{gpu_stat['vram_used']} / {gpu_stat['vram_total']}")            
                time.sleep(update_interval)
