# Microservices Architecture

- **Client Web/Mobile App**: Frontend that calls the backend through the API Gateway only.
- **API Gateway**: Single public entry point that routes external requests to individual backend services, handles rate limiting, and basic request validation.
- **Auth Service**: Standalone service that manages user registration, login, tokens, and session validation using its own Auth DB.
- **Order Service**: Manages the lifecycle of orders (create, update, cancel), coordinating with Inventory and Payment services and storing data in its own Orders DB.
- **Inventory Service**: Owns product and stock data, exposes APIs for checking and updating availability, backed by its own Inventory DB.
- **Payment Service**: Handles payment authorization, capture, refunds, and interaction with external payment providers, persisting data in its own Payments DB.
- **Reporting Service**: Consumes events from other services (orders, payments, inventory changes) and builds analytical views in its own Analytics DB.
- **Notification Service**: Sends emails, SMS, and push notifications based on events from the Order and Payment services, storing templates and logs in a Notifications DB.
- **Per-Service Databases**: Each service owns its own database (Auth DB, Orders DB, Inventory DB, Payments DB, Analytics DB, Notifications DB) to ensure loose coupling and independent scaling.
