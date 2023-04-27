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
                        "button_text": "--nowebui",
                        "key": "nowebui",
                    },    
                    {
                        "button_text": "--no-half",
                    }                      
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
                "--force-enable-xformers",
                "--xformers"
               ],               
            "description":["Most popular Stable Diffusion user interface, fully-featured and capable of installing extensions to help create virtually anything."]     
        },
        {
            "id": 10,
            "key": "app_",
            "image_path":b'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',
            "title": "Vladiffsuion - A1111 fork",
            "repo_name": "automatic",
            "github_url": "https://github.com/vladmandic/automatic",
            "git_clone_url":"https://github.com/vladmandic/automatic.git",
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
                        "button_text": "--lowvram",
                        "key": "lowvram",
                    },
                    {
                        "button_text": "--medvram",
                        "key": "medvram",
                    },

                ],
                [
                    {
                        "button_text": "--lowram",
                        "key": "lowram",
                    },    
                        {
                        "button_text": "--no-half",
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
                 
                ],            

            ],
            "def_args": [
                       "--autolaunch",
                       "--theme=dark",
            ],               
            "description":['"automatic" also known as Vladiffsuion is a fork of A1111 webui, diving into the name chaos with flair. This fork promises to deliver more frequent updates for improved stability, enhanced speed, and a selection of pre-installed extensions.']     
        },  
        {
            "id": 12,
            "key": "app_",
            "image_path":b'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',
            "title": "Stable Diffusion web UI-UX - A1111 fork",
            "repo_name": "stable-diffusion-webui-ux",
            "github_url": "https://github.com/anapnoe/stable-diffusion-webui-ux",
            "git_clone_url":"https://github.com/anapnoe/stable-diffusion-webui-ux.git",
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
                        "button_text": "--nowebui",
                        "key": "nowebui",
                    },    
                    {
                        "button_text": "--no-half",
                    }                      
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
                "--force-enable-xformers",
                "--xformers"
                ],               
            "description":['One more fork of Automatic1111 web UI has a beautiful user interface and many additional features. It appears to be well-maintained.']     
        },         
        {
            "id": 11,
            "key": "app_",
            "image_path":b'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAIAAAC0Ujn1AAACy0lEQVR4nLVVwU7yQBDe3bQEKxBsYgIaA/FC4qUhMWm8wAOQyJ3H8BF8Er34AGDiiQAHPXnApNF4ICTGoFFKsEKAuuz8h/FvcKlY5P/n0Gxndr+Znf1mhgIAIYQQAgAAQCkFAMYYWUaEEHjEWxBCKEIj6FJwkozHY8ZYKBTyNIqHa9v29fU15zwSiZimGQ6Hg/gDgMlkUq1WAUAIEYvF8vk8IYRSSoQQQgjbts/OztrttuM4zWazXC6jHhbKdDoFgFqtdnNzg5pGo3F1dYUmhqFZlmWaZjqdjkajhmFQSl3X/TFk3PD+/r63t4eJzeVyLy8vaPpMuaZptm2Tv4+ZzWZVVQ2Y5d3dXYwDAOr1ejKZ/EwyYn18fFxcXGxubpqmyRhb9kkR5O7u7vX1NZfLURSPfISQTqeTSCQYY0sRxqOsxNov0KvLbExMMqwIPXtX9p1hdTffFrTkRuoHv4d2XXc0GnkQ6GYwGIxGI3x8byfnXAjhC6JI/5xzRVFOT08rlUq5XJ5Op4yx4XBoWdZ4PFZVVVGUTCYTi8WEEIqiHB8fx+Pxo6MjPLgIGtljGEY4HPZCvr29PTk56fV6nHNVVYvFYqlUwjsdHBzgTp9m+WOLaLVa85c9Pz8HAM75guP+ucY2hoUQj8dLpZKu65hiXdcLhUImk8EC6Xa7nU6H+DEqaMk8Pz8/Pj4CwPb29tbWlqcfDoeVSuXw8HBtbU0q4EDQs7MDf5EnqL+8vNQ0LZvNStsCDSrsKkIIzL7Xv/CbSqXe3t7mT8kM+U4kOntKQoimaa7r+gQUENpXYOFcXQkaZTAYrK+vrwTtOE6/3599dlx3u92NjY1fQiNEu92+v7+fvTuun56ednZ2yFxBBnpGhDAMQ/JHKX14eAiFQpFIRGJe0Kg9LKnJCSEsy9rf3ydfm/BnQKu0fM654zi6rvta/8Fs/F/kWzD7/wDSnRnN1GeEDwAAAABJRU5ErkJggg==',
            "title": "Lama Cleaner",
            "repo_name": "lama-cleaner",
            "github_url": "https://github.com/Sanster/lama-cleaner",
            "git_clone_url":"https://github.com/Sanster/lama-cleaner.git",
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
                "-m pip install lama-cleaner",

            ],
            "entry_point": 
            {
                "install":"lama-cleaner",
                "launch":"lama-cleaner",
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
                        "button_text": "--model=lama",
                        "key": "model=lama",
                    },
                    {
                        "button_text": "--device=cpu",
                        "key": "--device=cpu",
                    },      
                    {
                        "button_text": "--port=8080",
                        "key": "port=8080",
                    },                                 
                ],               
            ],
            "def_args": [
                '--model=lama',
                '--device=cpu',
                '--port=8080',
            ],
            "description":[ """A free and open-source inpainting tool powered by SOTA AI model.""",
            ]             
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
            "description":["A powerful and modular stable diffusion GUI and backend."]     
                                       
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
                        "button_text": "--embeddings",
                        "key": "embeddings",
                    },  
                    {
                        "button_text": "--no-embeddings",
                        "key": "no-embeddings",
                    },                                                    
                ],

            ],
            "def_args": [
            ],               
            "description":["InvokeAI is a leading creative engine for Stable Diffusion models, empowering professionals, artists, and enthusiasts to generate and create visual media using the latest AI-driven technologies."]     
                                      
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
            "description":["This repository provides a Windows-focused Gradio GUI for Kohya's Stable Diffusion trainers. The GUI allows you to set the training parameters and generate and run the required CLI commands to train the model."]     
                                      
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
            "title": "Auto-GPT",
            "repo_name": "Auto-GPT",
            "github_url": "https://github.com/Torantulino/Auto-GPT",
            "git_clone_url":"https://github.com/Torantulino/Auto-GPT.git",
            "installed_version": "-",
            "available_version": "-",
            "installed": False,
            "visible":True,
            "status": 1,
            "isIncomplete": False,
            "type": "app",
            "install_requirements":True,
            "install_cuda":False,
            "install_instructions_available":False,
            "install_instructions": [
            ],              
            "entry_point": 
            {
                "install":"run.bat",
                "launch":"run.bat",
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
            ],
            "def_args": [
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
            "isIncomplete": False,
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
                    {
                        "button_text": "--auto-launch",
                    },                      
                    {
                        "button_text": "--model-menu",
                    },  
                ],  
                [

                    {
                        "button_text": "--notebook",
                    },
                    {
                        "button_text": "--chat",
                    },   
                ],                 
                [
                    {
                        "button_text": "--cai-chat",
                    },    
                    {
                        "button_text": "--character",
                    },                      
                ],
                [
                    {
                        "button_text": "--model",
                    },
                    {
                        "button_text": "--lora LORA",
                    },
                    {
                        "button_text": "--model-dir",
                    },
                ],
                [
                    {
                        "button_text": "--settings",
                    },
                    {
                        "button_text": "--xformers",
                    },
                ],       
                [
                    {
                        "button_text": "--extensions",
                    },
                    {
                        "button_text": "--verbose",
                    },
                ],            
                [
                    {
                        "button_text": "--cpu",
                    },
                    {
                        "button_text": "--auto-devices",
                    },
                ],         
                [
                    {
                        "button_text": "--gpu-memory",
                    },
                    {
                        "button_text": "--cpu-memory",
                    },
                ],                                          
                [

                    {
                        "button_text": "--listen",
                        "key": "listen",
                    },
                    {
                        "button_text": "--listen-host",
                    },                    
                    {
                        "button_text": "--listen-port=7862",
                    },                    
                ],            
                [
                    {
                        "button_text": "--gradio-auth-path",
                    },
                    {
                        "button_text": "--api",
                    },    
                    {
                        "button_text": "--share",
                    },                                    
                ]
            ],
            "def_args": [
               '--auto-launch',
                '--chat',
               ],    
            "description":["""Text generation web UI is like auto1111 webui for large language models """]     
        },   
        {
            "id": 9,
            "key": "app_",
            "image_path": b'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',
            "title": "Stable Karlo",
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
    
            ],
            "def_args": [
            ],
            "description":[ "Stable diffusion with a basic interface using Streamlit requires more than a 10GB VRAM GPU.",
            ]             
        },
        {
            "id": 13,
            "key": "app_",
            "image_path":b'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAYCAYAAADtaU2/AAAMbmlDQ1BJQ0MgUHJvZmlsZQAAeJyVVwdYU8kWnluSkJAQIICAlNCbIFIDSAmhBZBeBBshCSSUGBOCir0sKrh2EQEbuiqi2FZA7NiVRbH3xYKKsi7qYkPlTUhA133le+f75t4/Z878p9yZ3HsAoH/gSaV5qDYA+ZICWUJ4MHN0WjqT9AwggA50gReg8/hyKTsuLhpAGbj/Xd7dgNZQrjoruf45/19FVyCU8wFAxkKcKZDz8yE+DgBexZfKCgAgKvVWkwukSjwbYj0ZDBDiVUqcrcLblThThQ/32yQlcCC+DIAGlceTZQOgdQ/qmYX8bMij9RliV4lALAGAPgziAL6IJ4BYGfuw/PyJSlwOsT20l0IM4wGszO84s//GnznIz+NlD2JVXv2iESKWS/N4U//P0vxvyc9TDPiwhYMqkkUkKPOHNbyVOzFKiakQd0kyY2KVtYb4g1igqjsAKEWkiEhW2aMmfDkH1g8YQOwq4IVEQWwCcZgkLyZarc/MEodxIYa7BZ0iLuAmQWwI8UKhPDRRbbNRNjFB7Qutz5Jx2Gr9OZ6s36/S1wNFbjJbzf9GJOSq+TGtIlFSKsQUiK0LxSkxEGtB7CLPTYxS24wsEnFiBmxkigRl/NYQJwgl4cEqfqwwSxaWoLYvyZcP5IttFIm5MWq8r0CUFKGqD3aKz+uPH+aCXRZK2MkDPEL56OiBXATCkFBV7thzoSQ5Uc3zQVoQnKBai1OkeXFqe9xSmBeu1FtC7CEvTFSvxVMK4OZU8eNZ0oK4JFWceFEOLzJOFQ++DEQDDggBTKCAIxNMBDlA3NrV0AV/qWbCAA/IQDYQAme1ZmBFav+MBF4TQRH4AyIhkA+uC+6fFYJCqP8yqFVdnUFW/2xh/4pc8BTifBAF8uBvRf8qyaC3FPAEasT/8M6Dgw/jzYNDOf/v9QPabxo21ESrNYoBj0z6gCUxlBhCjCCGER1wYzwA98Oj4TUIDjechfsM5PHNnvCU0EZ4RLhOaCfcniCeK/shylGgHfKHqWuR+X0tcFvI6YkH4/6QHTLjBrgxcMY9oB82Hgg9e0ItRx23sirMH7j/lsF3T0NtR3Ylo+Qh5CCy/Y8rtRy1PAdZlLX+vj6qWDMH680ZnPnRP+e76gvgPepHS2whth87i53AzmOHsQbAxI5hjVgLdkSJB3fXk/7dNeAtoT+eXMgj/oc/ntqnspJy11rXTtfPqrkC4ZQC5cHjTJROlYmzRQVMNnw7CJlcCd9lGNPN1c0dAOW7RvX39Ta+/x2CGLR80837HQD/Y319fYe+6SKPAbDXGx7/g9909iwAdDQBOHeQr5AVqnS48kKA/xJ0eNKMgBmwAvYwHzf4RvMDQSAURIJYkATSwHhYZRHc5zIwGUwHc0AxKAXLwGpQATaAzWA72AX2gQZwGJwAZ8BFcBlcB3fh7ukAL0E3eAd6EQQhITSEgRgh5ogN4oS4ISwkAAlFopEEJA3JQLIRCaJApiPzkFJkBVKBbEJqkL3IQeQEch5pQ24jD5FO5A3yCcVQKqqHmqK26HCUhbLRKDQJHYdmo5PQInQ+ugQtR6vRnWg9egK9iF5H29GXaA8GME3MALPAnDEWxsFisXQsC5NhM7ESrAyrxuqwJvicr2LtWBf2ESfiDJyJO8MdHIEn43x8Ej4TX4xX4NvxevwUfhV/iHfjXwk0ggnBieBL4BJGE7IJkwnFhDLCVsIBwml4ljoI74hEogHRjugNz2IaMYc4jbiYuI64m3ic2EZ8TOwhkUhGJCeSPymWxCMVkIpJa0k7ScdIV0gdpA8amhrmGm4aYRrpGhKNuRplGjs0jmpc0Xim0UvWJtuQfcmxZAF5KnkpeQu5iXyJ3EHupehQ7Cj+lCRKDmUOpZxSRzlNuUd5q6mpaanpoxmvKdacrVmuuUfznOZDzY9UXaojlUMdS1VQl1C3UY9Tb1Pf0mg0W1oQLZ1WQFtCq6GdpD2gfdBiaLlocbUEWrO0KrXqta5ovaKT6TZ0Nn08vYheRt9Pv0Tv0iZr22pztHnaM7UrtQ9q39Tu0WHojNCJ1cnXWayzQ+e8znNdkq6tbqiuQHe+7mbdk7qPGRjDisFh8BnzGFsYpxkdekQ9Oz2uXo5eqd4uvVa9bn1dfQ/9FP0p+pX6R/TbDTADWwOuQZ7BUoN9BjcMPg0xHcIeIhyyaEjdkCtD3hsONQwyFBqWGO42vG74yYhpFGqUa7TcqMHovjFu7GgcbzzZeL3xaeOuoXpD/Ybyh5YM3Tf0jglq4miSYDLNZLNJi0mPqZlpuKnUdK3pSdMuMwOzILMcs1VmR806zRnmAeZi81Xmx8xfMPWZbGYes5x5itltYWIRYaGw2GTRatFraWeZbDnXcrflfSuKFcsqy2qVVbNVt7W59Sjr6da11ndsyDYsG5HNGpuzNu9t7WxTbRfYNtg+tzO049oV2dXa3bOn2QfaT7Kvtr/mQHRgOeQ6rHO47Ig6ejqKHCsdLzmhTl5OYqd1Tm3DCMN8hkmGVQ+76Ux1ZjsXOtc6P3QxcIl2mevS4PJquPXw9OHLh58d/tXV0zXPdYvr3RG6IyJHzB3RNOKNm6Mb363S7Zo7zT3MfZZ7o/trDycPocd6j1ueDM9Rngs8mz2/eHl7ybzqvDq9rb0zvKu8b7L0WHGsxaxzPgSfYJ9ZPod9Pvp6+Rb47vP908/ZL9dvh9/zkXYjhSO3jHzsb+nP89/k3x7ADMgI2BjQHmgRyAusDnwUZBUkCNoa9IztwM5h72S/CnYNlgUfCH7P8eXM4BwPwULCQ0pCWkN1Q5NDK0IfhFmGZYfVhnWHe4ZPCz8eQYiIilgecZNryuVza7jdkd6RMyJPRVGjEqMqoh5FO0bLoptGoaMiR60cdS/GJkYS0xALYrmxK2Pvx9nFTYo7FE+Mj4uvjH+aMCJhesLZREbihMQdie+SgpOWJt1Ntk9WJDen0FPGptSkvE8NSV2R2j56+OgZoy+mGaeJ0xrTSekp6VvTe8aEjlk9pmOs59jisTfG2Y2bMu78eOPxeeOPTKBP4E3Yn0HISM3YkfGZF8ur5vVkcjOrMrv5HP4a/ktBkGCVoFPoL1whfJbln7Ui63m2f/bK7E5RoKhM1CXmiCvEr3MicjbkvM+Nzd2W25eXmrc7XyM/I/+gRFeSKzk10WzilIltUidpsbR9ku+k1ZO6ZVGyrXJEPk7eWKAHP+pbFPaKnxQPCwMKKws/TE6ZvH+KzhTJlJapjlMXTX1WFFb0yzR8Gn9a83SL6XOmP5zBnrFpJjIzc2bzLKtZ82d1zA6fvX0OZU7unN/mus5dMfeveanzmuabzp89//FP4T/VFmsVy4pvLvBbsGEhvlC8sHWR+6K1i76WCEoulLqWlpV+XsxffOHnET+X/9y3JGtJ61KvpeuXEZdJlt1YHrh8+wqdFUUrHq8ctbJ+FXNVyaq/Vk9Yfb7Mo2zDGsoaxZr28ujyxrXWa5et/VwhqrheGVy5u8qkalHV+3WCdVfWB62v22C6oXTDp43ijbc2hW+qr7atLttM3Fy4+emWlC1nf2H9UrPVeGvp1i/bJNvatydsP1XjXVOzw2TH0lq0VlHbuXPszsu7QnY11jnXbdptsLt0D9ij2PNib8beG/ui9jXvZ+2v+9Xm16oDjAMl9Uj91PruBlFDe2NaY9vByIPNTX5NBw65HNp22OJw5RH9I0uPUo7OP9p3rOhYz3Hp8a4T2SceN09ovnty9Mlrp+JPtZ6OOn3uTNiZk2fZZ4+d8z93+Lzv+YMXWBcaLnpdrG/xbDnwm+dvB1q9WusveV9qvOxzualtZNvRK4FXTlwNuXrmGvfaxesx19tuJN+4dXPszfZbglvPb+fdfn2n8E7v3dn3CPdK7mvfL3tg8qD6d4ffd7d7tR95GPKw5VHio7uP+Y9fPpE/+dwx/yntadkz82c1z92eH+4M67z8YsyLjpfSl71dxX/o/FH1yv7Vr38G/dnSPbq747Xsdd+bxW+N3m77y+Ov5p64ngfv8t/1vi/5YPRh+0fWx7OfUj896538mfS5/IvDl6avUV/v9eX39Ul5Ml7/pwAGB5qVBcCbbQDQ0gBgwL6NMkbVC/YLoupf+xH4T1jVL/aLFwB18Ps9vgt+3dwEYM8W2H5BfjrsVeNoACT5ANTdfXCoRZ7l7qbiosI+hfCgr+8t7NlIKwH4sqyvr7e6r+/LZhgs7B2PS1Q9qFKIsGfYGPclMz8T/BtR9aff5fjjHSgj8AA/3v8FUaKQ2Z8UUFoAAAhlSURBVHicBcFLjFxZYYDh/5x77qOqblXX29XtR7ft7rbdQ48gzoAhIUyCFKIgNLBPMouskFigkC0LlE0kWCBFShaRkmWEEiCJJpmBGcYsAIfxDPNuj9t22+6Xu6uq63nrvs89+T5Rq/aMkBZCKgwC6XgYKRDGgAC7toRf9khGQ4pUo0pVvFIF11aUlCKZzrCkouzazAYjsjSjVPYI4wTXdam3egz6x8TpiEW4QBeGxGiU47mkcU6BQSpFISXlskOaC6QRVEslbMclcj201CjbxlaSctlnMVuQJhnxbIgtJcJIHMuhpGwqdY9FEnM2OsaQYoQkN4JCgDAS0WiuGsurogtNYQzVaglbSl7oWqxv3+DXj0IO5iH1Zh1HVakuddnavMDRUZ9pf0hwckx0NiQJF+RJRhYH2ELhOw7SUQhdMI8DojwjKTJCnaJ1jugs3zBuo4HWOTrPKSmBAl79/leYxhbf/KdH1D+1zY3P3qRXa4CWXOrVabkWO5/s8XB3j3azxv2773P6ZJ+TBx+TZxIjCjxS6l4FKSzG0ZQgi4iMRlMguue3jeVXMMKQa2i7iu2tTQoLFonFyue+Tr3ZpVQSJKd9JjKhu77Cy1/8DFaYEuSaLM042N1n7+kz3njl5+zv3Gc+PUMVGY7UtCpV8ixlGM+IjQbbQrTO3TDSq5LrHMdzON9s0mq16Vs+z33pz+iuXGUtjalXbM6ykNPjI/KqRbNV4vOrV7h+eRlXWRQI+mdT3nr/Ea/96H9555dvYpEhdIwlBEuezzxZEBUxsyREGWEQwqAsi3a3x6zSJHV9llc3WEQ5R/t79B/28RY5ppOSPvsEPZtSW1tmsn2dgfk0OsgYzRZ0rq2TxxGtlRZfuHWLnXfeJnMUcRSQFSllu4yULqnOUdJRKEviVWpY3RWubD1HpXcZR5SwBnOkW2LS8hlkB3TDmJ2372Lmc67xApc/u0nbzTB2iWQ45O7PbnP9S1/EsW3m5y9CmLD3eAclJaQJNc9mEiRoA0qWy7h+E6dWw2tX6Fy9inXuGqtBxnE+5N6dX+FGB1xZafPg7f/jcHRAzavxyekJzx+fUM9usNSr00sK+kd9Fg93eX5zg51ck/seVl7Q9OrkMsSzLWyRkuUxyimXcdttGhdWqa99ikpvA11U+O2djwimY2p+jVp1lbPDY+bBnCjPKaIFp3lIVlnCtkuMD/cJFgmVZhW/5CItyWgWMA5i3OYFsnBGYTRYJQwKEEhlWxgKgrnHnzRvsnXqUTtO+f1OmY2exY3t5/C1jw7mhOGEvDD4NZ9xOucH//wvvPrqG5S15uMPP+JwMUaUFDVP8dLXPs+3v/OXXNvs4QpNuVzHuGWiNENaCtW6sEZhL7Ndv0Y3cSCNMTLnyDFUGx5mPMJzCs5OdujPRniuSxjNaXrguy4//ME/cNm1+e8f/ZjYUlz6279heAi1dpuNC2X+8Lkq9UkJyz/Hrz58TKoTHNtDpvM5veXPsL16DbdlM/cdBuOIpFOHYcCHr/wH8/0PcJaaFIXBFJrFYsHZIuHWC7fotLo8XWjcZocLtSVs28KyFf3jE/buP6DSOceV6+t8fP8Js9kU25bkOkGeHewRTB8TrZTpV23uHPe5fe893nr9dX72yr/x7sPbvPXobbQs0DrHtW2Wl9os5TYrsk6j1OHR/pC/ePmvqEjJu6+/xu6b/0Oz0UQ7y9y9b/jJbwYczVPsmofOc4zJUV45JzGH3H78Hv7GKrP8mOloh9He+1gyRjgeZ4MTFsEMSzkgFA2/y5//0YsMxzEPxxNGv77LN7/118xffJHfvfZT/K2rnD15yOEzxc79Z0SFxnIEKAdtDEZIpMkN0fABMn9Ap5Nw7qLA37hE+VwXp9KgtbyOVC7j8RDb9khNgXJ91i6uU4QpUZHy6PSIv//u91HCYhIEBHFGEObUe21al1aJUsk0rDBdVBGqgoVARZMItzLEsw9w1YTKl7fIKzXGux8Q958gpSKOQ1zPR9Va2FnA6eiQH//032ltXuVkOkCnIe7GFdKswK7U6Vxa487td6lcMphFxDywKHfXiIM5AhchQlSRxJSchOT0hMGTY3pXb2LZOXbZJUZQGIPWGlPkqHhKpg1LnRU2vvEVEuHS/d0dLApanfNsvfTHfHI85GhsaK+s8uYvPyDWIVYxwaVLkC9wnBJZMkeZXBNMU+TBGLd5j8fBZcaP76PDCVFwhtQFfr1DNB0yOnnKS7e2Uc2L/PaNX3DwcIdZMCJNY/7xe9/hov9DVn/vC/zkX/+T659ewy4v8ezRKef986x0tjmwRkzknLmMEe3Gsqn3fJx2g9L5K6C6BIOI6OQpo4fvo5MIIcErNUh1QdvVxLlhGgYIaZHnmq31q6y3NxHli6ysXmJ0NCQrbCZRzmj/gBdvfhXT2GB/9x3M5Dc8OH0LVRQ580GAE1ksxo+Q+S7js4Byo4nfuUA6GxJOBoTTY0peg0EhsITBb11CpCHn2x2+8eU/5Xhvzs8/+IiDw1OKJETVzzEZL9he2SJsX2T0+F16PGOsYhyRIZYqbSOExLVd8Fw8r0y0CJnPpziui1IlXCMIps9I8wBHVUC5SOVQsSw2l1eol3zSeYknccg8i1CyREW1ef7cVWpLXU6nCW0mZKbPMHjK2ewYJbAQRpKmGtvSZCqj5FdQXpkkNzR9g6sLHC4yX/SZx2NsY7BNgc4Kqr0m1zbX+cV/vUe1XCMIU5b9Gn+wcZMom3H/6B69Spmnk1200FgmQlgOSggLUxiEAUwBJiWKchQ23YqNtHJcWzKUhnbjAm5QYRoOcJwSN9aepz9IuPW5GqkjcLXi717+OvnZnHuPQ0aTZwh9xu7glGkUU/c8MAvCNOT/AQlIKeF8Wle8AAAAAElFTkSuQmCC',
            "title": "Kandinsky 2.1 - webui",
            "repo_name": "Kandinsky-2",
            "github_url": "https://github.com/adrianpuiu/kandinsky",
            "extra_github_url": "https://github.com/ai-forever/Kandinsky-2",
            "git_clone_url":"https://github.com/adrianpuiu/kandinsky.git",
            "installed_version": "-",
            "available_version": "-",
            "installed": False,
            "visible":True,
            "status": 1,
            "isIncomplete": False,
            "type": "app",
            "install_requirements":False,
            "install_cuda":True,
            "install_instructions_available":True,
            "install_instructions": [
                "-m pip install torch==1.13.1 torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117",
                "-m pip install git+https://github.com/ai-forever/Kandinsky-2.git",
                "-m pip install git+https://github.com/openai/CLIP.git",
                "-m pip install opencv-python",
                "-m pip install gradio",
            ],
            "entry_point": 
            {
                "install":"app.py",
                "launch":"app.py",
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
             
            ],
            "def_args": [
            ],
            "description":[ "A Kandinsky web user interface for https://github.com/ai-forever/Kandinsky-2, requires more than a 8GB VRAM GPU.",
            ]             
        },         
        {
            "id": 14,
            "key": "app_",
            "image_path":b'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',            
            "title": "Ckpt2Safetensors-Conversion-Tool-GUI",
            "repo_name": "ckpt2Safetensors-Conversion-Tool-GUI",
            "github_url": "https://github.com/diStyApps/Safe-and-Stable-Ckpt2Safetensors-Conversion-Tool-GUI",
            "git_clone_url":"https://github.com/diStyApps/Safe-and-Stable-Ckpt2Safetensors-Conversion-Tool-GUI.git",
            "installed_version": "-",
            "available_version": "-",
            "installed": False,
            "visible":True,
            "status": 1,
            "isIncomplete": False,
            "type": "app",
            "install_requirements":True,
            "install_cuda":False,
            "install_instructions_available":False,
            "install_instructions": [
            ],
            "entry_point": 
            {
                "install":"run_app_gui.py",
                "launch":"run_app_gui.py",
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
             
            ],
            "def_args": [
            ],
            "description":["Effortlessly convert between Stable Diffusion checkpoints and safeTensors with the user-friendly Ckpt2Safetensors Tool-GUI, enabling seamless two-way conversions"]             
        },     
        {
            "id": 15,
            "key": "app_",
            "image_path":b'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAJhUlEQVR4nH2XW6jn1XXHP2vtvX+X/+X855w5Z845c5/J6MxIJb2IpfaeBmKKhbTlL4Q0tumbGoL4kKah0NSXpuRFYmNSWlM6rYTMv4VQhChpI21QE0etokajE53J3M5tzvV/+d323n04GojYLlgPe29YHxZrr8X6Cv+X9fuGwcADHJ/+cC/knY+YKB8VH28hxkMxSpcYkRh3JHApCs9F9NuR4RNvbfzHFkCfs2bAnf79wsv73/UVBn7hxKfm8sno0xrlkwY5Jmrx1hKTHHBIBHwNdYUrS2gKQoxvg/6zTxf+9vzSQ6vQNzAIQPz/wEKMIBKP3vrAXbp28Ytp7ReDCmWrFULejml7VlplELu9I0kVMNHGkfFxR6uodSl2vKWmacB1ryXdQ597/s2/OANR3kHF9wPLOx5vOPnpr5C07rabS9RZqyln9hiNQdq9OTrkJCsbmO0tWqXQ8ikilmuyyWYWiUk3srPsbTm2ZuoodbX21Veu/N2978Z+F67vQvv0lRjjqcN3fdNkM3fb4fUmtDqhWpi3zhfSTlKSueOQ7cFYRzSWYB1JTJgbz3DT8ARTWxXJeEvM9BFL0gmhWG1cOn/3zfv+5JvEGPv09d1kd8H9szpg4I/9wucfNp0Dfe+LWtXYam5eXTMiUUV/8Veo7vsdtu7/MKPDxwlRCD4w3H+UHz70MS4+8nGmj9+GlhW22EamD6oN0YYYatM+1D918vMPDxj4fv+s7mba75vBYOBPnvj4J6T3gX+ROqslbDtvI1WvRVJtQu8Y8uCn4GSLBiX81xoz9/87+VbF1oO/T3HHIjUw/Z/rtD7xEJN0Dd9exI43sTgam9eVLVzY/tEfvXLtXx/t0zc6GJwNp059cq8k2YPBhECOUWcIrRYmlpA4QicntAVPhaWiOdSmvvFm4vHfYHKiS8IES0HTs6hpYW2CaSpI92DFoNYYDEGTqQdPnbp374CzQUGid+lnTNqZjSpBnapmKdE6RCMxz9Bii/q/LxBGCf6NivE/ncMuZPyWm6H98HnMayWLyxlH/v5NmjjC2g5OwJgMa1vYxKkYCUnSnc19/AxIlJO3/Wk3TpLXjNr9vj0XM81VQ8U4UZAR0Rrk2M1UH/pVJqsl5t+eYXKiR/vwjXzpiRbfG13kpfUlbl/4OaxJePLak4z1IiKWYLrkIVJ1HaUzQTavSt2sX00lP20p09s1TQ/E0ARSp0qChAZNHAEHiWPSncXVFjdahrhEexgpXr3Ady8EkljiqreZXJonP3iCTHqUpKAOxaEuYFxO93d/U8vzS8G/cu5AOf7J7dZbe4dzSSRI1MSi0UJQNDF4aUFq8EWNbo4wK5dINcF15jHnr1FPHB9wB9isc7Y7QyQMaaohppUTxaIoag0kwsa5Z4jrK9FNT0cfpu6wYs0tWCSWQYIoGAPREJwQ2vsIJuKyFFnfwG+MKfMexfIK+uar/GTi6MTIHj3ElKTEomQm7mGniqCWiRuhLgGjUE9QPxZoi7rkFivOHmxcSnLitDpvYGkLyRzRgPT20iRt0jTDZS2K+cOUrz9LVhbEYoWxzZkU13FuioO9Y6yWY6brHlN+itJMuJxUiHWYLIVeG0YbKlbBuIMajeuW0/OEmWlESsAjxiFqsLWnnbfI8xbdNKN9YD+ZSzExMjV1iL3pIj7N2NuZ5cShWWbSveybOUq7O020inUpWIvpdjEnD4JNwRjUuK5iMmwU5IWXaK4tI2mKqkXFIjUkEZI8QcqGqXYHe/omzOxhpN1hRmeZNke5+fRB8sTQynMOHpgl7XQQyVDjEGMR53bb0xhELWItaiTZccFgshbqMpDdRyuOxFvsOGCriCkNijDZ3mQYa1Y23uSHk9fwzjFeCSQebFuQXMjaLdRm8A7UN55wZQNRRUyCqNtRjLusJkOwQcSi4hB1GAxJE0hK0FFN1krwVqmKiri5ihOHCwmTcsj1rQl5kmBypYoNURRrDEYMiu7O9bJA1AYxCVh32Ypxz6nJTou4KKqgu/XVKFgfkdJjNaF9bciOb4hi8NqmueFWOB8Jmw12UvDG9hrbUbGhRV2WJDGi+RQ61UI6INUSIi6qyWIw7jkV235MMIJJBEl410UcBJhrWhx9fZOrL59jbVJj1jZhtEWYFOzINqWWTJzlYpjwnStPkY6GdNQQ6khxZJEyzQnb27hhAS4VRASbPaZ+evbxiFxR1xY0DarJ7sQyLfbrLNnWNq+88R022g7OX4BqTLJ+hakXv4tf+T4b/irLxTLuUo6THo9feoxeXbBvbi92dRU/3IBYI8YGdS0JMVyR2cXH9Udf/9iOBnlE056gNgST0LXTLJZtVtff4sXVZ9ipt/AX3oKXnsZNNglpl2L/TZT7b6VJ9zJqlri48mO6zRwr5RWeXnqSlfGrLARHJ+niE0tUDSbtSRPDI09//dd2LESpizNfNqr3kHRmbGwHs76tF7deo2hG6LhAyproN5Hx1m7dq4KGLtaPGRVXWXOLDJsxO9sOKwnrcZn1nXXEX2Z67gby+TQUzmvTTNZCVX8Zomi/P9DXv/XH1zWG+7S9oC3J/eXNVynrIeoDwXukbhBN0KJAItTd/cS0TUgC47Zh6C+zUr/AdS7i44iKisbUDNnkyvWX6U7aPskWNIq/79y3/uB6vz9QHQzu9P3+WfPCN/7w0aauvmay3BGbmgghhN2+Ju4OFJfj2/PEosAW16Fao4pbjFo5EwtBDZUf4jVQmoagkSBNHVupq5ria9//xu892u9HMxjc6RVgMOiHfv+sefkfbrvHl6sDk027GKUBAsYgxmGDJ3QPYMsd8mYba4XEGNSPKeI2Te8IIjXRQuOExhCCxMbk064eLQ9+8I+/fE+/f9YMBoT3rLdR4AsCfxVPfehLX1Exd4dyhC/Lxo5rExsjft9J5OIPdn8pisaIaTxGM5Ijv465+iJGYiRNvclSa9I2DeGr33v2/nvhLwW+ENmVAe9d6OM7Z4mnfvuv75KgX5RgF8NwjNlaD2Hh52PcviZx54JoaEQiKBpl6saYtOajW/of0da0ulYLb5pr0cjnnnr2s2eIUXZJ8tOFXn8WLHFXwfTN60/++ZnaNx+MjX8gqrwd8lyTemhc2lKbz4v2DqK9g4T2AbF2StOmNCHNtXbydhX9A0PffPCpZz97pt/vG0R+Bvp+EuantluPXcF1/Jf+rGdL/YhLZz4as4Vbmus/PkSadtULFNVOa++JS3ay8lxTLH9buuGJ55//m633xniv/S9oV21VkzMDbAAAAABJRU5ErkJggg==',            
            "title": "Stable-Diffusion-Pickle-Scanner-GUI",
            "repo_name": "Stable-Diffusion-Pickle-Scanner-GUI",
            "github_url": "https://github.com/diStyApps/Stable-Diffusion-Pickle-Scanner-GUI",
            "git_clone_url":"https://github.com/diStyApps/Stable-Diffusion-Pickle-Scanner-GUI.git",
            "installed_version": "-",
            "available_version": "-",
            "installed": False,
            "visible":True,
            "status": 1,
            "isIncomplete": False,
            "type": "app",
            "install_requirements":True,
            "install_cuda":False,
            "install_instructions_available":False,
            "install_instructions": [
            ],
            "entry_point": 
            {
                "install":"run_app_gui.py",
                "launch":"run_app_gui.py",
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
             
            ],
            "def_args": [
            ],
            "description":["Better safe than sorry, Stable-Diffusion-Pickle-Scanner-GUI offers an extra layer of protection against potential malicious code. - safetensors models don't need to be scanned."]             
        },               
    ]
