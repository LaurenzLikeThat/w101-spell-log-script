import psutil
import time
import re

def main():
    for pid in psutil.pids():
        if psutil.Process(pid).name() == "WizardGraphicalClient.exe":
            path = psutil.Process(pid).exe()
    try:
        log_path = "{0}\\WizardClient.log".format(path.split("\\WizardGraphicalClient.exe")[0])
    except:
        print("Game is not open, exiting script... (Open the game and try again)")
        return
    print(f"Found log path: {log_path}")
    log = open(log_path, "r")
    log.seek(0, 2)
    close = False
    try:
        while True:
            log_lines = log.readlines()
            for line in log_lines:
                if "[STAT] CombatDetails   CombatResolver::ResolveCombatRound." in line:
                    print(line[77:])
                if re.search(r"\[DBGM\] CORE_SEER.*{IsSim:0} Participant \(sc (\d+)\) is dead after DoTs, move on to the next action", line) or re.search(r"\[DBGM\] CORE_SEER.*{IsSim:0} Participant \(id (\d+)\) missed", line):
                    print(line[51:])
                if "[DBGM] CORE_SEER       Mainloop exited with return code 0, shutting down client..." in line:
                    print("Game has been closed, exiting script...")
                    close = True
            time.sleep(0.1)
            if close:
                break
    finally:
        log.close()

if __name__ == "__main__":
    main()
