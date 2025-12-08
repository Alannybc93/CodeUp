@echo off
echo 🚀 Subindo projeto CodeUP para GitHub...
echo.

cd /d "C:\Users\Lanny\Documents\CodeUP\codeup"

echo 1. Adicionando arquivos...
git add .

echo.
echo 2. Criando commit...
git commit -m "Atualização: %date% %time%"

echo.
echo 3. Fazendo push para GitHub...
git push origin main

echo.
echo ✅ Concluído! Projeto enviado para: https://github.com/Alannybc93/CodeUp
pause