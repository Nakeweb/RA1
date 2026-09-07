
nombre_usuario = "JosiasMampo"
puertos_activos = 24
precio_base = "1500.50"  

precio_num = float(precio_base)
descuento = 0.10
precio_final = precio_num * (1 - descuento)


direcciones_ip = ["192.168.1.1", "192.168.1.10", "10.0.0.1", "172.16.0.1"]


dispositivo = {
    "nombre": "Switch 01",
    "marca": "Cisco",
    "modelo": "Catalyst",
    "estado": "Activo",
    "ip_gestion": "192.168.1.1"
}

if dispositivo["estado"] == "Activo":
    prioridad_revision = "Baja"
    mensaje_estado = "El dispositivo opera dentro de los parámetros normales."
else:
    prioridad_revision = "Alta"
    mensaje_estado = "Atención requerida: El dispositivo se encuentra fuera de línea."

nombre_archivo = "reporte_dispositivo.txt"

with open(nombre_archivo, "w", encoding="utf-8") as archivo:
    archivo.write(f"Generado por: {nombre_usuario}\n")
    archivo.write(f"Dispositivo: {dispositivo['nombre']} ({dispositivo['marca']} {dispositivo['modelo']})\n")
    archivo.write(f"IP de gestión: {dispositivo['ip_gestion']}\n")
    archivo.write(f"Estado actual: {dispositivo['estado']}\n")
    archivo.write(f"Prioridad de revisión: {prioridad_revision}\n")
    archivo.write(f"Mensaje: {mensaje_estado}\n")
    archivo.write(f"Costo final estimado de mantenimiento: ${precio_final:.2f}\n")
    archivo.write("\nIPs Monitoreadas en la red:\n")
    for ip in direcciones_ip:
        archivo.write(f" - {ip}\n")

print(f"Programa ejecutado con éxito. El reporte ha sido guardado en '{nombre_archivo}'.")