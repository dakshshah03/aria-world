# split an input video into frames
import argparse
import os
import cv2
from tqdm import tqdm

def extract_frames(input_video, output_dir, frame_step=1):
    """
    Extract frames from a video file and save them to the specified output directory.
    
    Args:
        input_video (str): Path to the input video file.
        output_dir (str): Path to the output directory where frames will be saved.
        frame_step (int): Extract every nth frame (default: 1, which extracts all frames).
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Open the video file
    vidcap = cv2.VideoCapture(input_video)
    
    # Get video properties
    frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    
    print(f"Processing video: {input_video}")
    print(f"Total frames: {frame_count}")
    print(f"FPS: {fps}")
    print(f"Extracting every {frame_step}th frame")
    
    # Extract frames
    count = 0
    saved_count = 0
    
    with tqdm(total=frame_count, desc="Extracting frames") as pbar:
        success = True
        while success:
            success, image = vidcap.read()
            
            if success:
                # Save frame if it's a multiple of frame_step
                if count % frame_step == 0:
                    frame_path = os.path.join(output_dir, f"frame_{saved_count:06d}.jpg")
                    cv2.imwrite(frame_path, image)
                    saved_count += 1
                
                count += 1
                pbar.update(1)
    
    print(f"Successfully extracted {saved_count} frames to {output_dir} (skipping every {frame_step-1} frames)")
    vidcap.release()

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Split a video into frames')
    parser.add_argument('-i', '--input', required=True, help='Path to input video file')
    parser.add_argument('-o', '--output', required=True, help='Path to output directory')
    parser.add_argument('-s', '--step', type=int, default=1, help='Extract every nth frame (default: 1)')
    args = parser.parse_args()
    
    # Check if input file exists
    if not os.path.isfile(args.input):
        print(f"Error: Input file '{args.input}' does not exist")
        return
    
    # Extract frames
    extract_frames(args.input, args.output, args.step)

if __name__ == "__main__":
    main()
