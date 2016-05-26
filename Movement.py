import cv2

#####################################################################
#         DEVELOPED BY ENDER - KUSTAS - CYBER SECURITY              #
#####################################################################

cam = cv2.VideoCapture(0)

winName = "Movement Indicator"

incfilename = 0

def diffImg(t0, t1, t2):
  
  d1 = cv2.absdiff(t2, t1) #input array or a scalar.
  d2 = cv2.absdiff(t1, t0) 
  
  return cv2.bitwise_and(d1, d2) #conjunction of two arrays


# Read three images first @Array:
t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
#print "t_minus",t_minus 
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
#print "t",t
t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
#print "t_plus",t_plus



while True:
  ret, frame = cam.read()
  cv2.imshow( winName, diffImg(t_minus, t, t_plus) )
  
  d1 = cv2.absdiff(t_plus, t)
  d2 = cv2.absdiff(t, t_minus)
  
  if ((d1 > 500).any() or (d2 >200).any()):

    cv2.imwrite("picture%s.jpg" %str(incfilename),frame)
    incfilename = incfilename + 1
    print incfilename
  # Read next image
  t_minus = t
  t = t_plus
  t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    
 
  key = cv2.waitKey(10)
  if key == 27:
    cv2.destroyWindow(winName)
    break

print "Goodbye"
