# 🗓️ Día 12 - Automatización y Registro de Actividades

## 📌 Objetivo del día
Aplicar conocimientos de manejo de archivos, automatización de tareas comunes con scripts de Python y el uso de las librerías `datetime`, `shutil`, y `os` para registrar actividades, respaldar archivos y calcular fechas dinámicamente.

---

## ✅ Contenido aplicado

- 📂 **Automatización de respaldo de archivos** con cambio de nombre automático y registro de actividad en un archivo log.
- 🕒 **Uso de `datetime` y `timedelta`** para obtener la fecha actual y sumar o restar días.
- 🧱 **Uso de `shutil.copy`** para duplicar archivos antes de renombrarlos.
- 🧠 **Manejo de rutas y archivos con `os`**.
- 🧾 **Creación de logs** en archivos `.log` con marcas de tiempo precisas.
- 📥 **Organización del código en módulos reutilizables (`utilidades`)**.
- 🔄 **Validación de entrada entera del usuario desde consola**.

---

## 📂 Archivos involucrados

- `general_reporte.py`: Script principal que gestiona las funciones de respaldo, registro y cálculo.
- `utilidades.py`: Contiene funciones auxiliares como `validar_entero`.
- `actividad.log`: Archivo donde se registran los eventos con fecha y hora.
- 📁 Carpetas creadas automáticamente:
  - `backup/`
  - `log/`

---

## 🧪 Ejecución de ejemplo

```python
# Dentro de general_reporte.py
if __name__ == "__main__":
    main()
```

---

## ✍️ Comentarios
- Se modificó el nombre del método `renombrar_archivo` a `backup_archivo` para reflejar mejor su función principal.
- Esta práctica complementa lo pendiente del Día 11, integrando las tres librerías faltantes (`datetime`, `shutil`, `os`).
- Cumple con los requisitos de organización, respaldo seguro y trazabilidad.
