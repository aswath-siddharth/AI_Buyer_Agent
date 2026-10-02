import os
import json
import boto3

AWS_REGION = os.getenv("AWS_DEFAULT_REGION", os.getenv("AWS_REGION", "us-east-1"))
BEDROCK_MODEL_ID = os.getenv("BEDROCK_MODEL_ID", "us.meta.llama3-3-70b-instruct-v1:0")

_boto3_session = None

def get_boto3_session():
    global _boto3_session
    if _boto3_session is None:
        _boto3_session = boto3.Session(region_name=AWS_REGION)
    return _boto3_session

def get_secrets_manager_client():
    session = get_boto3_session()
    return session.client("secretsmanager", region_name=AWS_REGION)

def get_bedrock_runtime_client():
    session = get_boto3_session()
    return session.client("bedrock-runtime", region_name=AWS_REGION)

def load_secrets_from_secrets_manager():
    """
    Fetch Razorpay credentials from AWS Secrets Manager ('ai-buyer/secrets')
    and populate os.environ if not already set.
    """
    if os.getenv("RAZORPAY_KEY_ID") and os.getenv("RAZORPAY_KEY_SECRET"):
        return

    try:
        sm = get_secrets_manager_client()
        res = sm.get_secret_value(SecretId="ai-buyer/secrets")
        secret_json = res.get("SecretString")
        if secret_json:
            try:
                data = json.loads(secret_json)
            except json.JSONDecodeError:
                # Parse unquoted key:value format e.g. {KEY1:VAL1,KEY2:VAL2}
                raw = secret_json.strip("{} \t\r\n")
                data = {}
                for item in raw.split(","):
                    if ":" in item:
                        k, v = item.split(":", 1)
                        data[k.strip("\"' ")] = v.strip("\"' ")

            for k, v in data.items():
                if v and not os.getenv(k):
                    os.environ[k] = str(v)
            print("Loaded Razorpay credentials from AWS Secrets Manager ('ai-buyer/secrets').")
    except Exception as e:
        print(f"Notice: Could not load 'ai-buyer/secrets' from Secrets Manager ({e}). Relying on local .env.")

def get_database_url() -> str:
    """
    Resolve PostgreSQL DATABASE_URL dynamically:
    1. Direct environment variable if provided
    2. AWS Secrets Manager (fetching RDS master secret)
    3. Fallback to local SQLite if AWS is unreachable
    """
    env_url = os.getenv("DATABASE_URL")
    if env_url:
        return env_url

    try:
        sm = get_secrets_manager_client()
        # Find the secret starting with rds!db-
        secret_list = sm.list_secrets().get("SecretList", [])
        rds_secret_id = None
        for s in secret_list:
            name = s.get("Name", "")
            if name.startswith("rds!db-"):
                rds_secret_id = name
                break

        if rds_secret_id:
            val = sm.get_secret_value(SecretId=rds_secret_id)
            sec = json.loads(val.get("SecretString", "{}"))
            user = sec.get("username", "postgres")
            password = sec.get("password")
            host = os.getenv("RDS_HOST")
            if not host:
                try:
                    rds = get_boto3_session().client("rds", region_name=AWS_REGION)
                    inst_name = os.getenv("RDS_INSTANCE_NAME", "ai-buyer-db")
                    desc = rds.describe_db_instances(DBInstanceIdentifier=inst_name)
                    inst_list = desc.get("DBInstances", [])
                    if inst_list:
                        host = inst_list[0].get("Endpoint", {}).get("Address")
                except Exception:
                    pass

            port = int(os.getenv("RDS_PORT", "5432"))
            dbname = os.getenv("RDS_DBNAME", "ai_buyer")
            if user and password and host:
                return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"
    except Exception as e:
        print(f"Notice: Could not load RDS credentials from AWS Secrets Manager ({e}).")

    return "sqlite:///./ai_buyer.db"
