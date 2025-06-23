from django.shortcuts import render
from django.http import JsonResponse
import datetime
import time


def index(request):
    return render(request, 'index.html', {

    })


def timestamp_api(request, timestamp_input):
    """
    Handle timestamp API requests.
    Accepts both date strings (YYYY-MM-DD) and Unix timestamps.
    Returns JSON with unix and utc properties, or null if input is invalid.
    """
    response_data = {
        "unix": None,
        "utc": None
    }

    try:
        # Check if input is a Unix timestamp (numeric string)
        if timestamp_input.isdigit():
            # Convert Unix timestamp to datetime
            unix_timestamp = int(timestamp_input)

            # Handle milliseconds vs seconds
            if unix_timestamp > 9999999999:  # Likely milliseconds
                unix_timestamp = unix_timestamp // 1000

            dt = datetime.datetime.fromtimestamp(unix_timestamp)

            response_data["unix"] = int(timestamp_input)  # Return original input
            response_data["utc"] = (
                dt.strftime("%a, %d %b %Y %H:%M:%S GMT")
            )

        else:
            # Try to parse as date string
            # Support multiple date formats
            date_formats = [
                "%Y-%m-%d",
                "%Y/%m/%d",
                "%m-%d-%Y",
                "%m/%d/%Y"
            ]

            dt = None
            for date_format in date_formats:
                try:
                    dt = datetime.datetime.strptime(timestamp_input,
                                                    date_format)
                    break
                except ValueError:
                    continue

            if dt:
                # Convert to Unix timestamp
                unix_timestamp = int(time.mktime(dt.timetuple()))

                response_data["unix"] = unix_timestamp
                response_data["utc"] = (
                    dt.strftime("%a, %d %b %Y %H:%M:%S GMT")
                )
            else:
                # If no valid date format found, return null values
                pass

    except (ValueError, OSError, OverflowError):
        # Handle any parsing errors by returning null values
        pass

    return JsonResponse(response_data)


# Keep the old views for backward compatibility
def display(request, month, day, year):
    try:
        # Ensure parameters are integers and handle MM-DD-YYYY format
        month_int = int(month)
        day_int = int(day)
        year_int = int(year)

        # Validate date parameters
        if month_int < 1 or month_int > 12:
            return JsonResponse({"error": "Invalid month"}, status=400)

        if day_int < 1 or day_int > 31:
            return JsonResponse({"error": "Invalid day"}, status=400)

        if year_int < 1900 or year_int > 2100:
            return JsonResponse({"error": "Invalid year"}, status=400)

        # Create datetime object
        date = datetime.datetime(year_int, month_int, day_int)
        timestamp = time.mktime(date.timetuple())
        return JsonResponse(timestamp, safe=False)

    except ValueError as e:
        return JsonResponse({"error": f"Invalid date: {str(e)}"},
                            status=400)
    except Exception as e:
        return JsonResponse({"error": f"Date parsing error: {str(e)}"},
                            status=400)


def display1(request, id):
    try:
        datestring = id
        dt = datetime.datetime.fromtimestamp(float(datestring))
        return JsonResponse(dt, safe=False)
    except (ValueError, OSError, OverflowError) as e:
        return JsonResponse({"error": f"Invalid timestamp: {str(e)}"},
                            status=400)
