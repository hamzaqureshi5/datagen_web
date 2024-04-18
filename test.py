# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# # Create the SQLAlchemy engine
# engine = create_engine(
#     #    "host=localhost port=5001 dbname=postgres user=postgres password=1234 connect_timeout=10 sslmode=prefer"
#     "postgresql://postgres:1234@localhost:5001/postgres"
# )  # Replace with your database URI

# # Create a base class for declarative class definitions
# Base = declarative_base()


# # Define your document model
# class Document(Base):
#     __tablename__ = "documents"

#     id = Column(Integer, primary_key=True)
#     title = Column(String)
#     content = Column(String)


# # Define your table model for YourTable
# class YourTable(Base):
#     __tablename__ = "your_table_name"  # Replace with the actual table name

#     # Define columns
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     age = Column(Integer)


# # Define your table model for TextData
# class TextData(Base):
#     __tablename__ = "text_data"  # Replace with the actual table name

#     # Define columns
#     id = Column(Integer, primary_key=True)
#     filename = Column(String)
#     content = Column(Text)  # Store text data as a Text column


# # Create the database tables
# Base.metadata.create_all(engine)

# # Create a session to interact with the database
# Session = sessionmaker(bind=engine)
# session = Session()

# # # Create and save a document
# # new_document = Document(title="Example Document", content="Lorem ipsum dolor sit amet.")
# # session.add(new_document)
# # session.commit()

# # Query data from YourTable
# data_from_your_table = session.query(YourTable).all()

# # Save text data to TextData table
# for row in data_from_your_table:
#     text_data = TextData(
#         filename=f"{row.name}.txt",
#         content=f"ID: {row.id}, Name: {row.name}, Age: {row.age}",
#     )
#     session.add(text_data)

# # # Close the session
# session.close()

from sqlalchemy import create_engine, Column, Integer, String, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the SQLAlchemy engine
engine = create_engine("postgresql://postgres:1234@localhost:5001/postgres")

# Create a base class for declarative class definitions
Base = declarative_base()


# Define your table model
class TextFile(Base):
    __tablename__ = "text_files"

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    file_data = Column(LargeBinary)


# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Read the contents of the .txt file as binary data
file_path = "requirements.txt"  # Replace with the path to your .txt file
with open(file_path, "rb") as file:
    file_data = file.read()

# Create a TextFile instance and insert it into the database
text_file = TextFile(filename="requirements.txt", file_data=file_data)
session.add(text_file)
session.commit()

# Close the session
session.close()
