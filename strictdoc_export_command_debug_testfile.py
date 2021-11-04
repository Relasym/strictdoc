import os


print(os.system(r'poetry run strictdoc export .\docs\reqif  --output-dir output --experimental-enable-file-traceability .\tests\unit\strictdoc\import\reqif\ '))
