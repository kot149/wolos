# Wake

Simple script to wake-on-lan remote devices via ssh.

## Prerequisites

- [uv](https://docs.astral.sh/uv/) installed on local machine
- `wakeonlan` command installed on SSH host

## Usage

1. Configure `config.json`
   ```sh
   cp config.example.json config.json
   ```
2. Run the script
   ```sh
   uv run wake.py
   ```
   or
   ```sh
   ./wake.sh
   ```
   or
   ```sh
   .\wake.ps1
   ```
