import os
requirements = open ("requirements.txt", 'r')
are_requirements_installed = requirements.read()
requirements.close()
if are_requirements_installed == "yes" :
    pass
else:
    os.system("pip install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl")
    os.system("pip install speechrecognition")
    os.system("pip install duration")
    requirements = open("requirements.txt" , 'w')
    requirements.write("yes")
    requirements.close()