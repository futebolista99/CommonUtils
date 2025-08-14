# AcmeUtils

## Project Purpose
AcmeUtils provides small personal utilities, such as retrieving secrets from Bitwarden, to simplify common development tasks.

## Installation
1. Clone this repository.
2. From the project root, install the package:
   ```bash
   pip install -e .
   ```

## Usage
Example of fetching a secret stored in Bitwarden:
```python
from acme_utils.bitwarden import get_secret_from_bitwarden

# Ensure the BWS_ACCESS_TOKEN environment variable is set
secret = get_secret_from_bitwarden("my/secret/key")
print(secret)
```

To check the installed version:
```python
from acme_utils import __version__
print(__version__)
```

## Development Guidelines
- Requires Python 3.10 or newer.
- Keep code formatted and linted.
- Run tests with `pytest` before committing changes.

## License
This project is released under the MIT License. See the LICENSE file for details.
