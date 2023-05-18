import ffmpeg

# specify the input video file path
input_video = 'static/input/Andaaz.mp4'

# specify the output audio file path
output_audio = "static/output/audio.wav"

# create a stream object for the input video file
input_stream = ffmpeg.input(input_video)

# extract the audio from the input video stream
audio_stream = input_stream.audio

# create an output stream object for the output audio file
output_stream = ffmpeg.output(
    audio_stream,
    output_audio,
    acodec='pcm_s16le',
    ar='44100',
    ac=2)

# run the FFmpeg command to extract the audio and save it as a WAV file
ffmpeg.run(output_stream)
