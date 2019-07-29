## 用户生成AirMemo 发行版
mkdir A
PyInstaller -F be-aes.py
rm -rf bulid 
rm be-aes.spec
mv dist ../../A
mv dist user_key

PyInstaller -F main.py
mv dist/main ../A

mv AirMemo.db ../A
rm -rf .