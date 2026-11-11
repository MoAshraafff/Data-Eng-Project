# Chicago Bike-Share Analytics Pipeline

Data Engineering course project — Phase 1: Proposal & Environment Setup.

Dataset: [Divvy Trip Data](https://divvy-tripdata.s3.amazonaws.com/index.html) (Chicago bike-share). See [docs/Phase1_Proposal.pdf](docs/Phase1_Proposal.pdf).

## Team

| Name | ID | Role |
|------|----|------|
| Mohamed Ashraf Gamal | 692300392 | Team lead & infrastructure |
| Ahmed Walid | 692300197 | Ingestion engineer |
| Khaled Hossam | 692400463 | Database & data quality |
| Mazen Walid | 692300202 | Orchestration & dashboard |

## Structure

```
├── docs/       # Proposals, architecture diagrams, data dictionary
├── scripts/    # Extraction and cleaning code
├── sql/        # Table schemas (DDL), quality checks, and views
├── flows/      # Kestra YAML orchestration flows
├── docker-compose.yml
├── .env.example
└── README.md
```

## How to run

You need [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.

1. Copy `.env.example` to `.env` and set your own passwords (on Windows PowerShell: `Copy-Item .env.example .env`).

   ```bash
   cp .env.example .env
   ```

2. Start PostgreSQL and pgAdmin:

   ```bash
   docker compose up -d
   ```

3. Open pgAdmin at <http://localhost:8080> and log in with `PGADMIN_DEFAULT_EMAIL` / `PGADMIN_DEFAULT_PASSWORD` from `.env`.

4. Connect to PostgreSQL: right-click **Servers → Register → Server**, then on the **Connection** tab enter:
   - Host: `postgres`
   - Port: `5432`
   - Username: `POSTGRES_USER` from `.env`
   - Password: `POSTGRES_PASSWORD` from `.env`

5. Stop the containers (data is kept in the `postgres_data` volume):

   ```bash
   docker compose down
   ```
