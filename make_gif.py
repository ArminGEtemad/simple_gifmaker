from moviepy.video.io.VideoFileClip import VideoFileClip
import argparse
import os

def make_gif(input_path, start, end, width, loop_count, output_path):
    clip = VideoFileClip(input_path).subclipped(start, end)
    clip = clip.resized(width=width)
    clip.write_gif(output_path, loop=loop_count)
    print(f"GIF saved to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert video to looping GIF.")
    parser.add_argument("input", help="Input video file")
    parser.add_argument("--start", type=float, default=0.0, help="Start time in seconds")
    parser.add_argument("--end", type=float, default=3.0, help="End time in seconds")
    parser.add_argument("--width", type=int, default=480, help="width of output GIF")
    parser.add_argument("--loop", type=int, default=0, help="Loop count (0 -> infinite)")
    parser.add_argument("--output", default="output.gif", help="GIF name")

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print("Error! No such path lmao!")
    else:
        make_gif(args.input, args.start, args.end, args.width, args.loop, args.output)