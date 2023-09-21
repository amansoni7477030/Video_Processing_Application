import cv2
import json
import os
import mysql.connector
from datetime import datetime
import logging
from multiprocessing import Pool

# Configure logging
logging.basicConfig(filename='error.log', level=logging.ERROR)

# Step 1: Configuration
config = {
    'video_file_paths': [
        'C:\\Users\\Aman soni\\Pictures\\Aman_soni_task1.mp4',  # Add paths to all video streams
        'C:\\Users\\Aman soni\\Pictures\\Aman_soni_task2.mp4',  # Example for a second camera stream
    ],
    'duration': 162,  # Video duration in seconds
    'mysql': {
        'host': 'localhost',
        'user': 'root',#Enter username of MySQL
        'password': '12345678',#Enter password of MySQL
        'database': 'aman',#Enter database name
    }
}

# Step 2: Video Stream Ingestion
def video_stream(video_path):
    cap = cv2.VideoCapture(video_path)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        yield frame

# Step 3: Frame Processing
output_dir = 'frames'
os.makedirs(output_dir, exist_ok=True)

def process_frame(args):
    frame, frame_id, camera_id, geo_location = args
    try:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Save one frame per second as an image
        if frame_id % 25 == 0:
            image_path = os.path.join(output_dir, f'{frame_id // 25}.jpg')
            cv2.imwrite(image_path, frame)
        else:
            image_path = None

        frame_info = {
            'camera_id': camera_id,
            'frame_id': frame_id,
            'geo_location': geo_location,
            'image_path': image_path,
        }
        
        # Write frame info to a JSON file
        with open('frame_info.json', 'a') as f:
            json.dump(frame_info, f)
            f.write('\n')
    
    except Exception as e:
        logging.error(f"Error processing frame {frame_id}: {str(e)}")

# Step 4: Batching
def batch_frame(frame_id):
    try:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Store batch_data in the database
        db_config = config['mysql']
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        cursor.execute("""
            INSERT INTO batches (starting_frame_id, ending_frame_id, timestamp)
            VALUES (%s, %s, %s)
        """, (frame_id, frame_id, timestamp))
        
        connection.commit()
        connection.close()
    
    except Exception as e:
        logging.error(f"Error batching frame {frame_id}: {str(e)}")

# Step 5: Data Storage
db_config = config['mysql']
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Create tables if they don't exist
try:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS batches (
            id INT AUTO_INCREMENT PRIMARY KEY,
            starting_frame_id INT,
            ending_frame_id INT,
            timestamp TIMESTAMP
        )
    """)
except Exception as e:
    logging.error(f"Error creating batches table: {str(e)}")

# Commit changes and close the connection when done
connection.commit()
connection.close()

if __name__ == '__main__':
    frame_id = 0
    pool = Pool(processes=len(config['video_file_paths']))  # Create a pool of processes
    
    for video_path in config['video_file_paths']:
        for frame in video_stream(video_path):
            # Step 3: Frame Processing
            camera_id = config['video_file_paths'].index(video_path) + 1  # Assign a camera ID
            args = (frame, frame_id, camera_id, 'location_xyz')
            pool.apply_async(process_frame, (args,))
            
            # Step 4: Batching (Create a new batch for every frame)
            pool.apply_async(batch_frame, (frame_id,))
            
            frame_id += 1
    
    pool.close()
    pool.join()
