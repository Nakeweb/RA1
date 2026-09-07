#ips_servidores = ["192.168.1.10","192.168.1.11","192.168.1.12"]

#print(ips_servidores[1])
#print(ips_servidores[2])

#ips_servidores.append("10.0.0.14")
#print(ips_servidores[3])

router = {
    "hostname": "Router1",
    "ip_adress": "192.168.1.1",
    "model": "Cisco 2900",
    "activo": True
}
#print(router["hostname"])
#print(router["model"])

#router["model"] = "Cisco 2911"
#router["puertos"] = 24

#print(router["model"])
#print(router["puertos"])

estado = "up"
vlan = 10

if estado == "up":
    print("El router esta activo")
else:
    print("El router esta inactivo")

vlans_permitidas = [10, 20, 30, 40, 50]
if vlan in vlans_permitidas:
    print("La VLAN esta permitida")
else:
    print("La VLAN no esta permitida")

with open("config.txt", "w") as archivo:
    archivo.write(f"Modelo del router: {router['model']}")