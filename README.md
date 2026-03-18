# wolos: Wake-on-LAN over SSH

A simple script to send Wake-on-LAN packets to remote devices over SSH.

```mermaid
graph LR
    subgraph Remote
        B(SSH Host) -- Wake on LAN --> C(Target Machine)
    end

    A(Local Machine) -- SSH --> B
```

## Prerequisites

- [uv](https://docs.astral.sh/uv/) installed on local machine
- On SSH host: `wakeonlan` command, or [uvx](https://docs.astral.sh/uv/concepts/tools/) (falls back to `uvx wakeonlan` when `wakeonlan` is not found)

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
   ./wolos
   ```
   or
   ```sh
   uv run wolos.py
   ```
