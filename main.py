import cv2

# Carga las dos imágenes que se van a utilizar para calcular el flujo óptico
img1 = cv2.imread('imagen1.jpg')
img2 = cv2.imread('imagen2.jpg')

# Convierte las imágenes a escala de grises para simplificar el cálculo
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Crea un objeto para almacenar los vectores de flujo óptico
flow = cv2.calcOpticalFlowFarneback(gray1, gray2, None, 0.5, 3, 15, 3, 5, 1.2, 0)

# Dibuja los vectores de flujo óptico en la imagen
h, w = img1.shape[:2]
y, x = np.mgrid[0:h, 0:w]
plt.quiver(x, y, flow[:,:,0], flow[:,:,1], color='r')
plt.show()

###################################################
import cv2
import numpy as np

# Cargamos las imágenes
prev_frame = cv2.imread("imagen1.jpg")
next_frame = cv2.imread("imagen2.jpg")

# Convertimos a escala de grises
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
next_gray = cv2.cvtColor(next_frame, cv2.COLOR_BGR2GRAY)

# Calculamos el flujo óptico
flow = cv2.calcOpticalFlowPyrLK(prev_gray, next_gray, None, None)

# Dibujamos los vectores de flujo óptico sobre la imagen
img_flow = cv2.drawOptFlowMap(prev_gray, flow, None, (0, 255, 0), 3)

# Mostramos el resultado
cv2.imshow("Optical Flow", img_flow)
cv2.waitKey(0)
cv2.destroyAllWindows()

