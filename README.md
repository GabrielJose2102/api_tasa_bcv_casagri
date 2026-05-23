# API Exchange Rate 💱

## 1. Cabecera de Presentación

| Atributo | Detalle |
| :--- | :--- |
| **Nombre Técnico** | `api_rate_currency` |
| **Nombre Comercial** | API Exchange Rate (BCV Automation) |
| **Autor** | Ing. Gabriel Torrealba (Software Engineer) |
| **Sistema de Destino** | Odoo 18.0 (Enterprise/Community) |
| **Lenguajes** | Python, XML |
| **Categoría** | Contabilidad / Localización |
| **Orientación** | Automatización de procesos financieros y cumplimiento cambiario. |

**Problema que resuelve:**  
En el contexto económico venezolano, la fluctuación diaria de las tasas de cambio emitidas por el Banco Central de Venezuela (BCV) exige una actualización constante y precisa. Este módulo elimina la carga administrativa de la carga manual, reduciendo el riesgo de errores humanos en la facturación y la contabilidad multi-moneda.

---

## 2. Lógica de Negocio

El módulo **API Exchange Rate** está diseñado para garantizar que la contabilidad de la empresa refleje siempre la realidad financiera oficial de Venezuela. 

### Puntos Clave:
*   **Sincronización Oficial:** Obtiene los valores de USD y EUR directamente desde fuentes vinculadas al BCV.
*   **Consistencia de Datos:** El sistema no solo actualiza el dólar, sino que recalcula la paridad del Euro basándose en la lógica nativa de Odoo, asegurando que todos los registros contables mantengan coherencia entre sí.
*   **Flexibilidad de Cálculo:** Permite a la gerencia financiera decidir si las tasas obtenidas deben ser **redondeadas** o **truncadas**, adaptándose a las políticas internas de cada empresa o a requerimientos específicos de auditoría.
*   **Gestión de Días No Laborales:** Incluye un registro de días feriados para prever comportamientos en el histórico de tasas durante fechas donde el mercado bancario no opera.

---

## 3. Explicación Técnica

Este desarrollo ha sido optimizado para la arquitectura de **Odoo 18**, siguiendo las mejores prácticas de extensibilidad.

### Arquitectura de Componentes:
1.  **Modelo `res.currency.rate`**: Se hereda y se extiende con el método `actualizar_tasa_bcv_ves()`. Este método actúa como el orquestador que consume el servicio de la API y genera los registros de tasas (`res.currency.rate`) para las monedas VES y EUR.
2.  **Configuración Persistente**: Utiliza el modelo `res.config.settings` para gestionar el parámetro `exchange_rate_round_method`. Este valor se almacena en el sistema mediante `ir.config_parameter`, permitiendo que la lógica de redondeo sea accesible globalmente.
3.  **Manejo de Monedas**:
    *   **USD**: Se toma como base para actualizar la moneda de referencia (VES).
    *   **EUR**: Se calcula dinámicamente (`usd_rate / eur_rate`) para mantener la proporción exacta respecto al dólar dentro de la tabla de tasas de Odoo.
4.  **Gestión de Feriados**: El modelo `res.holiday` permite registrar fechas especiales que el sistema puede consultar para validaciones lógicas antes de la ejecución de procesos automáticos.
5.  **Migración y Compatibilidad**: Se han eliminado dependencias obsoletas como `decimal_precision` (depreciado en v18) y se ha actualizado la sintaxis de los métodos `set_values` y `get_values`.

> **Nota para desarrolladores:** El proceso de actualización está diseñado para ser disparado mediante un *Cron* externo o interno llamando a `_save_exchange_rate()` en el modelo base de la API.

---

## 4. Guía de Uso

### Configuración Inicial
1.  **Instalación**: Instalar el módulo `api_rate_currency` desde el menú de Aplicaciones.
2.  **Ajustes de Tasa**: 
    *   Vaya a **Contabilidad / Ajustes**.
    *   Localice la sección **Gestión del tipo de cambio**.
    *   Seleccione el método deseado: 
        *   *Redondear*: Aplica redondeo matemático estándar.
        *   *Truncar*: Corta los decimales excedentes sin alterar el valor entero.
3.  **Días Feriados**: Si desea excluir días específicos, puede gestionarlos desde el menú de configuración en la tabla de **Días Feriados**.

### Funcionamiento Diario
El sistema está preparado para funcionar de forma totalmente automática. 
*   **Actualización Automática**: Un proceso programado (Cron) se ejecuta diariamente (usualmente a las 10:00 AM) para buscar la nueva tasa y aplicarla.
*   **Verificación**: Puede verificar las tasas creadas en **Contabilidad -> Configuración -> Monedas**, seleccionando VES o EUR y revisando la pestaña de "Tasas".

### Consideraciones:
*   Asegúrese de que las monedas **USD**, **EUR** y **VES** estén activas en su base de datos.
*   El sistema requiere acceso a internet para conectar con el servicio de tasas.

---

*Desarrollado por Ing Gabriel Torrealba (Software Engineer) para el ecosistema Odoo.*