import psutil

def main():
    for pid in psutil.pids():
        try:
            if psutil.Process(pid).name() == "WizardGraphicalClient.exe":
                path = psutil.Process(pid).exe()
        except psutil.NoSuchProcess:
            continue
    log_path = "{0}\\WizardClient.log".format(path.split("\\WizardGraphicalClient.exe")[0])
    print(f"Log path: {log_path}")
    old_length = 0
    while True:
        with open(log_path, "r") as log:
            log.seek(0)
            log_lines = log.readlines()
            new_length = len(log_lines)
            new_log_lines = []
            if new_length > old_length:
                new_log_lines = log_lines[old_length:new_length]
            elif new_length < old_length:
                new_log_lines = log_lines
            for line in new_log_lines:
                if "[STAT] CombatDetails   CombatResolver::ResolveCombatRound." in line:
                    print(line[77:])
            old_length = new_length

if __name__ == "__main__":
    main()
