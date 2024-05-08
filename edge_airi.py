import subprocess
def edge_playback(output):
    # ... (Your existing code for the edge_playback function)
    
    directory_path = "E:\RVC-beta-v2-0618\AniVoiceChanger"
    file_name = "main_colab.py"
    subprocess.Popen(["edge-tts", "--text", '"' + output + '--write-media hello.mp3'])
    run_code_in_directory(directory_path, file_name,py)
    
def run_code_in_directory(directory_path, file_name,py):
    command = "python {}/{}".format(directory_path, file_name,py)
   
    subprocess.call(command, shell=True)

output = 'Am I in danger??'
edge_playback(output)