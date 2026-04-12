# Prompt: Generate CV

## Objetivo
Generar un CV personalizado desde los datos JSON estructurados.

## Instrucciones

### 1. Seleccionar información
Desde los archivos JSON en `/data`, selecciona:
- **Perfil**: Nombre, título, contacto, resumen (desde `profile_master.json`)
- **Experiencia**: Roles relevantes para el objetivo (desde `roles.json`)
- **Proyectos**: Proyectos que demuestren competencias clave (desde `projects.json`)
- **Logros**: Achievements alineados con el rol objetivo (desde `achievements.json`)
- **Skills**: Tecnologías y expertise relevantes (desde `skills.json`)

### 2. Personalizar según contexto
Si el usuario especifica un rol o industria objetivo:
- Filtrar proyectos más relevantes
- Destacar skills específicas
- Ajustar orden de información según prioridad
- Usar keywords de la industria objetivo

### 3. Formato de salida
Usa el template en `/templates/cv_template.md` como base.

Adapta según necesidad:
- **Ejecutivo**: Énfasis en liderazgo y logros de negocio
- **Técnico**: Énfasis en tecnologías y proyectos específicos
- **Consultor**: Balance entre negocio y tecnología
- **Startup**: Énfasis en versatilidad y adaptabilidad

### 4. Generar archivo
1. Cargar datos desde JSON
2. Filtrar información relevante
3. Aplicar template seleccionado
4. Generar en `/outputs/CV_[nombre]_[fecha].md`
5. Confirmar archivo creado

## Variables disponibles
```
{{full_name}}
{{title}}
{{email}}
{{linkedin}}
{{profile_summary}}
{{education}}
{{certifications}}
{{languages}}
{{roles}}
{{projects}}
{{achievements}}
{{skills}}
{{differentials}}
```

## Ejemplo de uso
```
Usuario: "Genera CV para rol de Head de Tecnología en retail"
→ Cargar todos los JSON
→ Filtrar proyectos relacionados con retail/plataformas
→ Destacar liderazgo tecnológico
→ Priorizar skills en arquitectura y transformación digital
→ Generar en /outputs/CV_Head_Tecnologia_Retail_2026-04-12.md
```
