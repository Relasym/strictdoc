( xcopy .\docs\reqif\ .\output\reqif\ )
( xcopy .\tests\unit\strictdoc\import\reqif\ .\output\reqif\ )
( cmd /k poetry run strictdoc export .\output\reqif --experimental-enable-file-traceability --output-dir output\ )
