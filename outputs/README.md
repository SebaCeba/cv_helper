# 📁 Outputs / CVs Generados

Esta carpeta contiene los **CVs generados** a partir de los datos estructurados en `/data`.

## 📄 CVs Disponibles

| Archivo | Formato | Descripción |
|---------|---------|-------------|
| `CV_Head_Plataformas.md` | Markdown | CV en formato Markdown - énfasis en plataformas y transformación digital |
| `CV_Ejecutivo_Corporativo.html` | HTML | CV con diseño corporativo - layout de dos columnas con sidebar |
| `CV_Ejecutivo_Minimalista.html` | HTML | CV con diseño minimalista - estilo moderno y limpio |

## 🎯 Propósito

Los archivos en esta carpeta son **resultados generados** desde la fuente única de verdad en `/data`.

- ✅ Estos CVs pueden regenerarse cuando se actualice `/data`
- ✅ Son ejemplos de diferentes formatos y estilos
- ✅ No deben editarse manualmente (los cambios se perderán al regenerar)

## 📂 Archive

La subcarpeta `/archive` contiene:
- Documentos de proceso históricos
- Resúmenes de organización del proyecto
- Material de referencia que no es parte del sistema activo

## 🔄 Para Generar Nuevos CVs

1. Actualiza la información en `/data/*.json`
2. Usa los prompts en `/prompts/generate_cv.md`
3. Aplica los templates de `/templates`
4. Guarda los outputs generados aquí

---

**Nota**: Esta carpeta está configurada en `.gitignore` para no versionar CVs generados automáticamente (excepto `.gitkeep` y este README).
