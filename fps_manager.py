import os
import time
import random

def get_fps():
    """
    本来はここで実FPSを取得する。
    ここではデモとしてランダム値を返す。
    """
    return random.randint(1, 60)

while True:
    fps = get_fps()
    print("="*60)
    print(f"現在のFPS: {fps}")
    print("="*60)

    # =====================================================
    # 対応段階（実運用系コマンドを含む）
    # =====================================================

    if fps >= 30:
        print("✅ FPS安定: 通常運用。特に対応不要。")

    elif 20 <= fps < 30:
        print("ℹ FPS低下: 軽負荷モードに移行。")
        # ★ 運用系処理例
        os.system("taskkill /IM notepad.exe /F")   # 不要アプリ(例:メモ帳)を終了
        os.system("ipconfig /flushdns")            # ネットワーク負荷軽減
        print("　→ 不要プロセス終了、ネットワーク負荷軽減")

    elif 15 <= fps < 20:
        print("⚠ FPSさらに低下: 画質を落とし省電力。")
        # ★ 運用系処理例
        os.system("powercfg /setactive scheme_max")  # 最大省電力モードに変更
        print("　→ 電源プランを省電力に変更")

    elif 10 <= fps < 15:
        print("⚠ FPS危険水準: 重要でない処理を全停止。")
        # ★ 運用系処理例
        os.system("taskkill /F /IM chrome.exe")     # ブラウザを強制終了
        os.system("taskkill /F /IM explorer.exe")   # エクスプローラーを終了
        print("　→ ブラウザ・エクスプローラー停止")

    elif fps < 10:
        print("🚨 FPS極端低下: システムを安全に停止します。")
        # ★ 運用系処理例
        time.sleep(5)  # 警告表示
        os.system("shutdown /s /t 0")               # シャットダウン
        break

    time.sleep(1)
