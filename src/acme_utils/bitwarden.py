import subprocess
import os
import json
import logging
import shutil

logger = logging.getLogger(__name__)

if shutil.which("bws") is None:
    raise RuntimeError(
        "The 'bws' CLI is required but was not found. Please install the Bitwarden"
        " Secrets Manager CLI and ensure it is available in your PATH."
    )

# ===== シークレット情報の取得 =====
def get_secret_from_bitwarden(secret_key: str) -> str:
    """Retrieve a secret's value from Bitwarden by key using ``bws secret list``."""
    access_token = os.getenv("BWS_ACCESS_TOKEN")
    if access_token is None:
        raise RuntimeError("BWS_ACCESS_TOKEN environment variable is not set.")
    try:
        result = subprocess.run(
            ["bws", "secret", "list", "--access-token", access_token],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        logger.error("Bitwarden CLI failed: %s", exc.stderr.strip() if exc.stderr else exc)
        raise RuntimeError("Failed to list secrets from Bitwarden") from exc

    try:
        secrets_json = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        logger.error("Invalid JSON output while listing secrets: %s", exc.msg)
        raise RuntimeError("Bitwarden returned invalid JSON while listing secrets") from exc

    for entry in secrets_json:
        if entry.get("key") == secret_key:
            return entry.get("value")

    raise RuntimeError(f"Secret with key '{secret_key}' not found in Bitwarden")
