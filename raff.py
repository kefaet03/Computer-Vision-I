import cv2
import numpy as np

def draw_contours_and_reorder(image):
    """
    Draws contours in the four corners of the document and returns reordered coordinates.

    Args:
        image: The input image.

    Returns:
        image_copy: The image with drawn contours.
        reordered_corners: A list of reordered corner coordinates.
    """

    image_copy = image.copy()  # Avoid modifying the original image
    contours, hierarchy = cv2.findContours(image_copy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Initialize empty lists for detected corners and desired order
    detected_corners = []
    desired_order = [(0, 0), (image_copy.shape[1] - 1, 0), (image_copy.shape[1] - 1, image_copy.shape[0] - 1), (0, image_copy.shape[0] - 1)]

    for cnt in contours:
        area = cv2.contourArea(cnt)
        # Adjust tolerance based on your actual area variability
        if abs(area - 717.0) <= 50:  # Allow for some area variation
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            # Ensure the contour has four corners
            if len(approx) == 4:
                detected_corners.append(approx.ravel())

    # Check if all four corners are detected
    if len(detected_corners) != 4:
        print("Warning: Not all four corners were detected.")
        return image_copy, None

    # Reorder detected corners based on desired order using distance matching
    reordered_corners = [None] * 4
    for i in range(4):
        min_dist, min_index = float('inf'), None
        for j in range(len(detected_corners)):
            if not detected_corners[j]:
                continue
            dist = np.linalg.norm(desired_order[i] - detected_corners[j])
            if dist < min_dist:
                min_dist, min_index = dist, j
        reordered_corners[i] = detected_corners[min_index]
        detected_corners[min_index] = None  # Mark used corner

    # Draw contours on the image
    for cnt in reordered_corners:
        if cnt is not None:  # Check if corner was found
            cv2.drawContours(image_copy, [cnt.reshape(-1, 1, 2)], -1, (0, 255, 0), 2)

    return image_copy, reordered_corners

# Example usage
image = cv2.imread("F:\He_is_enough03 X UniqoXTech X Dreams\Academic\cse 2102\project\OpenCV\OMR Project\Trial Pictures\Trial01.jpg")
image_with_contours, corners = draw_contours_and_reorder(image)

if corners is not None:
    # Use the reordered corners for further processing, e.g., perspective wrap
    print("Reordered corners:", corners)
else:
    print("Corner detection failed.")

cv2.imshow("Image with Contours", image_with_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()
