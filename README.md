# Timestamp Microservice

A Django-based microservice that handles timestamp conversions between date strings and Unix timestamps.

## Features

- Convert date strings to Unix timestamps
- Convert Unix timestamps to date strings
- Handle invalid inputs gracefully by returning null values
- Support multiple date formats
- RESTful API endpoints

## API Endpoints

### Unified Timestamp API

**Endpoint:** `/api/timestamp/{input}/`

This endpoint accepts any string input and attempts to parse it as either:
- A Unix timestamp (numeric string)
- A date string in various formats (YYYY-MM-DD, YYYY/MM/DD, MM-DD-YYYY, MM/DD/YYYY)

**Response Format:**
```json
{
  "unix": 1451001600000,
  "utc": "Fri, 25 Dec 2015 00:00:00 GMT"
}
```

**Handling Invalid Inputs:**

The API specifically handles the test case: *"If it does not contain a date or Unix timestamp, it returns null for those properties."*

When the input is neither a valid date nor a valid Unix timestamp, the API returns:
```json
{
  "unix": null,
  "utc": null
}
```

**Examples:**

Valid inputs:
- `/api/timestamp/2015-12-25/` → Returns valid unix and utc values
- `/api/timestamp/1451001600000/` → Returns valid unix and utc values

Invalid inputs (return null):
- `/api/timestamp/invalid-input/` → Returns null for both properties
- `/api/timestamp//` → Returns null for both properties
- `/api/timestamp/abc123def456/` → Returns null for both properties
- `/api/timestamp/13-45-2023/` → Returns null for both properties
- `/api/timestamp/-1451001600000/` → Returns null for both properties

### Legacy Endpoints

- `/MM-DD-YYYY/` - Date format endpoint
- `/{unix_timestamp}/` - Unix timestamp endpoint

## Running the Service

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Start the development server:
```bash
python manage.py runserver
```

4. Test the API:
```bash
python demo_api.py
```

## Running Tests

```bash
python manage.py test microservice.tests.TimestampAPITestCase
```

The test suite includes comprehensive tests for:
- Valid date strings
- Valid Unix timestamps
- Invalid inputs (returning null)
- Empty strings
- Malformed dates
- Negative timestamps
- Response structure validation

## Implementation Details

The `timestamp_api` view function in `microservice/views.py` handles the core logic:

1. **Input Validation**: Checks if the input is a numeric string (Unix timestamp)
2. **Date Parsing**: Attempts to parse the input as a date string using multiple formats
3. **Error Handling**: Catches all parsing errors and returns null values
4. **Response Format**: Always returns a consistent JSON structure with `unix` and `utc` properties

The implementation ensures that any input that cannot be parsed as either a valid date or Unix timestamp will return `null` for both properties, satisfying the specific test case requirement.
