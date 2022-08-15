# KSE workshop

Repository demonstrating usage of Docker and Docker Compose.

## Architecture

- Redis - used to store JWT tokens to access API;
- PostgreSQL - used to store user data persistently;
- FastAPI image - actual app, sample app with authorization and data pull using tokens.

## Examples

Methods can be found in `example.py` file.

Documentation is created automatically and can be found in [localhost:8090/docs](localhost:8090/docs) after app is started.
