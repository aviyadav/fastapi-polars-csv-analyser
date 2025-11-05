# fastapi-polars-csv-analyser

# EDA App Backend

A simple backend service for Exploratory Data Analysis (EDA) using FastAPI and Polars.  
This application allows users to upload CSV files, get dataset summaries, and perform grouped aggregations on columns.

## Tech Stack

- **FastAPI** – for building the RESTful API
- **Polars** – for high-performance DataFrame operations
- **Pydantic** – for schema validation
- **Uvicorn** – for running the ASGI server

---

## Folder Structure

```
fastapi-polars-backend/
├── api/                 # API routes
│   ├── aggregation.py
│   ├── summary.py
│   └── upload.py
├── core/                # Core config (e.g., upload path)
│   └── config.py
├── schemas/             # Pydantic schemas
│   └── eda.py
├── services/            # Business logic
│   ├── eda.py
│   └── file_processing.py
├── temp_uploads/        # Temporary CSV storage
│   └── .gitkeep
├── main.py              # App entry point
└── requirements.txt     # Dependencies
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/utkarshg1/fastapi-polars-backend.git
cd fastapi-polars-backend
```

### 2. Create and Activate Virtual Environment

```bash
uv venv
source .venv/bin/activate    # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
uv sync
```

### 4. Run the Application

```bash
uvicorn main:app --reload
```

The API will be available at: [http://localhost:8000](http://localhost:8000)

---

## API Endpoints

### 📤 Upload CSV

**POST** `/upload/`  
Upload a CSV file to start EDA.

- **FormData**: `file` (CSV only)
- **Returns**: Column names if successful

---

### 📊 Dataset Summary

**GET** `/summary/`  
Returns number of rows, columns, and column-level metadata.

- **Response**:
  ```json
  {
    "num_rows": 1000,
    "num_columns": 5,
    "columns": [
      {
        "column": "age",
        "dtype": "i32",
        "missing": 0,
        "unique": 50
      }
    ]
  }
  ```

---

### 📈 Aggregation

**GET** `/aggregate/`  
Group by a categorical column and aggregate a numerical column.

- **Query Parameters**:

  - `cat_col`: Categorical column name
  - `con_col`: Continuous (numeric) column name
  - `agg_func`: One of the following:
    - `sum`
    - `mean`
    - `min`
    - `max`
    - `count`
    - `len`
    - `median`
    - `std`
    - `n_unique` (Count distinct values)

- **Example**:

```
GET /aggregate/?cat_col=gender&con_col=salary&agg_func=mean
```

---

## Notes

- Only one CSV is stored at a time (replaces previous upload).
- File must be `.csv` format.
- Categorical column must be of string or categorical type.
- Continuous column must be numeric for aggregations.
