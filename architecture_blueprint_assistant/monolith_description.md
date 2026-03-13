# Monolithic Architecture

- **Frontend Web/Mobile App**: Single client interface (browser or mobile) that sends all user actions to the monolithic backend.
- **Monolithic Backend**: Single deployable application that contains all business logic and modules in one codebase and process.
- **API & Routing Layer**: Handles HTTP requests from the frontend, routes them to the correct internal modules inside the monolith, and returns responses.
- **Authentication & User Management**: Manages sign-up, login, sessions, and user profiles within the monolithic codebase.
- **Order Management Module**: Implements core business workflows for creating, updating, and tracking orders end to end.
- **Inventory & Catalog Module**: Manages product/item data, availability, and catalog queries inside the same database schema.
- **Payments & Billing Module**: Integrates with external payment providers while keeping all payment logic and records in the monolith.
- **Reporting & Analytics**: Generates reports and aggregates metrics using the same production database and in-process jobs.
- **Relational Database**: Single shared database instance where all modules store and read data (users, orders, inventory, payments, and reports).
