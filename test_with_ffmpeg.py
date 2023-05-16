import ffmpeg as ff
'''input_stream = ff.input('static/input/videoplayback.mp4')
output_stream = ff.trim(input_stream, start='00:00:10', end='00:01:20',)
output_stream = ff.output(output_stream, 'static/output/output.mp4',c="copy")'''

def trim_video(input_file, output_file, start_time, end_time):
    ffmpeg_cmd = f'ffmpeg -i {input_file} -ss {start_time} -to {end_time} -c:v copy -c:a copy {output_file}'
    subprocess.call(ffmpeg_cmd, shell=True)
ff.run(output_stream)
