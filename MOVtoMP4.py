import moviepy.editor as moviepy
fromPath = input("Enter path of the file from: ")
toPath = input("Enter path of the file to: ")
clip = moviepy.VideoFileClip(fromPath)
clip.write_videofile(toPath)