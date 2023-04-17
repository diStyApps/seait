projects_data = [
        {
            "id": 1,
            "key": "app_",
            "image_path": b'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',
            "title": "Automatic1111 webui",
            "repo_name": "stable-diffusion-webui",
            "github_url": "https://github.com/AUTOMATIC1111/stable-diffusion-webui",
            "git_clone_url":"https://github.com/AUTOMATIC1111/stable-diffusion-webui.git",
            "installed_version": "-",
            "available_version": "-",
            "installed": True,
            "visible":True,
            "status": 1,
            "isIncomplete": False,
            "type": "app",
            "install_requirements":False,
            "install_cuda":False,
            "install_instructions_available":False,
            "install_instructions": [
            ],            
            "entry_point": 
                {
                    "install":"launch.py",
                    "launch":"launch.py",
                },  
            "buttons": [
                {
                    "button_text": "Update",
                    "key": "update",
                },
                {
                    "button_text": "Delete venv",
                    "key": "delete_venv",
                },
                {
                    "button_text": "Create venv",
                    "key": "create_venv",
                },                        
                {
                    "button_text": "Uninstall",
                    "key": "uninstall",
                },                                               
            ],
            "launch_buttons": [
                {
                    "button_text": "Launch",
                    "key": "launch",
                },           
                {
                    "button_text": "Install",
                    "key": "install",
                },                                               
            ],            
            "args": [
                [
                    {
                        "button_text": "--autolaunch",
                        "key": "autolaunch",
                    },  

                    {
                        "button_text": "--theme=dark",
                    },
                ],   
                [
                    {
                        "button_text": "--nowebui",
                        "key": "nowebui",
                    },    
                    {
                        "button_text": "--no-half",
                    }                      
                ],

                [
                    {
                        "button_text": "--force-enable-xformers",
                        "key": "force-enable-xformers",
                    },
                    {
                        "button_text": "--xformers",
                        "key": "xformers",
                    },
                ],                
                [
                    {
                        "button_text": "--lowvram",
                        "key": "lowvram",
                    },
                    {
                        "button_text": "--medvram",
                        "key": "medvram",
                    },
                    {
                        "button_text": "--lowram",
                        "key": "lowram",
                    },
                ],
                [
                    {
                        "button_text": "--share",
                        "key": "share",
                    },
                    {
                        "button_text": "--listen",
                        "key": "listen",
                    },

                    {
                        "button_text": "--api",
                        "key": "api",
                    },                    
                ],            
                [
                    {
                        "button_text": "--enable-insecure-extension-access",
                    },
                    {
                        "button_text": "--skip-version-check",
                    },                    
                ]
            ],
            "def_args": [
                       "--autolaunch",
                       "--theme=dark",
            ],               
            "description":[]     
        },
        {
            "id": 2,
            "key": "app_",
            "image_path": b'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',
            "title": "InvokeAI",
            "repo_name": "InvokeAI",
            "github_url": "https://github.com/invoke-ai/InvokeAI",
            "git_clone_url":"https://github.com/invoke-ai/InvokeAI.git",
            "installed_version": "-",
            "available_version": "-",
            "installed": False,
            "visible":True,
            "status": 1,
            "isIncomplete": False,
            "type": "app",
            "install_requirements":False,
            "install_cuda":False,
            "install_instructions_available":True,
            "install_instructions": [
                '-m pip install InvokeAI[xformers] --use-pep517 --extra-index-url https://download.pytorch.org/whl/cu117',
            ],
 
            "entry_point": 
            {
                "install":"invokeai-configure",
                "launch":"invokeai",
            },                      
            "buttons": [
                {
                    "button_text": "Update",
                    "key": "update",
                },
                {
                    "button_text": "Delete venv",
                    "key": "delete_venv",
                },
                {
                    "button_text": "Create venv",
                    "key": "create_venv",
                },                        
                {
                    "button_text": "Uninstall",
                    "key": "uninstall",
                },                                              
            ],
            "launch_buttons": [
                {
                    "button_text": "Launch",
                    "key": "launch",
                },    
                {
                    "button_text": "Install",
                    "key": "install",
                },                                                           
            ],            
            "args": [
                [
                    {
                        "button_text": "--web",
                        "key": "web",
                    },                                                          
                ],      
                [
                    {
                        "button_text": "--internet",
                        "key": "internet",
                    },  
                    {
                        "button_text": "--no-internet",
                        "key": "no-internet",
                    },                                                           
                ],    
                [        
                    {
                        "button_text": "--nsfw_checker",
                        "key": "nsfw_checker",
                    },  
                    {
                        "button_text": "--no-nsfw_checker",
                        "key": "no-nsfw_checker",
                    },                                                    
                ],   
                [        
                    {
                        "button_text": "--safety_checker",
                        "key": "safety_checker",
                    },  
                    {
                        "button_text": "--no-safety_checker",
                        "key": "no-safety_checker",
                    },                                                    
                ],  
                [        
                    {
                        "button_text": "--web",
                        "key": "embeddings",
                    },  
                    {
                        "button_text": "--no-embeddings",
                        "key": "no-embeddings",
                    },                                                    
                ],

            ],
            "def_args": [
                    "--web",
            ],               
            "description":[]     
                                      
        },    
        {
            "id": 3,
            "key": "app_",
            "image_path": b'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',
            "title": "ComfyUI",
            "repo_name": "ComfyUI",
            "github_url": "https://github.com/comfyanonymous/ComfyUI",
            "git_clone_url":"https://github.com/comfyanonymous/ComfyUI.git",
            "installed_version": "-",
            "available_version": "-",
            "installed": False,
            "visible":True,
            "status": 1,
            "isIncomplete": False,
            "type": "app",
            "install_requirements":True,
            "install_cuda":True,
            "install_instructions_available":False,
            "install_instructions": [
            ],              
            "download_models_path": "https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors",
            "checkpoints_path": "models\checkpoints",
            "entry_point": 
            {
                "install":"main.py",
                "launch":"main.py",
            },                      
            "buttons": [
                {
                    "button_text": "Update",
                    "key": "update",
                },
                {
                    "button_text": "Delete venv",
                    "key": "delete_venv",
                },
                {
                    "button_text": "Create venv",
                    "key": "create_venv",
                },                        
                {
                    "button_text": "Uninstall",
                    "key": "uninstall",
                },                                              
            ],
            "launch_buttons": [
                {
                    "button_text": "Launch",
                    "key": "launch",
                },    
                {
                    "button_text": "Install",
                    "key": "install",
                },                                                           
            ],            
            "args": [
                [
                    {
                        "button_text": "--normalvram",
                        "key": "normalvram",
                    },
                    {
                        "button_text": "--listen",
                        "key": "listen",
                    },                   
                ],               
            ],
            "def_args": [                  
            ],               
            "description":[]     
                                       
        },            
        {
            "id": 4,
            "key": "app_",
            "image_path": b'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',
            "title": "Kohya's GUI",
            "repo_name": "kohya_ss",
            "github_url": "https://github.com/bmaltais/kohya_ss",
            "git_clone_url":"https://github.com/bmaltais/kohya_ss.git",
            "installed_version": "-",
            "available_version": "-",
            "installed": False,
            "visible":True,
            "status": 1,
            "isIncomplete": False,
            "type": "app",
            "install_requirements":False,
            "install_cuda":False,
            "install_instructions_available":False,
            "install_instructions": [
            ],              
            "download_models_path": "https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors",
            "checkpoints_path": "models\checkpoints",
            "entry_point": 
            {
                "install":"setup.bat",
                "launch":"gui.bat",
            },                      
            "buttons": [
                {
                    "button_text": "Update",
                    "key": "update",
                },
                {
                    "button_text": "Delete venv",
                    "key": "delete_venv",
                },
                {
                    "button_text": "Create venv",
                    "key": "create_venv",
                },                        
                {
                    "button_text": "Uninstall",
                    "key": "uninstall",
                },                                              
            ],
            "launch_buttons": [
                {
                    "button_text": "Launch",
                    "key": "launch",
                },     
                {
                    "button_text": "Install",
                    "key": "install",
                },                                                          
            ],            
            "args": [
                [
                    {
                        "button_text": "--inbrowser",
                        "key": "inbrowser",
                    },
                    {
                        "button_text": "--share",
                        "key": "share",
                    },                    
                ],               
            ],
            "def_args": [
                "--inbrowser",
            ],               
            "description":[]     
                                      
        },         
        {
            "id": 5,
            "key": "app_",
            "image_path": b'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',
            "title": "Controlnet - auto1111 extension",
            "repo_name": "sd-webui-controlnet",
            "github_url": "https://github.com/Mikubill/sd-webui-controlnet",
            "git_clone_url":"https://github.com/Mikubill/sd-webui-controlnet.git",
            "installed_version": "-",
            "available_version": "-",
            "installed": False,
            "visible":True,
            "status": 1,
            "isIncomplete": False,
            "type": "webui_extension",
            "webui_path": "stable-diffusion-webui",
            "models_path": "https://huggingface.co/datasets/disty/seait_ControlNet-modules-safetensors",
            "buttons": [                     
                {
                    "button_text": "Download Models",
                    "key": "download_models",
                },                       
                {
                    "button_text": "Uninstall",
                    "key": "uninstall_webui_extension",
                },                                              
            ],
            "launch_buttons": [
                {
                    "button_text": "Update",
                    "key": "update_webui_extension",
                },                                                           
                {
                    "button_text": "Install",
                    "key": "install_webui_extension",
                },  
            ],
            "args": [                                               
            ],    
            "def_args": [
            ],               
            "description":[]     
                                                                
        },  
        {
            "id": 6,
            "key": "app_",
            "image_path": b'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',
            "title": "Dreambooth - auto1111 extension",
            "repo_name": "sd_dreambooth_extension",
            "github_url": "https://github.com/d8ahazard/sd_dreambooth_extension",
            "git_clone_url":"https://github.com/d8ahazard/sd_dreambooth_extension.git",
            "installed_version": "-",
            "available_version": "-",
            "installed": False,
            "visible":True,
            "status": 1,
            "isIncomplete": False,
            "type": "webui_extension",
            "webui_path": "stable-diffusion-webui",
            "buttons": [
                {
                    "button_text": "Uninstall",
                    "key": "uninstall_webui_extension",
                },                                            
            ],
            "launch_buttons": [
                {
                    "button_text": "Update",
                    "key": "update_webui_extension",
                },                                                           
                {
                    "button_text": "Install",
                    "key": "install_webui_extension",
                },  
            ],
            "args": [                                               
            ], 
            "def_args": [
            ],               
            "description":[]     
                          
        },  
        {
            "id": 7,
            "key": "app_",
            "image_path":b'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',
            "title": "Auto-GPT: An Autonomous GPT-4 Experiment",
            "repo_name": "Auto-GPT",
            "github_url": "https://github.com/Torantulino/Auto-GPT",
            "git_clone_url":"https://github.com/Torantulino/Auto-GPT.git",
            "installed_version": "-",
            "available_version": "-",
            "installed": False,
            "visible":True,
            "status": 1,
            "isIncomplete": True,
            "type": "app",
            "install_requirements":True,
            "install_cuda":False,
            "install_instructions_available":False,
            "install_instructions": [
            ],              
            "entry_point": 
            {
                "install":"scripts/main.py",
                "launch":"scripts/main.py",
            },                      
            "buttons": [
                {
                    "button_text": "Update",
                    "key": "update",
                },
                {
                    "button_text": "Delete venv",
                    "key": "delete_venv",
                },
                {
                    "button_text": "Create venv",
                    "key": "create_venv",
                },                        
                {
                    "button_text": "Uninstall",
                    "key": "uninstall",
                },                                              
            ],
            "launch_buttons": [
                {
                    "button_text": "Launch",
                    "key": "launch",
                },    
                {
                    "button_text": "Install",
                    "key": "install",
                },                                                           
            ],            
            "args": [
                [
                  
                ],               
            ],
            "description":["""Autonomous GPT runs till task complation uses on openai API, Be careful as it might be costly. Additionally, it requires a PINECONE API KEY."""]     
        },       
        {
            "id": 8,
            "key": "app_",
            "image_path": b'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',
            "title": "Text generation web UI",
            "repo_name": "text-generation-webui",
            "github_url": "https://github.com/oobabooga/text-generation-webui",
            "git_clone_url":"https://github.com/oobabooga/text-generation-webui.git",
            "installed_version": "-",
            "available_version": "-",
            "installed": False,
            "visible":True,
            "status": 1,
            "isIncomplete": True,
            "type": "app",
            "install_requirements":True,
            "install_cuda":True,
            "install_instructions_available":True,
            "install_instructions": [
                # "-m pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117",
                "-m pip install https://github.com/jllllll/bitsandbytes-windows-webui/raw/main/bitsandbytes-0.37.2-py3-none-any.whl --force-reinstall",
                "download-model.py facebook/opt-1.3b",
            ],
 
            "entry_point": 
            {
                "install":"server.py",
                "launch":"server.py",
            },                      
            "buttons": [
                {
                    "button_text": "Update",
                    "key": "update",
                },
                {
                    "button_text": "Delete venv",
                    "key": "delete_venv",
                },
                {
                    "button_text": "Create venv",
                    "key": "create_venv",
                },                        
                {
                    "button_text": "Uninstall",
                    "key": "uninstall",
                },                                              
            ],
            "launch_buttons": [
                {
                    "button_text": "Launch",
                    "key": "launch",
                },    
                {
                    "button_text": "Install",
                    "key": "install",
                },                                                           
            ],            
            "args": [
                [
                  
                ],               
            ],
            "def_args": [
            ],  
            "description":["""Text generation web UI is like auto1111 webui for large language models """]     
        },   
        {
            "id": 9,
            "key": "app_",
            "image_path": b'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',
            "title": "stable-karlo",
            "repo_name": "stable-karlo",
            "github_url": "https://github.com/kpthedev/stable-karlo",
            "git_clone_url":"https://github.com/kpthedev/stable-karlo.git",
            "installed_version": "-",
            "available_version": "-",
            "installed": False,
            "visible":True,
            "status": 1,
            "isIncomplete": False,
            "type": "app",
            "install_requirements":True,
            "install_cuda":False,
            "install_instructions_available":True,
            "install_instructions": [
                "-m pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1+cu113 --extra-index-url https://download.pytorch.org/whl/cu113",
            ],
            "entry_point": 
            {
                "install":"streamlit run app.py",
                "launch":"streamlit run app.py",
            },                      
            "buttons": [
                {
                    "button_text": "Update",
                    "key": "update",
                },
                {
                    "button_text": "Delete venv",
                    "key": "delete_venv",
                },
                {
                    "button_text": "Create venv",
                    "key": "create_venv",
                },                        
                {
                    "button_text": "Uninstall",
                    "key": "uninstall",
                },                                              
            ],
            "launch_buttons": [
                {
                    "button_text": "Launch",
                    "key": "launch",
                },    
                {
                    "button_text": "Install",
                    "key": "install",
                },                                                           
            ],            
            "args": [
                [
                                                          
                ],      

            ],
            "def_args": [
            ],
            "description":[ """
            Another stable diffusion has been added by request.
            Got CUDA error on a 10GB GPU, maybe it work for you.
                            """,
            ]             
        },                    
    ]
