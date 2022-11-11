from datetime import datetime, timedelta
import logging
from pathlib import Path

LOGGER = logging.getLogger(__name__)

files = ['file1.txt.done', 'file2.txt.done', 'file3.txt.done']
filepaths = [Path(file) for file in files]


done_file_suffix = '.done'

minimum_file_age = 5
sleep = 10


def _ignore_file(one, two):
    pass

def _get_file(done_files):

    total_files = len(done_files)
    total_done_files = 3

    for done_file in done_files:
        if done_file.with_suffix("").exists():
            # This is default case when both files (.csv and .csv.done) exist.
            total_files -= 2
            total_done_files -= 1
            # When the program ´yield´s it returns the file path of the next
            # file to be uploaded. On the next call to this function, the code
            # execution will continue from here, after the ´yield´ statement.
            yield done_file.with_suffix("")
        elif not done_file_suffix:
            total_files -= 1
            total_done_files -= 1
            today = datetime.now()
            last_modified = datetime.fromtimestamp(done_file.stat().st_mtime)
            if last_modified + timedelta(0, minimum_file_age) < today:
                yield done_file
            else:
                LOGGER.debug(
                    "Waiting until %s is %s seconds old.",
                    done_file,
                    minimum_file_age,
                )
        else:
            total_files -= 1
            LOGGER.error(
                "File %s does not exist but its '.done' file does.",
                done_file.with_suffix(""),
            )
            _ignore_file(done_file, False)
    if not done_files:
        LOGGER.info("No done files found... Sleeping %i seconds.", sleep)
        print('yoooo')

        # Logging
        debug_message = (
            f"{total_files} unfinished or unknown file(s). "
            f"{total_done_files} done file(s) with no twin."
        )
        if total_files > 100:
            LOGGER.error(debug_message)
        elif total_files > 20:
            LOGGER.warning(debug_message)
        else:
            LOGGER.debug(debug_message)
    else:
        print('asdasdas')


print(_get_file([]))

for datafile in _get_file(filepaths):
    print(datafile)

