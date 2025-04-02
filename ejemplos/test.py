from tkinter import *
from classLogoVmix import *
from classVideoVmix import *
import time
import time

inicio =int(time.time())
print(f"inicio:            {inicio:12d}")
time.sleep(3)
parada=int(time.time())
print(f"parada:            {parada:12d}")
diferencia = parada - inicio
print(f"delay:            {diferencia:12d}")
print(diferencia)

quit()




logo = AppLogoVmix(variables.direccionLogo)
logo.cargarLogo()
logo.reproduceLogo(variables.testDireccion2)

quit()


video1 = AppVideoVmix(variables.testDireccion)

video2=AppVideoVmix(variables.testDireccion2)

video3 = AppVideoVmix(variables.testDireccion3)

video4 =AppVideoVmix(variables.testDireccion4)

video1.cargarVideo()
time.sleep(1)
video1.cargarPreview()
time.sleep(1)
video1.reproducirVideo()
#logo.reproduceLogo(variables.testDireccion)
time.sleep(1)
video2.cargarVideo()
time.sleep(1)
video2.cargarPreview()

video1.esperarVideo()

video2.reproducirVideo()
#logo.reproduceLogo(variables.testDireccion2)
time.sleep(1)
video3.cargarVideo()
time.sleep(1)
video3.cargarPreview()
time.sleep(1)
video1.cerrarVideo()

video2.cerrarVideo()

video3.reproducirVideo()
#logo.reproduceLogo(variables.testDireccion3)
time.sleep(1)
video4.cargarVideo()
time.sleep(1)
video4.cargarPreview()
time.sleep(1)
video2.cerrarVideo()

video3.esperarVideo()

video4.reproducirVideo()
#logo.reproduceLogo(variables.testDireccion4)
time.sleep(1)
video3.cerrarVideo()

video4.esperarVideo()

video4.cerrarVideo()
