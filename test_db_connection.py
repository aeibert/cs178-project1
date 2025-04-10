import pymysql
import creds  # this is your existing creds file

try:
    conn = pymysql.connect(
        host=creds.host,
        user=creds.user,
        password=creds.password,
        db=creds.db,
        connect_timeout=10
    )
    print("✅ Successfully connected to the database.")
    conn.close()
except pymysql.MySQLError as e:
    print("❌ Failed to connect:")
    print(e)
