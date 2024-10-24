def process_data(callback):
    # Simulate some data processing
    print("Processing data...")
    callback()

def on_complete():
    print("Data processed successfully!")

# Passing the callback function stored in a variable
process_data(on_complete)
