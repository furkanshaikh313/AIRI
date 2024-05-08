
    
def run_code_in_directory(directory_path, file_name):
    command = "python {}/{}".format(directory_path, file_name)
    subprocess.call(command, shell=True)
import subprocess
directory_path = "E:\RVC-beta-v2-0618\AniVoiceChanger"
file_name = "main_colab.py"
run_code_in_directory(directory_path, file_name)