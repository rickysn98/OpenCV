import cv2

#camara encendida
cap = cv2.VideoCapture(0)

#mientras no cierre la camara
while(cap.isOpened()):
    
    #flag: bandera para saber si camara sigue prendida
    #frame: recibir imagen por imagen de video
    flag, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # Mi ventana se llama Video1 y voy a reproducir frame por frame
    cv2.imshow("Video1",gray)

    # Si escribo la letra q se cierra el ciclo
    #tomara una foto al presionar q
    if cv2.waitKey(1) == ord("q"):
        cv2.imwrite("captura de intruso.jpg", gray)
        break

# Cierra la camara
cap.release()

cv2.destroyAllWindows()