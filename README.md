# table-line-detector

`vline_detector()` is a function for finding the pixel location of vertical lines in images of tables. `hline_detector()` is an analogous function for horizontal. These could be useful for cropping cells of tables before running OCR.

## usage

`image = cv2.imread(image_path)`

`coords, plot  = vline_detector(image)`

The x-axis of `plot` denotes the width of the image. Moving along the width of the image, we can count the number of pixels in each vertical slice that is recognised as a vertical edge. The y-axis of `plot` shows this count. Therefore the spikes in `plot` are the horizontal coordinates of detected vertical lines. `coords` is a list of the positions of these spikes (i.e. the horizontal coordinates of detected vertical lines).
