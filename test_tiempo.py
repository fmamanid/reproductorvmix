from datetime import datetime, timedelta


fecha = datetime.now()

tiempo_transcurrido = timedelta(seconds=120)

nuevo_tiempo = fecha + tiempo_transcurrido

print(nuevo_tiempo)