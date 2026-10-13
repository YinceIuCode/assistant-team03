# Data Directory - Smart Virtual Assistant

This directory contains sample data files and schema documentation for the Smart Virtual Assistant project.

## Data Files

### 1. `offices.csv`
Contains the list of office locations and branch details for the system.

#### Field Schema:
| Field Name | Data Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `office_id` | String | Unique identifier for the office | `OFF01` |
| `office_name` | String | Full name of the office or branch | `HCMC Head Office` |
| `address` | String | Detailed address | `123 Le Loi Street, District 1, HCMC` |
| `phone` | String | Contact phone number | `12345678900` |
| `working_hours` | String | Operating hours | `07:30 - 17:00` |

## Data Sources & Ownership

### `offices.csv`
- **Source:** HCMUS Student Handbook / Official university portal (https://www.hcmus.edu.vn)
- **Data Owner:** Data Engineering Lead
- **Update Frequency:** Weekly
- **Purpose:** Provides office locations, working hours, and contact information for assistant retrieval.