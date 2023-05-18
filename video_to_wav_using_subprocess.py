import subprocess

input_video = "static/input/Andaaz.mp4"
output_audio = "static/output/audio_by_subprocess.wav"

ffmpeg_cmd = [
    "ffmpeg",
    "-i",
    input_video,
    "-vn",
    "-af",
    "arnndn",
    "-acodec",
    "pcm_s16le",
    "-ar",
    "44100",
    "-ac",
    "2",
    output_audio
]

subprocess.run(ffmpeg_cmd)
