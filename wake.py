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
    """設定ファイルを読み込む"""
    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print('Error: config.json が見つかりません')
        sys.exit(1)
    except json.JSONDecodeError:
        print('Error: config.json の形式が不正です')
        sys.exit(1)

def wake_device(host: str, mac_address: str):
    """SSH経由でWake on LANコマンドを実行"""
    try:
        cmd = ['ssh', host, f'wakeonlan {mac_address}']
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f'Error: Wake on LANコマンドの実行に失敗しました\n{result.stderr}')
            sys.exit(1)
        print(result.stdout)
        print(f'Wake on LANパケットを送信しました: {mac_address}')
    except subprocess.SubprocessError as e:
        print(f'Error: SSHコマンドの実行に失敗しました: {e}')
        sys.exit(1)

def main():
    """メイン処理"""
    config = load_config()

    if not config['devices']:
        print('Error: デバイスが設定されていません')
        sys.exit(1)

    # デバイス一覧から選択
    device_names = [device['name'] for device in config['devices']]
    selected = questionary.select(
        'Wake on LANを実行するデバイスを選択してください:',
        choices=device_names
    ).ask()

    if selected is None:  # Ctrl+C等でキャンセルされた場合
        print('\nキャンセルされました')
        sys.exit(0)

    # 選択されたデバイスの情報を取得
    selected_device = next(
        device for device in config['devices']
        if device['name'] == selected
    )

    # Wake on LANの実行
    wake_device(selected_device['ssh_host'], selected_device['mac_address'])

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nプログラムを終了します')
        sys.exit(0)
