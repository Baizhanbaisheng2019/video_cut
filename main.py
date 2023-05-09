from moviepy.editor import VideoFileClip
import math

def split_video(input_video, output_folder, num_segments):
    clip = VideoFileClip(input_video)
    duration = clip.duration
    segment_duration = duration / num_segments

    for i in range(num_segments):
        start_time = i * segment_duration
        end_time = (i + 1) * segment_duration if i < num_segments - 1 else duration
        output_path = f"{output_folder}/output_segment_{i+1}.mp4"

        subclip = clip.subclip(start_time, end_time)
        subclip.write_videofile(output_path, codec="libx264", audio_codec="aac")
        print(f"Created segment {i+1}: {output_path}")

    clip.close()

input_video = "G:\FFOutput/video2.mp4"
output_folder = "G:\FFOutput\cut2"
num_segments = 14

split_video(input_video, output_folder, num_segments)
