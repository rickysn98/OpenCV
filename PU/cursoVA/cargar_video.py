import cv2

#camara encendida
cap = cv2.VideoCapture(0)

#mientras no cierre la camara
while(cap.isOpened()):
    
    #flag: bandera para saber si camara sigue prendida
    #frame: recibir imagen por imagen de video
    flag, frame = cap.read()

    # Mi ventana se llama Video1 y voy a reproducir frame por frame
    cv2.imshow("Video1",frame)

    # Si escribo la letra q se cierra el ciclo
    if cv2.waitKey(1) == ord("q"):
        break

# Cierra la camara
cap.release()

cv2.destroyAllWindows()
