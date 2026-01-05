import os
import sys
import shutil
from pathlib import Path

BLUE = "\033[94m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
RESET = "\033[0m"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def header():
    clear()
    print(f"{BLUE}This version for crack MyDockFinder (All){RESET}")
    print(f"{BLUE}Bypass MyDockFinder By @LIBDock channel{RESET}")
    print("=" * 50)

def get_exe_dir():
    """Папка, где лежит .exe (или .py при отладке)"""
    if getattr(sys, 'frozen', False):
        return Path(sys.executable).parent.resolve()
    else:
        return Path(__file__).parent.resolve()

def find_target_dir() -> Path | None:
    """Ищет MyDockFinder в приоритетных местах"""
    base = get_exe_dir()
    cwd = Path.cwd()
    candidates = [
        base / "MyDockFinder",
        base / "MyDockFinder" / "MyDockFinder",
        cwd / "MyDockFinder",
        cwd / "MyDockFinder" / "MyDockFinder",
    ]
    for cand in candidates:
        if cand.is_dir() and (cand / "Dock_64.exe").is_file():
            return cand
    return None

def copy_if_exists(src, dst, label):
    if not src.exists():
        print(f"{RED}MISSING: {label}{RESET}")
        return False
    try:
        if src.is_file():
            if dst.exists():
                dst.unlink()
            shutil.copy2(src, dst)
            print(f"{GREEN}✓ {label}{RESET}")
        elif src.is_dir():
            if dst.exists():
                if dst.is_file():
                    dst.unlink()
                else:
                    shutil.rmtree(dst)
            try:
                shutil.copytree(src, dst, dirs_exist_ok=True)
            except TypeError:
                shutil.copytree(src, dst)
            print(f"{GREEN}✓ {label} (folder){RESET}")
        return True
    except Exception as e:
        print(f"{RED}✗ FAILED: {label} — {e}{RESET}")
        return False

def bypass_libdock():
    exe_dir = get_exe_dir()
    target = find_target_dir()
    libdock = exe_dir / "W1xcedBypassLoL" / "LIBDock"

    if not libdock.exists():
        print(f"{RED}W1xcedBypassLoL/LIBDock not found. Expected in same folder as .exe.{RESET}")
        return
    if not target:
        print(f"{RED}MyDockFinder folder not found.{RESET}")
        return

    print(f"\n→ LIBDock: {libdock}")
    print(f"→ Target:  {target}")
    print("→ Bypass @LIBDock (single pass)...")
    copy_if_exists(libdock / "Dock_64.exe",      target / "Dock_64.exe",      "Dock_64.exe")
    copy_if_exists(libdock / "steam_api.dll",    target / "steam_api.dll",    "steam_api.dll")
    copy_if_exists(libdock / "steam_api64.dll",  target / "steam_api64.dll",  "steam_api64.dll")
    copy_if_exists(libdock / "steam_settings",   target / "steam_settings",   "steam_settings")
    print(f"\n{GREEN}Open Dock_64.exe and close it after the menu opens, then come back here{RESET}")
    print(f"\n{GREEN}Bypass done By @W1xced, @LIBDock{RESET}")

def manipulate_replacement():
    exe_dir = get_exe_dir()
    target = find_target_dir()
    libdock = exe_dir / "W1xcedBypassLoL" / "LIBDock"
    buckapp = libdock / "Buckapp_for_work"

    for name, p in [("LIBDock", libdock), ("Buckapp_for_work", buckapp)]:
        if not p.exists():
            print(f"{RED}Folder not found: {name} → {p}{RESET}")
            return
    if not target:
        print(f"{RED}MyDockFinder folder not found.{RESET}")
        return

    print(f"\n→ LIBDock: {libdock}")
    print(f"→ Buckapp: {buckapp}")
    print(f"→ Target:  {target}")
    print("→ Stage 1: Copy from LIBDock...")
    copy_if_exists(libdock / "Dock_64.exe",      target / "Dock_64.exe",      "Dock_64.exe")
    copy_if_exists(libdock / "steam_api.dll",    target / "steam_api.dll",    "steam_api.dll")
    copy_if_exists(libdock / "steam_api64.dll",  target / "steam_api64.dll",  "steam_api64.dll")
    copy_if_exists(libdock / "steam_settings",   target / "steam_settings",   "steam_settings")
    print("\n→ Stage 2: Overwrite from Buckapp_for_work...")
    copy_if_exists(buckapp / "Dock_64.exe",      target / "Dock_64.exe",      "Dock_64.exe (Buckapp)")
    copy_if_exists(buckapp / "steam_api.dll",    target / "steam_api.dll",    "steam_api.dll (Buckapp)")
    copy_if_exists(buckapp / "steam_api64.dll",  target / "steam_api64.dll",  "steam_api64.dll (Buckapp)")
    print(f"\n{GREEN}All done bypass Work.{RESET}")

def main():
    while True:
        header()
        print("1. Bypass Check license")
        print("2. Manipulate file replacement")
        try:
            c = input("\n> ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nBye.")
            break
        if c == "1":
            bypass_libdock()
            input("\nPress Enter to return...")
        elif c == "2":
            manipulate_replacement()
            input("\nPress Enter to return...")
        else:
            print(f"{YELLOW}Invalid.{RESET}")
            input()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n{RED}Error: {e}{RESET}")
        input()