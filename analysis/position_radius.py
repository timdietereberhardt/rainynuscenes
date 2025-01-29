import os
import cv2
import numpy as np
import csv

# Function to calculate x, y, size for each region and save them along with the filename to a CSV file
def calculate_and_save_xy_size_to_csv(input_dir, output_csv_path):
    # Prepare a list to hold the filename, x, y, size data
    inputs = []

    # Iterate through all PNG files in the directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.png'):
            input_image_path = os.path.join(input_dir, filename)
            image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

            # Invert the image to detect black regions as foreground
            _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

            # Find contours of the black regions
            contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Loop over each contour to calculate x, y, size
            for contour in contours:
                # Calculate the moments to find the centroid
                M = cv2.moments(contour)
                if M['m00'] != 0:
                    cx = int(M['m10'] / M['m00'])
                    cy = int(M['m01'] / M['m00'])
                else:
                    cx, cy = 0, 0
                
                # Normalize centroid (x, y) relative to image dimensions
                #normalized_x = cx / image.shape[1]
                #normalized_y = cy / image.shape[0]

                # Calculate the size as the square root of the area
                area = cv2.contourArea(contour)
                radius = np.sqrt(area)/np.pi
                #normalized_size = size / max(image.shape)

                # Append the filename, normalized x, y, size to the list
                inputs.append([filename, cx, cy, radius])

    # Write the inputs to a CSV file
    with open(output_csv_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['image_filename', 'x', 'y', 'size'])  # CSV header

        # Write the filename, x, y, size values for each region
        for row in inputs:
            writer.writerow(row)

    print(f"Saved x, y, size data to {output_csv_path}")


