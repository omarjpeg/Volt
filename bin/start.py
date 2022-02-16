from ppadb.client import Client as AdbClient
import os, subprocess
sdk_path = r"C:\Users\omara\AppData\Local\Android\Sdk\emulator;"

# def initialize_emulator(emupath):
#     os.system(f'cd {emupath} ')
#     os.system(r'emulator -avd Pixel_5_API_27')
#     print(os.getenv('Path'))
#     subprocess.Popen(['emulator', '-avd', 'Pixel_5_API_27'],  shell=True,env={'Path': sdk_path+os.getenv('PATH')})


print("""                                        
                        ,--,    ___
       ,---.          ,--.'|  ,--.'|_    
      /__./|   ,---.  |  | :  |  | :,'    
 ,---.;  ; |  '   ,'\ :  : '  :  : ' :    
/___/ \  | | /   /   ||  ' |.;__,'  /    
\   ;  \ ' |.   ; ,. :'  | ||  |   |    
 \   \  \: |'   | |: :|  | ::__,'| :                
  ;   \  ' .'   | .; :'  : |__'  : |__    
   \   \   '|   :    ||  | '.'|  | '.'|    
    \   `  ; \   \  / ;  :    ;  :    ;    
     :   \ |  `----'  |  ,   /|  ,   /      
      '---"            ---`-'  ---`-'         
""")
print('Starting Volt!\n')
print('Initializing emulator: Pixel_5_API_27!\n')
# print(sdk_path)
# initialize_emulator(sdk_path)

client = AdbClient(host="127.0.0.1", port=5037)  # Default is "127.0.0.1" and 5037
devices = client.devices()

if len(devices) == 0:
    print('No devices, please make sure you have ADB installed and the sdk')
    quit()
while True:
    input()
