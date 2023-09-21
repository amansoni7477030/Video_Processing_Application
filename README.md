# Video_Processing_Application
1. Introduction
Purpose of the Application
The Video Processing Application is designed to process video streams from multiple sources, extract frames, perform batch processing, and store relevant data in a database. This application is useful for various purposes such as surveillance, data analysis, and more.
Key Features
•	Ingest video streams from multiple cameras simultaneously.
•	Extract frames from the video streams and save them as image files.
•	Create batches of frames based on the specified duration.
•	Store batch information in a MySQL database.
•	Handle errors gracefully and log relevant information for debugging.
•	Achieve concurrent processing of frames from different cameras for improved performance.
2. System Requirements
Hardware Requirements
•	Modern computer i3 5th generation and above with sufficient CPU and RAM.
•	One or more cameras or video sources.
•	Adequate storage space for saving frames and data.
Software Requirements
•	Operating System: Windows, Linux, or macOS.
•	Python 3.x installed.
•	Required Python packages: OpenCV, json, mysql.connector, logging, multiprocessing.
3. Getting Started
Installation
1.	Ensure you have Python 3.x installed on your system.
2.	Install the required Python packages using pip:
   pip install opencv-python json mysql-connector-python logging 
Configuration
1.	Modify the video_file_paths list to include the paths to your video streams.
2.	Adjust other configuration parameters as needed, such as database credentials and duration.
4. Using the Application
Video Stream Ingestion
•	The application can ingest video streams from multiple cameras simultaneously.
•	Add the paths to your video streams in the video_file_paths list in the configuration.
Frame Processing
•	Frames are extracted from the video streams and saved as image files.
•	One frame per second is saved as an image.
•	Frame information, including camera ID and image path, is logged to a JSON file.
Batching
•	Batches of frames are created based on the specified duration in the configuration.
•	Each batch includes information such as batch ID, starting frame ID, ending frame ID, and a timestamp.
•	Batch information is stored in a MySQL database.
Data Storage
•	The application stores batch information in a MySQL database.
•	A table named "batches" is created to store this information.
•	Batch data includes batch ID, starting frame ID, ending frame ID, and a timestamp.
5. Error Handling and Logging
•	The application includes error handling mechanisms to capture and handle exceptions.
•	Errors are logged in an "error.log" file, including details about the error and the frame or batch causing the error.
•	Logging helps in debugging and troubleshooting issues.
6. Concurrency and Performance
•	The application is designed to achieve concurrent processing of frames from different cameras.
•	It uses the multiprocessing library to create a pool of processes, one for each camera stream.
•	Concurrent processing improves the performance of the application.
7. Documentation and Comments
•	The code is well-documented with comments that explain the purpose and functionality of key functions and classes.
•	This documentation helps developers understand and maintain the code.
8. Conclusion
The Video Processing Application is a powerful tool for processing video streams, extracting frames, and storing batch information in a database. It offers flexibility, error handling, and concurrent processing to meet various use cases. With proper configuration and usage, it can be a valuable asset for tasks such as surveillance, data analysis, and more.
For any questions or support, please contact
Name = Aman Soni
Mail id = amansoni7477030@gmail.com
