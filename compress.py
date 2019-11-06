import ffmpeg
import os
import sys

path = sys.argv[1]

for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith('.mp4'):
            os.rename(root+'/'+file, root+'/converting.mp4')
            (
                ffmpeg
                .input(root+'/converting.mp4')
                .output(root+'/'+file, **{'crf': 30, 'preset': 'slow'})
                .run()
            )
            os.remove(root+'/'+'/converting.mp4')
