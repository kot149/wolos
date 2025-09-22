# Wake

A simple script to Wake-on-LAN remote devices via SSH.

```mermaid
graph LR
    subgraph Remote
        B(SSH Host) -- Wake on LAN --> C(Target Machine)
    end

    A(Local Machine) -- SSH --> B
```

## Prerequisites

- [uv](https://docs.astral.sh/uv/) installed on local machine
- `wakeonlan` command installed on SSH host

## Usage

1. Configure `config.json`
   ```sh
   cp config.example.json config.json
   ```
   ```sh
   edit config.json
   ```
2. Run the script
   ```sh
   ./wake
   ```
   or
   ```sh
   uv run wake.py
   ```
