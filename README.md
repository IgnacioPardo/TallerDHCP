# Taller DHCP - TDIV UTDT

- ¿Qué tipos de paquetes `DHCP` capturaron? ¿Capturaron todos los tipos de paquetes del protocolo? Explicar cuáles paquetes se envían por Broadcast y cuáles no.

Paquetes de tipo discover, request e inform. No capturamos paquetes de tipo Offer. Dejando de lado los paquetes inform, tanto request, offer y discover se envían por broadcast.

- ¿Qué tipos de mensajes son parte del protocolo `DHCP`?

Mensajes de tipo broadcast.

- ¿Qué tipo de protocolo usa el mensaje `Ping`?

Utiliza el protocolo `ARP`

- ¿Qué protocolo de la capa de transporte fue utilizado?

El protocolo `UDP`

- ¿Cuál es el IP del servidor?

La IP del servidor será donde esté corriendo el archivo `dhcp_server.py`

- ¿Cuál es la máscara de subred de la red utilizada?

Como estábamos conectados en una red clase $C$, la máscara subred es acorde, en este caso a la red $255.255.255.0$
