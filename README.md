# Chicago Bike-Share Analytics Pipeline

Data Engineering course project — Phase 1: Proposal & Environment Setup.

Dataset: [Divvy Trip Data](https://divvy-tripdata.s3.amazonaws.com/index.html) (Chicago bike-share). See [docs/Phase1_Proposal.pdf](docs/Phase1_Proposal.pdf).

## Team

| Name | ID |
|------|----|
| Mohamed Ashraf Gamal | 692300392 |
| Ahmed Walid | 692300197 |
| Khaled Hossam | 692400463 |
| Mazen Walid | 692300202 |

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

2. Start PostgreSQL, pgAdmin and Kestra:

   ```bash
   docker compose up -d
   ```

3. Open pgAdmin at <http://localhost:8080> and log in with `PGADMIN_DEFAULT_EMAIL` / `PGADMIN_DEFAULT_PASSWORD` from `.env`.

4. Connect to PostgreSQL: right-click **Servers → Register → Server**, then on the **Connection** tab enter:
   - Host: `postgres`
   - Port: `5432`
   - Username: `POSTGRES_USER` from `.env`
   - Password: `POSTGRES_PASSWORD` from `.env`

5. Load the pipeline into Kestra (run again whenever you edit a file in `flows/`). Use your `KESTRA_USER` / `KESTRA_PASSWORD` from `.env`:

   ```bash
   curl -u "admin@example.com:ChangeMe123" -X POST -F fileUpload=@flows/divvy_pipeline.yml http://localhost:8081/api/v1/main/flows/import
   ```

6. Open Kestra at <http://localhost:8081>, log in with the same user, open **Flows → divvy_pipeline → Execute**, and pick a year and month. The flow downloads that month of trips and loads it into the `raw.divvy_trips` table. Running a month twice does not create duplicates.

   To download a month without Kestra instead: `python scripts/extract_divvy.py 2024 6` (saves to `data/raw/`, which git ignores).

7. Stop the containers (data is kept in the Docker volumes):

   ```bash
   docker compose down
   ```
