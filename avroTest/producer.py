import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

schema = avro.schema.Parse(open("user.avsc", "rb").read())

writer = DataFileWriter(open("users.avro", "wb"), DatumWriter(), schema)
writer.append({"name": "Alyssa", "favorite_number": 256, "last":"mesh","test":"active"})
writer.append({"name": "Ben", "favorite_number": 7, "favorite_color": "red"})
writer.close()

print(avro.schema.Names())
schema2 = avro.schema.Parse(open("user1.avsc", "rb").read())

reader = DataFileReader(open("users.avro", "rb"), DatumReader(reader_schema=schema2))
for user in reader:
    print(user)
reader.close()
      