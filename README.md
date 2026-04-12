# 📄 CV Helper

Sistema modular de generación de CVs profesionales basado en archivos JSON estructurados.

> **Proyecto**: Generador de CV personalizable  
> **Autor**: Sebastián Ceballos  
> **Última actualización**: Abril 2026

## 🎯 Descripción

CV Helper es un sistema de gestión de información profesional que permite mantener toda tu experiencia, habilidades y logros en formato JSON estructurado. Esto facilita:

- ✅ **Generación de múltiples formatos** de CV (HTML, Markdown, PDF)
- ✅ **Personalización por rol** o industria específica
- ✅ **Mantenimiento centralizado** de información profesional
- ✅ **Eliminación de duplicados** y datos inconsistentes
- ✅ **Versionado y control** de tu historia profesional

## 📁 Estructura del Proyecto

```
.
├── data/                          # Datos estructurados del CV
│   ├── profile_master.json        # Información personal, formación, idiomas
│   ├── roles.json                 # Experiencia profesional
│   ├── projects.json              # Proyectos destacados
│   ├── achievements.json          # Logros profesionales
│   └── skills.json                # Habilidades técnicas y blandas
├── CV_Ejecutivo_Corporativo.html  # Template CV corporativo
├── CV_Ejecutivo_Minimalista.html  # Template CV minimalista
├── CV_Sebastian_Ceballos_Head_Plataformas.md  # CV formato Markdown
└── validate_json.py               # Script de validación
```

## 📊 Descripción de Archivos JSON

### `profile_master.json`
Información base del perfil:
- **personal**: Datos de contacto (nombre, título, ubicación, email, LinkedIn)
- **profile_summary**: Resumen ejecutivo profesional
- **education**: Formación académica (2 títulos)
- **certifications**: Certificaciones profesionales (3 certificaciones)
- **languages**: Idiomas (Español, Inglés)
- **differentials**: 4 diferenciales profesionales clave

### `roles.json`
Experiencia laboral organizada por roles:
- **3 roles profesionales** desde 2015 a la actualidad
- Por cada rol: empresa, cargo, fechas, responsabilidades, tecnologías
- Roles identificados: `role_001`, `role_002`, `role_003`

### `projects.json`
Proyectos específicos de alto impacto:
- **5 proyectos destacados** vinculados a roles
- Por proyecto: nombre, descripción, logros, tecnologías, año
- Proyectos: OneStream, Power BI, P&L, IA/Automatización, Arquitecturas

### `achievements.json`
Logros profesionales categorizados:
- **7 logros** clasificados por tipo
- Categorías: Leadership, Implementation, Innovation, Modernization, Standardization, Governance, Change Management
- Cada logro vinculado a un `role_id`

### `skills.json`
Competencias técnicas y blandas:
- **expertise_areas**: 6 áreas de expertise core
- **technologies**: 4 categorías tecnológicas con niveles de proficiencia
  - Plataformas Financieras (4 items)
  - Data & Analytics (3 items)
  - Automatización & IA (3 items)
  - Ecosistemas (2 items)
- **soft_skills**: 6 habilidades blandas clave

## ✅ Validación

Ejecutar script de validación:
```powershell
python validate_json.py
```

Estado actual: **✓ TODOS LOS ARCHIVOS JSON SON VÁLIDOS**

## 🎯 Principios de Diseño

1. **Sin inventar información**: Solo datos existentes de CVs originales
2. **Sin duplicados**: Información única en cada archivo
3. **Textos concisos**: Información clara y directa
4. **Estructura modular**: Fácil actualización y mantenimiento
5. **JSON válido**: Verificado programáticamente

## � Inicio Rápido

### Validar archivos JSON

```powershell
python validate_json.py
```

### Estructura de datos

Toda la información profesional está organizada en `/data`:
- **profile_master.json** → Información personal y formación
- **roles.json** → Experiencia laboral detallada  
- **projects.json** → Proyectos destacados
- **achievements.json** → Logros profesionales
- **skills.json** → Competencias técnicas y blandas

## 🛠️ Próximas Funcionalidades

- [ ] Generador automático HTML desde JSON
- [ ] Exportación a PDF
- [ ] Templates personalizables
- [ ] Filtros por industria/rol
- [ ] Integración con LinkedIn API
- [ ] Sistema de versionado de CVs

## 📊 Características

- 🔒 **Sin información inventada**: Solo datos verificados
- 🎨 **Modular**: Fácil actualización de secciones individuales
- ✅ **Validado**: JSON validado automáticamente
- 📝 **Documentado**: Cada archivo con propósito claro
- 🔗 **Relacional**: IDs conectan proyectos con roles

## 🤝 Contribuir

Este es un proyecto personal, pero si encuentras útil la estructura, ¡úsala libremente!

## 📝 Licencia

MIT License - Úsalo como plantilla para tu propio CV Helper

## 📞 Contacto

**Sebastián Ceballos**
- LinkedIn: [linkedin.com/in/sebaceba](https://linkedin.com/in/sebaceba)
- Email: sceballost@gmail.com

---

⭐ Si esta estructura te resulta útil, considera darle una estrella al repo
