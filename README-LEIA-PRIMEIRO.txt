EL FLACO TJS OPTIMIZED — pacote para gerar o EXE do Windows

Este pacote foi preparado para compilar o aplicativo em um ambiente Windows na nuvem.
Você NÃO precisa instalar Python no seu PC para executar o EXE final. A compilação é feita pelo GitHub Actions.

PASSOS
1. Entre em https://github.com e crie uma conta, se ainda não tiver.
2. Crie um repositório novo. Pode chamar: el-flaco-tjs-optimized
3. Extraia este ZIP no seu computador.
4. Envie os arquivos extraídos ao repositório (incluindo a pasta .github/workflows).
   Importante: no GitHub, use "Add file" > "Upload files" e arraste os arquivos. A pasta .github precisa ser incluída.
5. Abra a aba "Actions" do repositório.
6. Se aparecer uma confirmação para habilitar workflows, aceite.
7. Abra a execução chamada "Build Windows EXE" e aguarde ficar verde (concluída).
8. Clique na execução concluída, desça até "Artifacts" e baixe "EL-FLACO-TJS-OPTIMIZED-Windows".
9. Extraia o ZIP baixado. Dentro estará EL_FLACO_TJS_OPTIMIZED.exe.
10. No Windows, execute o arquivo. Baixe apenas o artefato do seu próprio repositório.

SEGURANÇA
- O workflow compila apenas o app.py incluído neste projeto usando PyInstaller.
- Não desative o Microsoft Defender para executar o app.
- O Windows pode mostrar aviso para aplicativos não assinados. Isso não prova, por si só, que o app é malware; verifique a origem e faça uma verificação de segurança antes de abrir.
- O aplicativo não promete aumento de FPS. A versão atual oferece diagnóstico básico, limpeza de arquivos temporários, atalho para Modo de Jogo e checklist.
