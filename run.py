import uvicorn

if __name__ == "__main__":
    # Run the FastAPI app
    uvicorn.run(
        "app.main:app",  # Path to the FastAPI app instance
        host="0.0.0.0",  # Set the host to allow external connections
        port=8000,       # Specify the port to run the app
        reload=True      # Enable auto-reload for development
    )