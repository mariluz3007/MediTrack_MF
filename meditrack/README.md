# Meditrack

Esqueleto inicial de una aplicación Flask para gestionar medicamentos.

## Ejecutar

Desde esta carpeta, activa el entorno virtual que creaste en la carpeta superior:

```powershell
..\venv\Scripts\Activate.ps1
python run.py
```

La aplicación queda disponible en `http://127.0.0.1:5000`.

Para definir una clave propia en PowerShell antes de iniciar:

```powershell
$env:SECRET_KEY = "reemplaza-esto-por-una-clave-segura"
```

## Pruebas

```powershell
pytest
```

La conexión predeterminada usa SQLite. La estructura incluye los archivos base; los modelos, formularios, rutas y pantallas funcionales quedan pendientes de completar.
