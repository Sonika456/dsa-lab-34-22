#!/bin/bash
echo " Запуск микросервисов..."
python currency_manager/app.py &
python data_manager/app.py &
python gateway/app.py &
echo "✅ Готово. Откройте: http://localhost:5000"
wait