
import libusb

# Inicializar la biblioteca libusb
context = libusb.init()

# Buscar el dispositivo USB
dev = libusb.get_device_list(context)[0]

# Abrir el dispositivo USB
handle = libusb.open_device(dev)

# Leer datos del dispositivo USB
data = libusb.read_bulk(handle, 1, 1024)

# Imprimir los datos leídos
print(data)

# Cerrar el dispositivo USB
libusb.close_device(handle)

# Liberar la biblioteca libusb
libusb.exit(context)

