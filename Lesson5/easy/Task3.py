# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil
import os

new_file = __file__ + "copy"

# копуруем файл

shutil.copy(__file__, new_file)

# удалем копию

# os.remove(new_file)

