import os
import whisper

# Initialize the Whisper model
model = whisper.load_model("base")

# Function to transcribe the audio file
def transcribe_audio(file_path):
    transcription = model.transcribe(file_path)
    return transcription["text"]

# Function to save transcription
def save_transcription(file_name, transcription):
    with open(f"{file_name}_transcription.txt", "w") as file:
        file.write(transcription)

# Function to scan a folder and its subfolders
def scan_folder_and_transcribe(folder_path):
    if not os.path.exists(folder_path):
        print("Error: The folder does not exist. Please check the path.")
        return

    for root, dirs, files in os.walk(folder_path):  
        for file in files:
            # Only process audio/video files
            if file.endswith((".m4a", ".mp3", ".mp4", ".wav")): 
                file_path = os.path.join(root, file)
                file_name = os.path.splitext(os.path.basename(file))[0] 
                print(f"🎙 Transcribing: {file_name}")
                transcription = transcribe_audio(file_path) 
                save_transcription(file_name, transcription) 
                print(f"{file_name} transcription completed!")


folder_path = "D:/PYTHON_PROJECT/recording"  
scan_folder_and_transcribe(folder_path) 



