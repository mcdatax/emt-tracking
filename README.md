# EMT-TRACKING 🚌

Seguimiento en tiempo real de autobuses EMT Madrid con predicción de retrasos.

## Stack
- **Backend:** FastAPI (Python) + Spring Boot (Java)
- **Streaming:** Redpanda (Kafka-compatible)
- **Frontend:** Angular (web) + Flutter (móvil)
- **Infra:** Docker · Kubernetes · Azure

## Arquitectura
Ver `docs/architecture/`

## Módulos
| Módulo | Tecnología | Descripción |
|---|---|---|
| emt-gateway | FastAPI | API Gateway + EMT Madrid client |
| emt-realtime | Spring Boot | Procesamiento tiempo real |
| emt-prediction | FastAPI | Serving modelos ML |
| emt-web | Angular | Dashboard web |
| emt-mobile | Flutter | App móvil |
