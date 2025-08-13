import subprocess
import os
import json

# ===== シークレット情報の取得 =====
def get_secret_from_bitwarden(secret_name: str) -> str:
    """Bitwarden CLI を使って秘密を取得する"""
    access_token = os.getenv("BWS_ACCESS_TOKEN")
    if access_token is None:
        raise RuntimeError("BWS_ACCESS_TOKEN environment variable is not set.")
    result = subprocess.run(
        ["bws", "secret", "get", secret_name, "--access-token", access_token],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True
    )
    secret_json = json.loads(result.stdout)
    return secret_json["value"]

