import ffmpeg as ff
input_stream = ff.input('static/input/videoplayback.mp4')
output_stream = ff.trim(input_stream, start='00:00:10', end='00:01:20')
output_stream = ff.output(output_stream, 'static/output/output.mp4')
ff.run(output_stream)
