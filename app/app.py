import psycopg2
import redis
import time

def postgres_check():
    conn = psycopg2.connect(
        host="postgres",
        database="testdb",
        user="postgres",
        password="postgres"
    )
    print("✅ PostgreSQL Connected")
    conn.close()

def redis_check():
    r = redis.Redis(host="redis", port=6379)
    r.set("status","ok")
    print("✅ Redis Connected")

if __name__ == "__main__":
    time.sleep(10)
    postgres_check()
    redis_check()

    with open("output.txt","w") as f:
        f.write("Enterprise CI Success\n")