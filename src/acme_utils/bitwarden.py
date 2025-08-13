import subprocess
import os
import json
import logging

logger = logging.getLogger(__name__)

# ===== シークレット情報の取得 =====
def get_secret_from_bitwarden(secret_name: str) -> str:
    """Bitwarden CLI を使って秘密を取得する"""
    access_token = os.getenv("BWS_ACCESS_TOKEN")
    if access_token is None:
        raise RuntimeError("BWS_ACCESS_TOKEN environment variable is not set.")
    try:
        result = subprocess.run(
            ["bws", "secret", "get", secret_name, "--access-token", access_token],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        logger.error("Bitwarden CLI failed: %s", exc.stderr.strip() if exc.stderr else exc)
        raise RuntimeError(
            f"Failed to retrieve secret '{secret_name}' from Bitwarden"
        ) from exc

    try:
        secret_json = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        logger.error(
            "Invalid JSON output for secret '%s': %s",
            secret_name,
            exc.msg,
        )
        raise RuntimeError(
            f"Bitwarden returned invalid JSON for secret '{secret_name}'"
        ) from exc
    return secret_json["value"]

