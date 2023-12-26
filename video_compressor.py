import os
import subprocess
from tkinter import filedialog, Tk, Label, Button, Scale, HORIZONTAL, Text, Scrollbar
import threading  # Importa el módulo threading

def comprimir_video(ruta_video, crf):
    ruta_temp = ruta_video + ".tmp"
    comando = [
        'ffmpeg',
        '-i', ruta_video,
        '-vcodec', 'libx264',
        '-crf', str(crf),
        '-preset', 'veryfast',  # Aumenta la velocidad de compresión
        '-y',
        '-f', 'mp4',  # Especificar explícitamente el formato de salida
        ruta_temp
    ]
    
    result = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    log.insert("end", f"Comando ejecutado: {comando}\n")
    log.insert("end", f"Salida: {result.stdout}\n")
    log.insert("end", f"Errores: {result.stderr}\n")
    
    if result.returncode == 0:
        os.remove(ruta_video)
        os.rename(ruta_temp, ruta_video)
        return True
    else:
        return False

def buscar_videos(carpeta):
    for raiz, dirs, archivos in os.walk(carpeta):
        for archivo in archivos:
            if archivo.lower().endswith(('.mp4', '.avi', '.mkv', '.mov')):
                yield os.path.join(raiz, archivo)

def seleccionar_carpeta():
    carpeta = filedialog.askdirectory()
    if carpeta:
        btn_comprimir['state'] = 'normal'
        btn_comprimir.carpeta = carpeta

def iniciar_compresion():
    # Deshabilita el botón mientras se comprimen los videos
    btn_comprimir['state'] = 'disabled'
    # Inicia la compresión en un hilo separado
    threading.Thread(target=compresion_en_background).start()

def compresion_en_background():
    crf = scale_crf.get()
    contador = 0
    for video in buscar_videos(btn_comprimir.carpeta):
        resultado = comprimir_video(video, crf)
        log.insert("end", f"{video}: {'Compresión exitosa' if resultado else 'Error al comprimir'}\n")
        if resultado:
            contador += 1
    label['text'] = f'Número de vídeos comprimidos: {contador}'
    # Habilita el botón nuevamente después de completar la compresión
    btn_comprimir['state'] = 'normal'

app = Tk()
app.title("Compresor de Vídeos")

label = Label(app, text="Elige una carpeta para comprimir los vídeos")
label.pack(pady=20)

btn_seleccionar = Button(app, text="Seleccionar Carpeta", command=seleccionar_carpeta)
btn_seleccionar.pack(pady=10)

label_crf = Label(app, text="Calidad de compresión (CRF):")
label_crf.pack(pady=10)

scale_crf = Scale(app, from_=28, to=35, orient=HORIZONTAL)  # Ajusta el rango de CRF
scale_crf.set(32)  # Establece un valor predeterminado en el medio del rango
scale_crf.pack(pady=10)

btn_comprimir = Button(app, text="Comenzar Compresión", command=iniciar_compresion, state='disabled')
btn_comprimir.pack(pady=20)

log = Text(app, height=10, width=50)
log.pack(pady=10)
scroll = Scrollbar(app, command=log.yview)
scroll.pack(side="right", fill="y")
log.config(yscrollcommand=scroll.set)

app.mainloop()
