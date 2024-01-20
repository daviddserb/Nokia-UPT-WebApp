# Nokia-WebApp-UPT

This is a Python-based web application utilizing Django.

The core functionality involves importing, filtering, grouping, and performing calculations on Nokia's test data extracted from notepad files.

To access the application, user registration is required. Upon logging in, users can view tests organized by their unique IDs. Each test displays passed and failed results, along with the percentage of passed tests.
Users can also customize their experience by adding specific tests to their favorites list for easy reference.

A notable feature is the integration of Celery Beat, a scheduler, to automatically update tests whenever notepad files are edited.
