# Paper Digest — lista curada mensual

Tú decides qué papers entran (revisando el volumen del mes de tus
revistas de referencia) y escribes tú mismo el resumen, implicaciones,
preguntas abiertas y campo de estudio de cada uno en `papers.json`. El
script no llama a ninguna API externa ni resume nada: solo coge el
siguiente paper de la lista, en orden, y lo manda por email tal cual lo
escribiste. Es el mismo patrón que el proyecto de las fábulas de Esopo.

## Flujo mensual

1. A principios de mes, repasas los volúmenes nuevos de tus revistas de
   referencia (ver lista más abajo) y eliges los papers que te interesan.
2. Por cada uno, añades un objeto en `papers.json` con tu propio resumen,
   implicaciones, preguntas y campo de estudio ya escritos.
3. El workflow diario coge el siguiente de la lista (`state/state.json`
   guarda por dónde vas) y te lo manda.
4. Cuando se acaban los papers de `papers.json`, el workflow no falla,
   simplemente no envía nada ese día — hasta que añadas más.

## Formato de `papers.json`

```json
{
  "title": "Título exacto",
  "authors": "Apellido1 et al.",       // opcional
  "journal": "Nombre de la revista",   // opcional pero recomendado
  "year": "2026",                      // opcional
  "url": "https://doi.org/10.xxxx/xxxxx", // opcional
  "category": "Cardiología computacional",
  "resumen": "Tu resumen del paper",
  "implicaciones": "Por qué importa / a quién le sirve",
  "preguntas_abiertas": "Preguntas para reflexionar",
  "campo_estudio": "Subcampo concreto",
  "notes": "Opcional: por qué te interesó"
}
```

Solo `title` y `category` son estrictamente necesarios para que el script
no falle; el resto son los campos que realmente dan contenido al email,
así que en la práctica los rellenarás todos.

## Puesta en marcha

1. Sube este contenido a un repo de GitHub.
2. Secrets necesarios en `Settings → Secrets and variables → Actions`:
   - `GMAIL_ADDRESS`
   - `GMAIL_APP_PASSWORD` (contraseña de aplicación de Gmail)
   - `RECIPIENT_EMAIL`
3. Rellena `papers.json` con tus primeros papers del mes.
4. Lanza el workflow manualmente ("Run workflow" en la pestaña Actions)
   para probarlo, o espera al cron diario (06:00 UTC).

## Revistas de referencia por tema

- **Redes neuronales / deep learning**: IEEE TNNLS, IEEE TPAMI, JMLR, Neural Networks
- **Cardiología computacional**: IEEE JBHI, Computers in Biology and Medicine, npj Digital Medicine, Circulation
- **Diabetes y metabolismo**: Diabetes Care, Diabetologia, The Lancet Diabetes & Endocrinology, Nutrients
- **Bioseñales**: Journal of Neural Engineering, IEEE Trans. Biomedical Engineering, Biomedical Signal Processing and Control, Sensors
- **Fisiología espacial**: npj Microgravity, Aerospace Medicine and Human Performance, Frontiers in Physiology
- **Datos clínicos / interoperabilidad**: JAMIA, Journal of Biomedical Informatics, npj Digital Medicine
- **Metodología**: Statistics in Medicine, BMC Medical Research Methodology, PLOS Computational Biology
- **Multidisciplinares**: Nature Machine Intelligence, Nature Biomedical Engineering

## Coste

Cero. No hay llamadas a ninguna API de pago — solo GitHub Actions (gratis
para repos personales dentro de los límites normales) y Gmail SMTP.
