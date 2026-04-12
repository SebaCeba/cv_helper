# Comandos Git para Subir al Repositorio

## 🔧 Configuración Inicial

Si es la primera vez que usas Git en este proyecto:

```powershell
# Inicializar repositorio local
git init

# Configurar usuario (si no está configurado globalmente)
git config user.name "SebaCeba"
git config user.email "sceballost@gmail.com"

# Conectar con repositorio remoto
git remote add origin https://github.com/SebaCeba/cv_helper.git

# Verificar conexión
git remote -v
```

## 📤 Primer Push

```powershell
# Agregar todos los archivos
git add .

# Crear commit inicial
git commit -m "feat: estructura inicial del generador de CV

- Agregados 5 archivos JSON con datos estructurados
- Creados templates HTML (corporativo y minimalista)
- Añadido script de validación de JSON
- Documentación completa en README y RESUMEN_ORGANIZACIÓN
- Configuración de .gitignore para Python"

# Subir al repositorio (rama main)
git branch -M main
git push -u origin main
```

## 🔄 Actualizaciones Futuras

Para cambios posteriores:

```powershell
# Ver estado de archivos modificados
git status

# Agregar cambios específicos
git add data/profile_master.json

# O agregar todos los cambios
git add .

# Commit con mensaje descriptivo
git commit -m "update: actualización de experiencia laboral"

# Push
git push
```

## 📝 Convenciones de Commits

Usa prefijos semánticos:

- `feat:` - Nueva funcionalidad
- `update:` - Actualización de información
- `fix:` - Corrección de errores
- `docs:` - Cambios en documentación
- `refactor:` - Reestructuración de código
- `style:` - Cambios de formato

## ⚠️ Antes de cada Push

```powershell
# Validar JSONs
python validate_json.py

# Verificar qué se va a subir
git status
git diff
```

## 🌿 Trabajar con Ramas (Opcional)

Para cambios experimentales:

```powershell
# Crear nueva rama
git checkout -b feature/nueva-funcionalidad

# Trabajar en la rama...

# Volver a main
git checkout main

# Fusionar rama
git merge feature/nueva-funcionalidad
```

## 🔗 Links Útiles

- Repo: https://github.com/SebaCeba/cv_helper
- Documentación Git: https://git-scm.com/doc
