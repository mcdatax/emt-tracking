# ADR-001: Decisiones de Stack Tecnológico

## Estado: Aceptado

## Decisiones

| Decisión | Alternativas descartadas | Razón |
|---|---|---|
| FastAPI sobre Django | Django REST | Performance async, tipado, OpenAPI automático |
| Spring Boot 3 | Quarkus | Estándar empresas españolas (Indra, everis, GMV) |
| Redpanda sobre Kafka | Kafka puro | Mismo protocolo, sin ZooKeeper, más simple en local |
| Angular sobre React | React, Vue | Alta demanda en España para perfiles Java full-stack |
| UV sobre Poetry | pip, Poetry | 10-100x más rápido, estándar emergente 2025 |
| Temurin sobre Oracle JDK | Oracle JDK | Sin restricciones de licencia comercial |
