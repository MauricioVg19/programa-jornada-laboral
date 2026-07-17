# =====================================================================
# MATRIZ DE DATOS (Recurso, Lunes, Martes, Miércoles, Jueves, Viernes)
# =====================================================================
MATRIZ_HORAS = [
    ["Luisa Ramirez", 8, 8, 9, 8, 10],       # Total: 43 horas (Sobretiempo)
    ["Mauricio Gonzalez", 8, 7, 8, 8, 7],     # Total: 38 horas (Estándar)
    ["Manuela Ramirez", 9, 9, 10, 9, 8],     # Total: 45 horas (Sobretiempo)
    ["Juan Gonzalez", 8, 8, 8, 8, 8]       # Total: 40 horas (Estándar)
]

UMBRAL_ESTANDAR = 40

# =====================================================================
# MÓDULO / FUNCIÓN PRINCIPAL DE LÓGICA DE NEGOCIO
# =====================================================================
def procesar_jornada_laboral(registro_recurso: list, umbral: int) -> tuple:
    """
    Calcula el total de horas semanales de un recurso y clasifica su jornada.
    
    Args:
        registro_recurso (list): Lista que contiene [Nombre, H_Lun, H_Mar, ..., H_Vie]
        umbral (int): Límite de horas para el horario estándar.
        
    Returns:
        tuple: (total_horas, clasificacion)
    """
    nombre = registro_recurso[0]
    # Extraemos solo las horas (desde el índice 1 en adelante) y las sumamos
    horas_diarias = registro_recurso[1:]
    total_horas = sum(horas_diarias)
    
    # Clasificación según la lógica de negocio
    if total_horas > umbral:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"
        
    return total_horas, clasificacion

# =====================================================================
# FUNCIÓN PARA GENERAR EL REPORTE (SALIDA)
# =====================================================================
def generar_reporte_horas(matriz_datos: list):
    """
    Recorre la matriz de recursos, procesa sus datos e imprime el informe final.
    """
    print("=" * 65)
    print(f"{'RECURSO':<18} | {'TOTAL HORAS':<12} | {'CLASIFICACIÓN JORNADA'}")
    print("=" * 65)
    
    for recurso in matriz_datos:
        nombre = recurso[0]
        # Llamamos al módulo para procesar los datos
        total_horas, tipo_jornada = procesar_jornada_laboral(recurso, UMBRAL_ESTANDAR)
        
        # Imprimir salida con formato alineado
        print(f"{nombre:<18} | {total_horas:<12} | {tipo_jornada}")
        
    print("=" * 65)

# =====================================================================
# BLOQUE DE EJECUCIÓN
# =====================================================================
if __name__ == "__main__":
    generar_reporte_horas(MATRIZ_HORAS)