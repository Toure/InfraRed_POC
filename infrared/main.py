import atexit
import readline

# TODO figure out another namespace option for CLI
from cli.core_args import Cli
#
#
from cli.inspector import ConfigManager
from core.logger import glob_logger
from core.logger import make_timestamped_filename

configmanager = ConfigManager()


class InfraRed(object):
    def __init__(self):
        self.log_dir = configmanager.lookup('log_dir')

    def save_results(self):
        """
        Write output to log files.
        :return: timestamped log file.
        """
        glob_logger.info("Saving History...")
        log_path = self.log_dir + make_timestamped_filename('iridium_cli_history')
        readline.write_history_file(log_path)


def main():
    infrared = InfraRed()
    atexit.register(infrared.save_results)


if __name__ == "__main__":
    import sys
    sys.exit(int(main() or 0))