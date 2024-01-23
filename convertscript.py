import os
from readConfig import returnValue

if 'pnnx' in returnValue('conversion_method'):
    pnnx=True
    onnx=False
if 'True' in returnValue('fp16'):
    fp16=1
else:
    fp16=0
os.system('git clone https://github.com/hzwer/Practical-RIFE')

os.system('cp -r Practical-RIFE/* .')



os.system('wget https://raw.githubusercontent.com/TNTwise/Rife-NCNN-Model-Comparisons/c053eaf9b51fa07467954d4d8ed1cf752b1fd68b/0.png && wget https://raw.githubusercontent.com/TNTwise/Rife-NCNN-Model-Comparisons/c053eaf9b51fa07467954d4d8ed1cf752b1fd68b/2.png')


os.system('pip install -r requirements.txt')

os.system('python3 modify_train_log.py')
os.system('mv train_log/ train_log_backup/')
os.system('mv train_log_export/ train_log/')

os.system('python3 inference_img.py  --img 0.png 2.png --exp 1')

os.system('mv train_log/ train_log_export/') 
os.system('mv train_log_backup/ train_log/')

os.system('chmod +x pnnx')
os.system(f'./pnnx rife.pt inputshape=[1,3,256,256],[1,3,256,256],[1] fp16={fp16} optlevel=2 ncnnparam=flownet.param ncnnbin=flownet.bin')
    
os.system('python3 fix_param_file.py')
