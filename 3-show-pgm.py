import cv2

for count in range(6,10):
    filename = './training-set/%s.pgm' % str(count)
    img = cv2.imread(filename);
    #img.convertTo(img, CV_8U, 255.0 / 4096.0);

    cv2.namedWindow('gopnix Detected!!')

    cv2.imshow('gopnix Detected!!', img);
    #waitKey();
