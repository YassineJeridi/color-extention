import eel
import subprocess

eel.init('web')

@eel.expose
def color_set(color):
    result = []
    for i in range(len(color)):
        component_name = get_color_component_name(i)
        command = f'"C:\\Program Files\\Blackmagic Design\\DaVinci Resolve\\fuscript.exe" -l lua -x Fusion().CurrentComp.ActiveTool.{component_name}[1]={color[i]}'
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            result.append(output.decode('utf-8'))
        except subprocess.CalledProcessError as e:
            result.append(f'Error: {e.output.decode("utf-8")}')
    return result

def get_color_component_name(index):
    return ['Red1', 'Green1', 'Blue1'][index]

# def color_set_back(color):
#     result = []
#     for i in range(len(color)):
#         component_name = get_color_component_name_back(i)
#         command = f'"C:\\Program Files\\Blackmagic Design\\DaVinci Resolve\\fuscript.exe" -l lua -x Fusion().CurrentComp.ActiveTool.{component_name}[1]={color[i]}'
#         try:
#             output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
#             result.append(output.decode('utf-8'))
#         except subprocess.CalledProcessError as e:
#             result.append(f'Error: {e.output.decode("utf-8")}')
#     return result

# def get_color_component_name_back(index):
#     return ['TopLeftRed', 'TopLeftGreen', 'TopLeftBlue'][index]

eel.start('index.html')
