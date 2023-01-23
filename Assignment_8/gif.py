import os
import imageio
IMAGES=[]
file_list=sorted(os.listdir("images/"))
for file_name in file_list:
    file_path="images/"+file_name
    print(file_path)
    image=imageio.imread(file_path)
    IMAGES.append(image)
    
imageio.mimsave("images/my_output.gif",IMAGES)
