#!/bin/bash

# Mensagem de commit padrão
COMMIT_MSG="Atualização de todos os projetos"

# Loop por todas as pastas dentro do diretório atual
for dir in */ ; do
    if [ -d "$dir/.git" ]; then
        echo "Processando repositório: $dir"
        cd "$dir"

        git add .
        git commit -m "$COMMIT_MSG"
        git push origin main

        cd ..
    else
        echo "Ignorando pasta (não é git): $dir"
    fi
done

echo "Todos os repositórios foram processados."
