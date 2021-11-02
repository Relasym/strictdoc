( xcopy .\docs\reqif\ .\output\reqif\ /Y)
( xcopy .\tests\unit\strictdoc\import\reqif\ .\output\reqif\ /Y)
( cmd /k poetry run strictdoc export .\output\reqif --experimental-enable-file-traceability --output-dir output\ )
