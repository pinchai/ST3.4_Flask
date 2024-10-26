from sqlalchemy import create_engine, text

def connection():
    try:
        # Connect to the database
        engine = create_engine("mysql+mysqlconnector://root:mysql@127.0.0.1/st34_pos")
        # Test the connection
        connection = engine.connect()
        return connection
    except Exception as e:
        return str(e)
