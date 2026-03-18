#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#   "questionary>=2.1.0",
# ]
# ///

import json
import subprocess
import sys
import questionary

def load_config():
    """Load config.json"""
    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print('Error: config.json not found')
        sys.exit(1)
    except json.JSONDecodeError:
        print('Error: config.json is invalid')
        sys.exit(1)

def wake_device(host: str, mac_address: str):
    """Execute Wake on LAN command via SSH"""
    def run_wol(cmd_str: str):
        cmd = ['ssh', host, cmd_str]
        return subprocess.run(cmd, capture_output=True, text=True)

    try:
        result = run_wol(f'wakeonlan {mac_address}')
        if result.returncode != 0 and 'not found' in result.stderr.lower():
            result = run_wol(f'uvx wakeonlan {mac_address}')
        if result.returncode != 0:
            print(f'Error: Failed to execute Wake on LAN command\n{result.stderr}')
            sys.exit(1)
        print(result.stdout)
        print(f'Sent Wake on LAN packet to {mac_address}')
    except subprocess.SubprocessError as e:
        print(f'Error: Failed to execute SSH command: {e}')
        sys.exit(1)

def main():
    """Main process"""
    config = load_config()

    if not config['devices']:
        print('Error: No devices are configured')
        sys.exit(1)

    # Select device from the list
    device_names = [device['name'] for device in config['devices']]
    selected = questionary.select(
        'Select a device to execute Wake on LAN:',
        choices=device_names
    ).ask()

    if selected is None:  # Canceled by Ctrl+C etc.
        print('\nCanceled')
        sys.exit(0)

    # Get the information of the selected device
    selected_device = next(
        device for device in config['devices']
        if device['name'] == selected
    )

    # Execute Wake on LAN
    wake_device(selected_device['ssh_host'], selected_device['mac_address'])

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nProgram terminated')
        sys.exit(0)
