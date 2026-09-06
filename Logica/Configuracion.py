router: dict[str, str | int | bool] = {
    "marca": "Cisco",
    "ip_lan": "10.0.1.1",
    "estado": "Inactivo",
    "puertos_abiertos": 4,
}

# Modificar el estado del router a activo
router["estado"] = "Activo"

# Sumar 2 al numero de puertos abiertos
valor: int = router["puertos_abiertos"]  # type: ignore
router["puertos_abiertos"] = valor + 2

# Agregar una nueva clave al dictionario
router["firewall"] = True

print("Configuracion Del Router")
print(router)
