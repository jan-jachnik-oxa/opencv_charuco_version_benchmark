import cv2 as cv
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--old-api", action='store_true', help="Use old API")

args = parser.parse_args()

if args.old_api:
    print("Testing old api")
else:
    print("Testing new api")


frame = cv.imread("BoardImage.jpg", cv.IMREAD_GRAYSCALE)
dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_5X5_250)

if args.old_api:
    board = cv.aruco.CharucoBoard_create(24,17, 0.03, 0.022, dictionary)
    detector_parameters = cv.aruco.DetectorParameters_create()
    detector_parameters.cornerRefinementMethod = cv.aruco.CORNER_REFINE_NONE
else:
    board = cv.aruco.CharucoBoard((24,17), 0.03, 0.022, dictionary)
    detector_parameters = cv.aruco.DetectorParameters()
    detector_parameters.cornerRefinementMethod = cv.aruco.CORNER_REFINE_NONE

    aruco_detector = cv.aruco.ArucoDetector(dictionary, detector_parameters);
    charuco_detector = cv.aruco.CharucoDetector(board)
    charuco_detector.setDetectorParameters(detector_parameters)


tm_detect_markers = cv.TickMeter()
tm_detect_charuco = cv.TickMeter()

for i in range(10):
    # Detect Aruco
    tm_detect_markers.start()
    if args.old_api:
        markers_corners, markers_ids,_  = cv.aruco.detectMarkers(frame, dictionary, parameters=detector_parameters)
    else:
        markers_corners, markers_ids,_ = aruco_detector.detectMarkers(frame)
    tm_detect_markers.stop()

    # Detect CharuCo
    tm_detect_charuco.start()
    if args.old_api:
        retval, charuco_corners, charuco_ids = cv.aruco.interpolateCornersCharuco(markers_corners, markers_ids, frame, board)
    else:
        charuco_corners, charuco_ids, markers_corners, markers_ids = charuco_detector.detectBoard(frame, markerCorners=markers_corners, markerIds=markers_ids)
    tm_detect_charuco.stop()

print(f"Number of Aruco markers detected: {len(markers_ids)}")
print(f"Number of Charuco corners detected: {len(charuco_corners)}")
print(f"Time to detect markers: {tm_detect_markers.getAvgTimeSec()}")
print(f"Time to detect charuco: {tm_detect_charuco.getAvgTimeSec()}")

