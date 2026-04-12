# Prompt: Setup Data

## Objetivo
Configurar y validar los archivos JSON base del generador de CV.

## Instrucciones

### 1. Verificar estructura de datos
Asegúrate de que existan estos archivos en `/data`:
- `profile_master.json` - Información personal, formación, certificaciones
- `roles.json` - Experiencia laboral detallada
- `projects.json` - Proyectos destacados con logros
- `achievements.json` - Logros profesionales categorizados
- `skills.json` - Competencias técnicas y blandas

### 2. Validar JSON
Ejecuta el validador para confirmar que todos los archivos son JSON válido:
```bash
python validate_json.py
```

### 3. Principios de datos
- ✅ Solo información real y verificada
- ✅ Sin duplicados entre archivos
- ✅ Textos concisos y directos
- ✅ IDs relacionales entre archivos (role_id, project_id)
- ✅ Estructura consistente en todos los archivos

### 4. Actualización de datos
Para agregar nueva información:
1. Identifica el archivo correcto según tipo de información
2. Sigue la estructura JSON existente
3. Mantén consistencia en IDs y referencias
4. Valida el JSON después de cada cambio
5. Actualiza solo la información necesaria

## Ejemplo de flujo
```
Usuario: "Agrega mi nuevo proyecto X"
→ Abrir projects.json
→ Agregar entrada con estructura consistente
→ Vincular con role_id correspondiente
→ Validar JSON
→ Confirmar cambio
```
