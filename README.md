# 🎮 Gaming of a Lifetime: Personal Data Analytics Dashboard

**A comprehensive, interactive analytics platform to visualize and analyze your personal video game history across decades.**

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-FF4B4B.svg)](https://streamlit.io/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14-336791.svg)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED.svg)](https://www.docker.com/)

---

## 🌟 Overview

**Gaming of a Lifetime** is a data-driven web application designed to track, visualize, and analyze a lifetime of gaming habits. It transforms raw personal data (game name, console, genre, hours played, personal scores) into high-fidelity interactive visualizations, providing insights into platform preferences, genre evolution, and scoring trends.

The platform goes beyond simple tracking by cross-referencing personal data with industry-standard benchmarks from **Metacritic** (scores and sales) and **How Long To Beat** (completion times).

---

## 🚀 Key Features

### 1. Interactive EDA Dashboard
- **Platform Analytics:** Dynamic treemaps and sunburst charts to explore game distribution by brand (Sony, Microsoft, Nintendo, etc.) and specific console models.
- **Genre Insights:** Real-time breakdown of gaming habits by genre and sub-genre.
- **Backlog Management:** Automated tracking of unfinished games and abandonment rates per platform.

### 2. External Data Integration
- **Metacritic Comparison:** Merge personal scores with critical reviews and user ratings to identify personal bias or "hidden gems."
- **HLTB Analysis:** Compare actual time spent playing vs. global completion averages for story-driven or completionist playthroughs.
- **Automated Scrapers:** Custom-built Python scrapers for fetching the latest data from Metacritic and HLTB.

### 3. Advanced Filtering & Exploration
- Multi-dimensional filters (year, genre, console, finished status) powered by Streamlit's reactive UI.
- Direct DataFrame exploration with pre-processed and cleaned data.

---

## 🛠 Tech Stack

### Backend & Data Processing
- **Python 3.10+**: Core logic and data manipulation.
- **Pandas & NumPy**: High-performance data wrangling and ETL.
- **SQLAlchemy & Psycopg2**: Object-Relational Mapping (ORM) and direct PostgreSQL connection.
- **Scrapy/BeautifulSoup**: Scraper logic for HLTB and Metacritic data retrieval.

### Frontend & Visualization
- **Streamlit**: Modern reactive framework for the web dashboard.
- **Plotly Express**: Interactive, hover-enabled charts (Treemaps, Scatter plots).
- **Seaborn & Matplotlib**: Static statistical visualizations for distribution analysis.
- **Pygal & Squarify**: Specialized visualizations for hierarchy and radar charting.

### Infrastructure & Operations
- **PostgreSQL 14**: Centralized relational database for persistent storage.
- **Docker & Docker Compose**: Full-stack containerization for consistent deployment.
- **Poetry**: Dependency management and environment isolation.

---

## 🏗 System Architecture

The project follows a modular architecture:

1.  **Data Ingestion Layer**: Scrapers and CSV importers fetch data into the PostgreSQL database.
2.  **Database Layer**: Tables for `gaming_lifetime` (personal), `metacritic` (market), and `how_long_to_beat` (metrics) are maintained with specialized indexes for performance.
3.  **Analytics Layer**: Python functions process the raw SQL data into analysis-ready DataFrames (handling multi-genre explosion, brand tagging, etc.).
4.  **Presentation Layer**: Multi-page Streamlit app renders interactive components.

---

## 📁 Repository Structure

```text
├── app/                        # Streamlit Application Source
│   ├── functions/              # Modular logic: db_co, analytics, filters, scrapers
│   ├── pages/                  # Multi-page dashboard layouts
│   ├── home_page.py            # Main entry point (Welcome/Overview)
│   └── pyproject.toml          # Poetry dependency manifest
├── db_data/                    # Database Infrastructure
│   ├── init.sql                # PostgreSQL Schema definition
│   ├── seed.sql                # Initial data insertion
│   └── csv/                    # Source data for initialization
├── scripts/                    # Standalone utility scripts for DB imports
├── Docker-compose.yml          # Container orchestration
└── new_features_ideas.md       # Project roadmap & upcoming features
```

---

## 🚦 Getting Started

### Prerequisites
- **Docker & Docker Compose**
- **Python 3.10+** (if running outside Docker)
- **Poetry** (recommended for local development)

### Quick Start (Dockerized)
1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Binardino/Gaming_of_a_lifetime.git
    cd Gaming_of_a_lifetime
    ```
2.  **Configure Environment**:
    Create a `.env` file in the root directory (refer to the project settings for required variables like `POSTGRES_USER`, `POSTGRES_PASSWORD`, etc.).
3.  **Launch the stack**:
    ```bash
    docker-compose up --build
    ```
4.  **Access the Dashboard**:
    Open [http://localhost:8501](http://localhost:8501) (default Streamlit port).

### Local Development (Non-Docker)
1.  Install dependencies: `poetry install`
2.  Run the app: `streamlit run app/home_page.py`

---

## 📊 Database Schema Highlights

- **`gaming_lifetime`**: The core table containing game metadata, personal scores, and play timestamps.
- **`metacritic_merged`**: A denormalized table joining personal records with Metascores, User scores, and global sales data.
- **Unique Indexes**: Implemented on `(game_name, console, published_year)` to prevent data duplication during scraping cycles.

---

## 🗺 Roadmap

Current development focuses on implementing the features detailed in `new_features_ideas.md`, including:
- **Console Genre Radar**: Visualizing platform "identity" via spider charts.
- **Hidden Gems Detector**: Highlighting games with high personal scores but low critical consensus.
- **World Development Map**: Geographic analysis of developer studios.

---

## 👤 Author

**Binardino** - [langlois.robin@gmail.com](mailto:langlois.robin@gmail.com)

---
*Created as part of a Python training and personal data visualization project.*
