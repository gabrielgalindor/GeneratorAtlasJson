import json


frames = []
print('Set origin name of image source')
image_source = input()
print("Set Total Height of image in px")
height = int(input())
print("Set Total width of image in px")
width = int(input())
print(type(width))
print("---------------")
print("Set Frames Size")
print("Set Frame Height")
frame_height = int(input())
print("Set Frame Width")
frame_width = int(input())
print("---------------")
print("Set Frame Prefix Name")
prefix = input()
print("Set Frame Sufix Name")
sufix = input()
set_new_frame = True
number_frame = 0

while set_new_frame:
    print("---------")
    print(f"Set position X for frame {number_frame}")
    pos_x = int(input())
    print(f"Set position Y for frame {number_frame}")
    pos_y = int(input())
    print("--------------")
    print("Continue ? Type 'y' for continue or 'n' for stop")
    type_continue = input()
    if type_continue !='y' and type_continue!='n':
        while type_continue !='y' and type_continue != 'n':
            print("wrong answer, please type again")
            print("Continue ? Type 'y' for continue or 'n' for stop")
            type_continue = input()
    if type_continue=='n':
        set_new_frame=False
    frame_dict = {'filename': f'{prefix}{number_frame}{sufix}', "rotated": False, "trimmed": False, 'sourceSize': {'w': frame_width, 'h':frame_height}, 'spriteSourceSize': {'x':pos_x, 'y': pos_y, 'w': frame_width, 'h':frame_height}, 'frame':{'x':pos_x+1, 'y': pos_y+1, 'w': frame_width, 'h':frame_height}, 'anchor':{'x':0, 'y':0}}
    print('------ now I will send you the frame added -----')
    print('--------------------------------------')
    print(frame_dict)
    print('--------//-------//--------')
    number_frame+=1
    frames.append(frame_dict)

print("Saving process is active")
print("set name for atlas json file")
name_file = input()
textures = []
texture_dict = {
    'image':image_source,
    'format': 'RGBA8888',
    'size': {'w': width, 'h': height},
    'scale':1,
    'frames':frames
}
textures.append(texture_dict)
meta = {
    'app':"https://www.codeandweb.com/texturepacker",
    'version': '3.0',
    'smartupdate': '$TexturePacker:SmartUpdate:ee78cacc38551445f4ac068d5f89f5bf:6cc19705e7b39b96deecddd16df19941:21e37d97209970b57444d06f2d32a983$'
}
atlas_json = {
    'textures':textures,
    'meta':meta
}

json_object = json.dumps(atlas_json)

with open(name_file,'w') as outfile:
    outfile.write(json_object)